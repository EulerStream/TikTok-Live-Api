"""Generate one Python SDK package from the committed OpenAPI spec.

Run from the package folder (its `pnpm run generate` does this):

    cd sdk/python/live && python3 ../common/scripts/generate.py

The folder's sdk.json says what to build:

    {
      "projectName": "TikTokLiveApiSdk",   distribution name on PyPI
      "packageName": "TikTokLiveApiSdk",      import name
      "specPackage": "live",                  optional; a key in spec/packages.json
      "version": "0.6.1"                      optional; overrides ./version.txt
    }

The package's version normally lives in version.txt beside sdk.json: each
package is versioned on its own, and the release workflow writes the new
number back there after publishing.

With `specPackage` the spec is cut down to that package's tags before
generation; without it the package gets the full spec.

Everything this writes into the package folder (the import package,
pyproject.toml, README.md, .gitignore, test/sdk_manifest.json, build/) is
git-ignored build output. CI runs the same
script.
"""

import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
COMMON_DIR = os.path.abspath(os.path.join(HERE, ".."))
PYTHON_DIR = os.path.abspath(os.path.join(COMMON_DIR, ".."))
REPO_ROOT = os.path.abspath(os.path.join(PYTHON_DIR, "..", ".."))

SPEC_PATH = os.path.join(REPO_ROOT, "spec", "openapi.json")
PACKAGES_PATH = os.path.join(REPO_ROOT, "spec", "packages.json")
TAG_NAMES_PATH = os.path.join(COMMON_DIR, "tag_names.json")
SPEC_SCRIPTS_DIR = os.path.join(REPO_ROOT, ".github", "scripts")

# openapi-python-client regenerates pyproject.toml with this placeholder; the
# real version is pinned at the end from sdk.json or the package's version.txt.
PLACEHOLDER_VERSION = "0.0.2"


def run(*command):
    subprocess.run(command, check=True)


def copy_into(source_dir, target_dir):
    """Copy every file in source_dir into target_dir, replacing same-named files."""
    if not os.path.isdir(source_dir):
        return
    for name in sorted(os.listdir(source_dir)):
        source = os.path.join(source_dir, name)
        if os.path.isfile(source):
            shutil.copy(source, os.path.join(target_dir, name))


def main() -> None:
    package_dir = os.getcwd()
    config_path = os.path.join(package_dir, "sdk.json")
    if not os.path.isfile(config_path):
        sys.exit(f"No sdk.json in {package_dir}. Run this from an SDK package folder.")
    with open(config_path, encoding="utf-8") as fh:
        sdk = json.load(fh)

    build_dir = os.path.join(package_dir, "build")
    os.makedirs(build_dir, exist_ok=True)

    # 1. Spec: copy, normalize, cut down to this package's tags if it has any,
    #    then respell the tags Python would name badly.
    build_spec = os.path.join(build_dir, "openapi.json")
    shutil.copy(SPEC_PATH, build_spec)
    run(sys.executable, os.path.join(SPEC_SCRIPTS_DIR, "normalize_spec.py"), build_spec)
    if sdk.get("specPackage"):
        run(
            sys.executable,
            os.path.join(SPEC_SCRIPTS_DIR, "filter_spec.py"),
            build_spec,
            PACKAGES_PATH,
            sdk["specPackage"],
        )
    # The generator names a group by splitting its tag at capitals, which reads
    # "OAuth" as two words; tag_names.json respells such tags for Python only.
    run(
        sys.executable,
        os.path.join(SPEC_SCRIPTS_DIR, "rename_tags.py"),
        build_spec,
        TAG_NAMES_PATH,
    )

    # 2. Templates: the generator takes one custom template folder, so the
    #    shared templates and this package's own are merged, package last.
    templates_dir = os.path.join(build_dir, "templates")
    shutil.rmtree(templates_dir, ignore_errors=True)
    os.makedirs(templates_dir)
    copy_into(os.path.join(COMMON_DIR, "templates"), templates_dir)
    copy_into(os.path.join(package_dir, "templates"), templates_dir)

    # 3. Generator config: the shared settings plus this package's names.
    with open(os.path.join(COMMON_DIR, "config.base.json"), encoding="utf-8") as fh:
        generator_config = json.load(fh)
    package = sdk["packageName"]
    generator_config.update(
        {
            "project_name_override": sdk["projectName"],
            "package_name_override": package,
            "package_version_override": PLACEHOLDER_VERSION,
            # The generator cleans up its output with ruff. Its default hooks
            # run on "." and ruff skips git-ignored folders, which is what the
            # generated package is in this repository, so the package folder
            # is named explicitly. The "." hooks keep formatting the rest.
            "post_hooks": [
                f"ruff check --fix-only {package}",
                f"ruff format {package}",
                "ruff check --fix-only .",
                "ruff format .",
            ],
        }
    )
    generator_config_path = os.path.join(build_dir, "config.json")
    with open(generator_config_path, "w", encoding="utf-8") as fh:
        json.dump(generator_config, fh, indent=2)
        fh.write("\n")

    # 4. Generate.
    run(
        "openapi-python-client",
        "generate",
        "--path", build_spec,
        "--output-path", "./",
        "--overwrite",
        "--config", generator_config_path,
        "--custom-template-path", templates_dir,
    )

    # The published code must be the cleaned-up code. If ruff did not reach the
    # package (see post_hooks above), stop here rather than ship raw output.
    run("ruff", "format", "--check", "--quiet", package)

    # 5. Test manifest, then the real version.
    run(sys.executable, os.path.join(HERE, "render_manifest.py"))
    version = sdk.get("version")
    if not version:
        with open(os.path.join(package_dir, "version.txt"), encoding="utf-8") as fh:
            version = fh.read().strip()
    run("poetry", "version", version)


if __name__ == "__main__":
    main()

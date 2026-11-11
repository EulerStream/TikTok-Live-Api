"""Emit a manifest of a generated SDK package's API surface for its tests.

The Python SDKs are generated from the OpenAPI spec by openapi-python-client.
This script scans the *generated output* (not the spec) so the manifest is the
generator's realized view of the spec, and writes it to test/sdk_manifest.json
in the package folder.

The shared basic tests read that manifest instead of hardcoding API module and
model names, so they never go stale when the spec adds, renames, or removes
API groups or schemas.

Run from the package folder after generation (generate.py does this):
    python3 ../common/scripts/render_manifest.py
"""

import ast
import json
import os
import sys

PACKAGE_ROOT = os.getcwd()
MANIFEST_PATH = os.path.join(PACKAGE_ROOT, "test", "sdk_manifest.json")


def load_package_name() -> str:
    """The import name of the package generated in this folder, from sdk.json."""
    config_path = os.path.join(PACKAGE_ROOT, "sdk.json")
    if not os.path.isfile(config_path):
        sys.exit(f"No sdk.json in {PACKAGE_ROOT}. Run this from an SDK package folder.")
    with open(config_path, encoding="utf-8") as fh:
        return json.load(fh)["packageName"]


def discover_api_modules(package_dir: str) -> list[str]:
    """Every subpackage of <package>.api (one per OpenAPI tag)."""
    api_dir = os.path.join(package_dir, "api")
    if not os.path.isdir(api_dir):
        sys.exit(f"API directory not found: {api_dir}. Run codegen first.")
    modules = [
        name
        for name in os.listdir(api_dir)
        if name != "__pycache__"
        and os.path.isfile(os.path.join(api_dir, name, "__init__.py"))
    ]
    if not modules:
        sys.exit(f"No API modules discovered under {api_dir}.")
    return sorted(modules)


def discover_models(package_dir: str) -> list[str]:
    """The __all__ exports declared by <package>.models.__init__."""
    models_init = os.path.join(package_dir, "models", "__init__.py")
    if not os.path.isfile(models_init):
        sys.exit(f"models __init__ not found: {models_init}. Run codegen first.")
    tree = ast.parse(open(models_init, encoding="utf-8").read(), models_init)
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "__all__" for t in node.targets
        ):
            value = ast.literal_eval(node.value)
            return sorted(value)
    sys.exit(f"Could not find __all__ in {models_init}.")


def main() -> None:
    package = load_package_name()
    package_dir = os.path.join(PACKAGE_ROOT, package)
    manifest = {
        "package": package,
        "api_modules": discover_api_modules(package_dir),
        "models": discover_models(package_dir),
    }
    os.makedirs(os.path.dirname(MANIFEST_PATH), exist_ok=True)
    with open(MANIFEST_PATH, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2)
        fh.write("\n")
    print(
        f"Wrote {MANIFEST_PATH}: "
        f"{len(manifest['api_modules'])} API modules, "
        f"{len(manifest['models'])} models"
    )


if __name__ == "__main__":
    main()

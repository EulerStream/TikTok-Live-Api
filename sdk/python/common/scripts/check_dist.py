"""Check that a built Python SDK package actually contains its code.

The generated sources are git-ignored in this repository, and Poetry leaves
VCS-ignored files out of a build unless pyproject.toml includes them
explicitly. A build that silently drops them still succeeds and produces a
wheel with nothing but metadata, so this script opens what `poetry build`
wrote to dist/ and looks.

Run from the package folder after `poetry build`:
    python3 ../common/scripts/check_dist.py
"""

import glob
import json
import os
import sys
import tarfile
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
COMMON_DIR = os.path.abspath(os.path.join(HERE, ".."))
ALIAS_NAME = "EulerApiSdk"
ALIAS_SOURCE = os.path.join(COMMON_DIR, "alias", ALIAS_NAME, "__init__.py")


def newest(pattern):
    matches = sorted(glob.glob(pattern), key=os.path.getmtime)
    if not matches:
        sys.exit(f"check_dist: nothing matches {pattern}. Run `poetry build` first.")
    return matches[-1]


def required_files(sdk):
    package = sdk["packageName"]
    files = [
        f"{package}/__init__.py",
        f"{package}/py.typed",
        f"{package}/client.py",
        f"{package}/api/__init__.py",
        f"{package}/models/__init__.py",
    ]
    if sdk.get("deprecatedAlias"):
        files.append(f"{ALIAS_NAME}/__init__.py")
    return files


def check_archive(label, names, read, sdk):
    """names maps an in-package path to its archive member; read returns its bytes."""
    problems = []
    for path in required_files(sdk):
        if path not in names:
            problems.append(f"{label} is missing {path}")
    alias_path = f"{ALIAS_NAME}/__init__.py"
    if sdk.get("deprecatedAlias") and alias_path in names:
        with open(ALIAS_SOURCE, "rb") as fh:
            if read(names[alias_path]) != fh.read():
                problems.append(f"{label}: {alias_path} differs from the shared alias source")
    if any("__pycache__" in path for path in names):
        problems.append(f"{label} contains __pycache__ files")
    return problems


def main() -> None:
    with open("sdk.json", encoding="utf-8") as fh:
        sdk = json.load(fh)

    problems = []

    wheel_path = newest(os.path.join("dist", "*.whl"))
    with zipfile.ZipFile(wheel_path) as wheel:
        names = {name: name for name in wheel.namelist()}
        problems += check_archive(os.path.basename(wheel_path), names, wheel.read, sdk)

    sdist_path = newest(os.path.join("dist", "*.tar.gz"))
    with tarfile.open(sdist_path) as sdist:
        # Every sdist member sits under one "<name>-<version>/" folder.
        names = {member.name.split("/", 1)[1]: member for member in sdist.getmembers() if "/" in member.name}
        problems += check_archive(
            os.path.basename(sdist_path),
            names,
            lambda member: sdist.extractfile(member).read(),
            sdk,
        )

    if problems:
        sys.exit("check_dist: FAILED\n  " + "\n  ".join(problems))
    print(f"check_dist: OK ({os.path.basename(wheel_path)}, {os.path.basename(sdist_path)})")


if __name__ == "__main__":
    main()

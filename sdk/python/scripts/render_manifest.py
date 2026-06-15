"""Emit a manifest of the generated SDK's API surface for the test suite.

The Python SDK is generated from the live OpenAPI spec
(https://api.eulerstream.com/dashboard/openapi) by openapi-python-client.
This script scans the *generated output* (not the spec) so the manifest is the
generator's realized view of the spec, and writes it to test/sdk_manifest.json.

test/test_basic.py reads that manifest instead of hardcoding API module and
model names, so the tests never go stale when the spec adds, renames, or removes
API groups or schemas.

Run after generation, e.g.:
    python scripts/render_manifest.py
"""

import ast
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SDK_ROOT = os.path.join(HERE, "..")
PACKAGE_DIR = os.path.join(SDK_ROOT, "EulerApiSdk")
API_DIR = os.path.join(PACKAGE_DIR, "api")
MODELS_INIT = os.path.join(PACKAGE_DIR, "models", "__init__.py")
MANIFEST_PATH = os.path.join(SDK_ROOT, "test", "sdk_manifest.json")


def discover_api_modules() -> list[str]:
    """Every subpackage of EulerApiSdk.api (one per OpenAPI tag)."""
    if not os.path.isdir(API_DIR):
        sys.exit(f"API directory not found: {API_DIR}. Run codegen first.")
    modules = [
        name
        for name in os.listdir(API_DIR)
        if name != "__pycache__"
        and os.path.isfile(os.path.join(API_DIR, name, "__init__.py"))
    ]
    if not modules:
        sys.exit(f"No API modules discovered under {API_DIR}.")
    return sorted(modules)


def discover_models() -> list[str]:
    """The __all__ exports declared by EulerApiSdk.models.__init__."""
    if not os.path.isfile(MODELS_INIT):
        sys.exit(f"models __init__ not found: {MODELS_INIT}. Run codegen first.")
    tree = ast.parse(open(MODELS_INIT, encoding="utf-8").read(), MODELS_INIT)
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "__all__" for t in node.targets
        ):
            value = ast.literal_eval(node.value)
            return sorted(value)
    sys.exit(f"Could not find __all__ in {MODELS_INIT}.")


def main() -> None:
    manifest = {
        "api_modules": discover_api_modules(),
        "models": discover_models(),
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

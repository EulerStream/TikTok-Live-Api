"""
Tests for the final EulerApiSdk release.

EulerApiSdk was renamed: it is now tiktok-api-sdk (everything) and
tiktok-live-api-sdk (TikTok LIVE only). This folder builds one last EulerApiSdk
release with the same code as tiktok-api-sdk, a README that says where the
package went, and a warning on import. These tests check that release.

Run with: python test/test_legacy.py
"""

import importlib
import os
import subprocess
import sys
import warnings

HERE = os.path.dirname(os.path.abspath(__file__))
PACKAGE_DIR = os.path.join(HERE, "..")

sys.path.insert(0, PACKAGE_DIR)

FINAL_VERSION = "0.6.1"

passed = 0
failed = 0


def run_test(name, fn):
    """Run a single test function, tracking pass/fail."""
    global passed, failed
    print(f"  {name} ... ", end="")
    try:
        fn()
        print("OK")
        passed += 1
    except Exception as exc:
        print(f"FAILED: {exc}")
        failed += 1


def test_import_warns_and_names_both_new_packages():
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        importlib.import_module("EulerApiSdk")

    moved = [
        w for w in caught if issubclass(w.category, DeprecationWarning) and "EulerApiSdk has moved" in str(w.message)
    ]
    assert len(moved) == 1, f"expected one moved warning, got {len(moved)}"
    message = str(moved[0].message)
    assert "tiktok-api-sdk" in message, message
    assert "tiktok-live-api-sdk" in message, message


def test_package_is_the_full_client():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        sdk = importlib.import_module("EulerApiSdk")
        users = importlib.import_module("EulerApiSdk.api.tik_tok_users")
    assert hasattr(sdk, "Client"), "EulerApiSdk should export Client"
    assert hasattr(sdk, "AuthenticatedClient"), "EulerApiSdk should export AuthenticatedClient"
    # A real package, not a redirect: its modules carry its own name.
    assert users.__name__ == "EulerApiSdk.api.tik_tok_users", users.__name__


def test_readme_says_where_the_package_went():
    with open(os.path.join(PACKAGE_DIR, "README.md"), encoding="utf-8") as fh:
        readme = fh.read()
    for expected in ("tiktok-api-sdk", "tiktok-live-api-sdk", "pip uninstall EulerApiSdk"):
        assert expected in readme, f"README.md should mention {expected!r}"


def test_version_is_the_final_one():
    result = subprocess.run(["poetry", "version", "-s"], cwd=PACKAGE_DIR, capture_output=True, text=True, check=True)
    assert result.stdout.strip() == FINAL_VERSION, result.stdout


if __name__ == "__main__":
    tests = [
        ("Import warns once and names both new packages", test_import_warns_and_names_both_new_packages),
        ("Package is the full client under its old name", test_package_is_the_full_client),
        ("README says where the package went", test_readme_says_where_the_package_went),
        ("Version is the final 0.6.1", test_version_is_the_final_one),
    ]

    print(f"\nRunning {len(tests)} legacy tests...\n")
    for name, fn in tests:
        run_test(name, fn)

    print(f"\n{passed} passed, {failed} failed, {passed + failed} total\n")

    if failed > 0:
        sys.exit(1)
    else:
        print("All tests passed.")

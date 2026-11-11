"""
Surface tests for the tiktok-api-sdk Python package.

tiktok-api-sdk ships every API group: the TikTok LIVE and account groups that
tiktok-live-api-sdk also has, plus the groups that exist only here. No total is
asserted, so the spec can add groups without touching this test. The deprecated
``EulerApiSdk`` import name that the package also provides is checked too.

Run with: python test/test_surface.py
"""

import importlib
import json
import os
import sys
import warnings

HERE = os.path.dirname(os.path.abspath(__file__))
PACKAGE_DIR = os.path.join(HERE, "..")

sys.path.insert(0, PACKAGE_DIR)

PACKAGE = "TikTokApiSdk"

SHARED_WITH_LIVE = [
    "tik_tok_live",
    "tik_tok_live_gifts",
    "tik_tok_live_moderation",
    "tik_tok_web_socket_api",
    "accounts",
    "authentication",
]

GENERAL_ONLY = [
    "analytics",
    "tik_tok_general",
    "tik_tok_signing",
    "tik_tok_captchas",
    "tik_tok_users",
    "tik_tok_videos",
]

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


def load_api_modules():
    with open(os.path.join(HERE, "sdk_manifest.json"), encoding="utf-8") as fh:
        return json.load(fh)["api_modules"]


def test_every_group_present():
    modules = load_api_modules()
    for name in SHARED_WITH_LIVE + GENERAL_ONLY:
        assert name in modules, f"{PACKAGE} should include api.{name}"


def test_alias_file_matches_shared_source():
    shipped = os.path.join(PACKAGE_DIR, "EulerApiSdk", "__init__.py")
    source = os.path.join(PACKAGE_DIR, "..", "common", "alias", "EulerApiSdk", "__init__.py")
    with open(shipped, "rb") as fh:
        shipped_bytes = fh.read()
    with open(source, "rb") as fh:
        source_bytes = fh.read()
    assert shipped_bytes == source_bytes, "EulerApiSdk/__init__.py differs from the shared alias source"


def test_deprecated_import_name():
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        old = importlib.import_module("EulerApiSdk")
        new = importlib.import_module(PACKAGE)
        assert old is new, "EulerApiSdk should be the same module as TikTokApiSdk"

        old_gifts = importlib.import_module("EulerApiSdk.api.tik_tok_live_gifts")
        new_gifts = importlib.import_module(f"{PACKAGE}.api.tik_tok_live_gifts")
        assert old_gifts is new_gifts, "EulerApiSdk submodules should be the same module objects"

    deprecations = [
        w
        for w in caught
        if issubclass(w.category, DeprecationWarning) and "EulerApiSdk is deprecated" in str(w.message)
    ]
    assert len(deprecations) == 1, f"expected one DeprecationWarning, got {len(deprecations)}"
    assert PACKAGE in str(deprecations[0].message), "the warning should name the new import"


def test_deprecated_name_reaches_general_only_groups():
    # Migrating from the old EulerApiSdk package to this one is a package name
    # change only, so the old import paths for every group must still resolve.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        old_users = importlib.import_module("EulerApiSdk.api.tik_tok_users")
        new_users = importlib.import_module(f"{PACKAGE}.api.tik_tok_users")
    assert old_users is new_users, "EulerApiSdk.api.tik_tok_users should be TikTokApiSdk's module"


if __name__ == "__main__":
    tests = [
        ("Every API group is present", test_every_group_present),
        ("Shipped alias file matches the shared source", test_alias_file_matches_shared_source),
        ("Deprecated EulerApiSdk import resolves to this package and warns once", test_deprecated_import_name),
        ("Deprecated EulerApiSdk import reaches general-only groups", test_deprecated_name_reaches_general_only_groups),
    ]

    print(f"\nRunning {len(tests)} surface tests...\n")
    for name, fn in tests:
        run_test(name, fn)

    print(f"\n{passed} passed, {failed} failed, {passed + failed} total\n")

    if failed > 0:
        sys.exit(1)
    else:
        print("All tests passed.")

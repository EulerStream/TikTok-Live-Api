"""
Surface tests for the tiktok-live-api-sdk Python package.

tiktok-live-api-sdk ships the TikTok LIVE groups plus the account groups a
LIVE integration needs; everything else lives only in tiktok-api-sdk. The split
is decided by spec/packages.json. These tests pin the outcome, and check the
deprecated ``EulerApiSdk`` import name that the package also provides.

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

PACKAGE = "TikTokLiveApiSdk"

REQUIRED = [
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

EXPECTED_GROUP_COUNT = 13

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


def test_live_groups_present():
    modules = load_api_modules()
    for name in REQUIRED:
        assert name in modules, f"{PACKAGE} should include api.{name}"


def test_general_only_groups_absent():
    modules = load_api_modules()
    for name in GENERAL_ONLY:
        assert name not in modules, f"{PACKAGE} must not include api.{name}"


def test_group_count():
    modules = load_api_modules()
    assert len(modules) == EXPECTED_GROUP_COUNT, (
        f"expected {EXPECTED_GROUP_COUNT} API groups, got {len(modules)}: {modules}"
    )


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
        assert old is new, "EulerApiSdk should be the same module as TikTokLiveApiSdk"

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


def test_version_comes_from_the_package_version_file():
    # Each package has its own version.txt; the generator's placeholder version
    # in pyproject.toml must have been replaced with it.
    import tomllib

    with open(os.path.join(PACKAGE_DIR, "version.txt"), encoding="utf-8") as fh:
        expected = fh.read().strip()
    with open(os.path.join(PACKAGE_DIR, "pyproject.toml"), "rb") as fh:
        actual = tomllib.load(fh)["tool"]["poetry"]["version"]
    assert actual == expected, f"pyproject.toml has version {actual}, version.txt has {expected}"


def test_deprecated_name_has_no_general_only_groups():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        # The alias itself must resolve; only the general-only group is absent.
        importlib.import_module("EulerApiSdk")
        try:
            importlib.import_module("EulerApiSdk.api.tik_tok_users")
        except ModuleNotFoundError:
            return
    raise AssertionError("EulerApiSdk.api.tik_tok_users should not exist in the LIVE package")


if __name__ == "__main__":
    tests = [
        ("LIVE and account groups are present", test_live_groups_present),
        ("General-only groups are absent", test_general_only_groups_absent),
        ("Exactly 13 API groups", test_group_count),
        ("Shipped alias file matches the shared source", test_alias_file_matches_shared_source),
        ("Deprecated EulerApiSdk import resolves to this package and warns once", test_deprecated_import_name),
        ("Deprecated EulerApiSdk import has no general-only groups", test_deprecated_name_has_no_general_only_groups),
        ("Version comes from the package's version.txt", test_version_comes_from_the_package_version_file),
    ]

    print(f"\nRunning {len(tests)} surface tests...\n")
    for name, fn in tests:
        run_test(name, fn)

    print(f"\n{passed} passed, {failed} failed, {passed + failed} total\n")

    if failed > 0:
        sys.exit(1)
    else:
        print("All tests passed.")

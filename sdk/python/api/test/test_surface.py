"""
Surface tests for the TikTokApiSdk Python package.

TikTokApiSdk ships every API group: the TikTok LIVE and account groups that
TikTokLiveApiSdk also has, plus the groups that exist only here. No total is
asserted, so the spec can add groups without touching this test. The package
must also install nothing but its own import package.

Run with: python test/test_surface.py
"""

import json
import os
import sys

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
    "tik_tok_signing",
    "tik_tok_captchas",
    "tik_tok_users",
    "tik_tok_videos",
]

# The OAuth group follows its tag: api.tik_tok_general while the committed spec
# says "TikTok General", api.tik_tok_oauth once it carries the server's
# "TikTok OAuth" (respelled for Python in common/tag_names.json; unrespelled it
# would be api.tik_tok_o_auth).
OAUTH_GROUP = ["tik_tok_oauth", "tik_tok_general"]

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
    present = [name for name in OAUTH_GROUP if name in modules]
    assert len(present) == 1, f"{PACKAGE} should include the TikTok OAuth group exactly once, found {present}"
    assert "tik_tok_o_auth" not in modules, "the TikTok OAuth tag reached the generator unrespelled"


def test_installs_only_its_own_import_package():
    # The package must not install anything under another import name. In
    # particular it must not provide ``EulerApiSdk``: that folder belongs to the
    # old EulerApiSdk package, and writing into it breaks programs that still
    # use that package in the same environment.
    import tomllib

    with open(os.path.join(PACKAGE_DIR, "pyproject.toml"), "rb") as fh:
        packages = tomllib.load(fh)["tool"]["poetry"]["packages"]
    assert packages == [{"include": PACKAGE}], f"pyproject.toml installs {packages}"


def test_version_comes_from_the_package_version_file():
    # Each package has its own version.txt; the generator's placeholder version
    # in pyproject.toml must have been replaced with it.
    import tomllib

    with open(os.path.join(PACKAGE_DIR, "version.txt"), encoding="utf-8") as fh:
        expected = fh.read().strip()
    with open(os.path.join(PACKAGE_DIR, "pyproject.toml"), "rb") as fh:
        actual = tomllib.load(fh)["tool"]["poetry"]["version"]
    assert actual == expected, f"pyproject.toml has version {actual}, version.txt has {expected}"


if __name__ == "__main__":
    tests = [
        ("Every API group is present", test_every_group_present),
        ("Installs only its own import package", test_installs_only_its_own_import_package),
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

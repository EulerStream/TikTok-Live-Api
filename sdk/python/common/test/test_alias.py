"""Tests for the deprecated ``EulerApiSdk`` import alias.

The alias ships inside both tiktok-api-sdk and tiktok-live-api-sdk. These
tests exercise it against tiny stand-in packages, so they need no generated
SDK: each test builds a temporary site with fake ``TikTokApiSdk`` and/or
``TikTokLiveApiSdk`` packages beside a copy of the alias, then imports through
the old name in a fresh interpreter.

Run with: python3 sdk/python/common/test/test_alias.py -v
"""

import os
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ALIAS_SOURCE = os.path.join(HERE, "..", "alias", "EulerApiSdk")


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)


def make_fake_sdk(site, name, label):
    """A stand-in SDK package: <name>/__init__.py, api/__init__.py, api/gifts.py."""
    write(os.path.join(site, name, "__init__.py"), f'NAME = "{label}"\n')
    write(os.path.join(site, name, "api", "__init__.py"), "")
    write(os.path.join(site, name, "api", "gifts.py"), "VALUE = 1\n")


class AliasTests(unittest.TestCase):
    def setUp(self):
        self.site = tempfile.mkdtemp()
        self.cwd = tempfile.mkdtemp()
        shutil.copytree(ALIAS_SOURCE, os.path.join(self.site, "EulerApiSdk"))

    def tearDown(self):
        shutil.rmtree(self.site)
        shutil.rmtree(self.cwd)

    def install(self, general=False, live=False):
        if general:
            make_fake_sdk(self.site, "TikTokApiSdk", "api")
        if live:
            make_fake_sdk(self.site, "TikTokLiveApiSdk", "live")

    def run_script(self, script):
        """Run script in a fresh interpreter that sees only the temporary site."""
        env = {"PYTHONPATH": self.site, "PATH": os.environ.get("PATH", "")}
        return subprocess.run(
            [sys.executable, "-W", "always", "-c", script],
            capture_output=True,
            text=True,
            env=env,
            cwd=self.cwd,
        )

    def assert_passes(self, script):
        result = self.run_script(script)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result

    def test_resolves_to_live_when_only_live_present(self):
        self.install(live=True)
        self.assert_passes(
            "import EulerApiSdk, TikTokLiveApiSdk\n"
            "assert EulerApiSdk is TikTokLiveApiSdk\n"
        )

    def test_prefers_general_when_both_present(self):
        self.install(general=True, live=True)
        self.assert_passes(
            "import EulerApiSdk\n"
            "assert EulerApiSdk.NAME == 'api', EulerApiSdk.NAME\n"
        )

    def test_submodule_is_same_object(self):
        self.install(general=True)
        self.assert_passes(
            "import sys\n"
            "import EulerApiSdk.api.gifts as old\n"
            "import TikTokApiSdk.api.gifts as new\n"
            "assert old is new\n"
            "assert sys.modules['EulerApiSdk.api.gifts'] is new\n"
            "assert sys.modules['EulerApiSdk.api'] is sys.modules['TikTokApiSdk.api']\n"
        )

    def test_from_import_works(self):
        self.install(general=True)
        self.assert_passes(
            "from EulerApiSdk.api.gifts import VALUE\n"
            "assert VALUE == 1\n"
            "from EulerApiSdk.api import gifts\n"
            "assert gifts.VALUE == 1\n"
        )

    def test_real_module_spec_is_untouched(self):
        self.install(general=True)
        self.assert_passes(
            "import EulerApiSdk.api.gifts\n"
            "import TikTokApiSdk.api.gifts as real\n"
            "assert real.__spec__.name == 'TikTokApiSdk.api.gifts', real.__spec__.name\n"
            "assert real.__name__ == 'TikTokApiSdk.api.gifts', real.__name__\n"
            "import TikTokApiSdk.api as real_package\n"
            "assert real_package.__spec__.name == 'TikTokApiSdk.api'\n"
        )

    def test_emits_deprecation_warning_once(self):
        self.install(general=True)
        result = self.assert_passes(
            "import EulerApiSdk\n"
            "import EulerApiSdk.api\n"
            "import EulerApiSdk.api.gifts\n"
        )
        self.assertEqual(result.stderr.count("DeprecationWarning"), 1, result.stderr)
        self.assertIn("TikTokApiSdk", result.stderr)

    def test_missing_submodule_raises(self):
        self.install(general=True)
        self.assert_passes(
            "try:\n"
            "    import EulerApiSdk.api.nope\n"
            "except ModuleNotFoundError:\n"
            "    pass\n"
            "else:\n"
            "    raise SystemExit('expected ModuleNotFoundError')\n"
        )

    def test_neither_target_present_raises_import_error(self):
        self.assert_passes(
            "try:\n"
            "    import EulerApiSdk\n"
            "except ImportError as exc:\n"
            "    message = str(exc)\n"
            "    assert 'tiktok-api-sdk' in message, message\n"
            "    assert 'tiktok-live-api-sdk' in message, message\n"
            "else:\n"
            "    raise SystemExit('expected ImportError')\n"
        )

    def test_stale_files_are_ignored(self):
        # The retired EulerApiSdk distribution owned this same folder. If its
        # files are still there, the redirect must win over them.
        self.install(general=True)
        stale = os.path.join(self.site, "EulerApiSdk", "api")
        write(os.path.join(stale, "__init__.py"), "")
        write(os.path.join(stale, "gifts.py"), "VALUE = 999\n")
        self.assert_passes(
            "from EulerApiSdk.api.gifts import VALUE\n"
            "assert VALUE == 1, VALUE\n"
        )


if __name__ == "__main__":
    unittest.main()

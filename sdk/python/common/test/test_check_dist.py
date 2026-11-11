"""Tests for check_dist.py, which checks what a built Python package contains.

Run with: python3 sdk/python/common/test/test_check_dist.py -v
"""

import importlib.util
import os
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))

spec = importlib.util.spec_from_file_location("check_dist", os.path.join(HERE, "..", "scripts", "check_dist.py"))
check_dist = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_dist)

SDK = {"projectName": "TikTokApiSdk", "packageName": "TikTokApiSdk"}

COMPLETE = [
    "TikTokApiSdk/__init__.py",
    "TikTokApiSdk/py.typed",
    "TikTokApiSdk/client.py",
    "TikTokApiSdk/api/__init__.py",
    "TikTokApiSdk/models/__init__.py",
    "tiktokapisdk-0.1.0.dist-info/METADATA",
]


def problems(paths):
    return check_dist.check_archive("package.whl", {path: path for path in paths}, lambda member: b"", SDK)


class CheckArchiveTests(unittest.TestCase):
    def test_a_complete_package_passes(self):
        self.assertEqual(problems(COMPLETE), [])

    def test_missing_code_is_reported(self):
        found = problems([path for path in COMPLETE if path != "TikTokApiSdk/client.py"])
        self.assertEqual(len(found), 1, found)
        self.assertIn("TikTokApiSdk/client.py", found[0])

    def test_a_second_import_package_is_reported(self):
        # A package that also installs EulerApiSdk/ overwrites the real EulerApiSdk
        # package in any environment that has both, and breaks whatever imports it.
        found = problems(COMPLETE + ["EulerApiSdk/__init__.py"])
        self.assertEqual(len(found), 1, found)
        self.assertIn("EulerApiSdk", found[0])

    def test_compiled_files_are_reported(self):
        found = problems(COMPLETE + ["TikTokApiSdk/__pycache__/client.cpython-312.pyc"])
        self.assertEqual(len(found), 1, found)
        self.assertIn("__pycache__", found[0])


if __name__ == "__main__":
    unittest.main()

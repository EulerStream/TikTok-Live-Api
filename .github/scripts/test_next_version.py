"""Tests for next_version.py.

Run with: python3 -m unittest discover -s .github/scripts -p 'test_next_version.py' -v
"""

import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "next_version.py")

sys.path.insert(0, HERE)

import next_version  # noqa: E402


class NextVersionTests(unittest.TestCase):
    def test_major(self):
        self.assertEqual(next_version.next_version("0.8.0", "major"), "1.0.0")

    def test_minor(self):
        self.assertEqual(next_version.next_version("0.6.0", "minor"), "0.7.0")

    def test_patch(self):
        self.assertEqual(next_version.next_version("1.2.3", "patch"), "1.2.4")

    def test_minor_and_major_reset_lower_parts(self):
        self.assertEqual(next_version.next_version("1.2.3", "minor"), "1.3.0")
        self.assertEqual(next_version.next_version("1.2.3", "major"), "2.0.0")

    def test_surrounding_whitespace_is_tolerated(self):
        # version.txt ends with a newline.
        self.assertEqual(next_version.next_version("0.8.0\n", "patch"), "0.8.1")

    def test_skip_is_rejected(self):
        with self.assertRaises(ValueError):
            next_version.next_version("0.8.0", "skip")

    def test_malformed_versions_are_rejected(self):
        for current in ("1.2", "x.y.z", "1.2.3.4", "", "1.2.-3"):
            with self.subTest(current=current):
                with self.assertRaises(ValueError):
                    next_version.next_version(current, "patch")


class NextVersionCliTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run([sys.executable, SCRIPT, *args], capture_output=True, text=True)

    def test_prints_the_next_version(self):
        result = self.run_cli("0.8.0", "major")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "1.0.0\n")

    def test_bad_input_exits_non_zero(self):
        for args in (("0.8.0", "skip"), ("1.2", "patch"), ("x.y.z", "patch"), ("0.8.0",)):
            with self.subTest(args=args):
                result = self.run_cli(*args)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()

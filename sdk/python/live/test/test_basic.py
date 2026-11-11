"""
Basic tests for the TikTokLiveApiSdk Python package.

The checks themselves are shared by every Python SDK package and live in
sdk/python/common/test/basic.py; this file points them at this package.

Run with: python test/test_basic.py
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# The package under test, then the shared test code.
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "..", "common", "test"))

from basic import run_basic_tests  # noqa: E402

if __name__ == "__main__":
    sys.exit(run_basic_tests("TikTokLiveApiSdk", os.path.join(HERE, "sdk_manifest.json")))

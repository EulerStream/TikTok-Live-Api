"""
End-to-end tests for the tiktok-live-api-sdk Python package.

Makes real HTTP calls against the live API.

Run with: python test/test_e2e.py
"""

import os
import sys

# Ensure the package root is on the path so imports work when running directly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

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


# ---------------------------------------------------------------------------
# 1. get_rate_limits sync_detailed returns 200 with parsed data
#
# CI has no secrets, so this must be a route that answers without an API key.
# The TikTok LIVE routes do, but only a few times a minute per IP, so they
# return 429 on a busy runner. The rate-limit route reports those limits and is
# not itself subject to them.
# ---------------------------------------------------------------------------


def test_get_rate_limits_sync_detailed():
    from TikTokLiveApiSdk import Client
    from TikTokLiveApiSdk.api.accounts import get_rate_limits

    client = Client(base_url="https://api.eulerstream.com")
    response = get_rate_limits.sync_detailed(client=client)

    assert response.status_code.value == 200, f"Expected status 200, got {response.status_code.value}"
    assert response.parsed is not None, "Expected parsed data, got None"
    assert response.parsed.day.max_ > 0, "Expected a daily limit"


# ---------------------------------------------------------------------------
# Run all tests
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    tests = [
        ("get_rate_limits sync_detailed returns 200 with parsed data", test_get_rate_limits_sync_detailed),
    ]

    print(f"\nRunning {len(tests)} e2e tests...\n")
    for name, fn in tests:
        run_test(name, fn)

    print(f"\n{passed} passed, {failed} failed, {passed + failed} total\n")

    if failed > 0:
        sys.exit(1)
    else:
        print("All tests passed.")

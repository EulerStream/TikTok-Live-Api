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
# 1. retrieve_hashtag_list sync_detailed returns 200
#
# The hashtag list is a TikTok LIVE route that answers without an API key,
# which CI needs: the test workflow has no secrets.
# ---------------------------------------------------------------------------


def test_retrieve_hashtag_list_sync_detailed():
    from TikTokLiveApiSdk import Client
    from TikTokLiveApiSdk.api.tik_tok_live import retrieve_hashtag_list

    client = Client(base_url="https://api.eulerstream.com")
    response = retrieve_hashtag_list.sync_detailed(client=client)

    assert response.status_code.value == 200, f"Expected status 200, got {response.status_code.value}"


# ---------------------------------------------------------------------------
# Run all tests
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    tests = [
        ("retrieve_hashtag_list sync_detailed returns 200", test_retrieve_hashtag_list_sync_detailed),
    ]

    print(f"\nRunning {len(tests)} e2e tests...\n")
    for name, fn in tests:
        run_test(name, fn)

    print(f"\n{passed} passed, {failed} failed, {passed + failed} total\n")

    if failed > 0:
        sys.exit(1)
    else:
        print("All tests passed.")

"""
Basic tests for the EulerApiSdk Python SDK.

Run with: python test/test_basic.py
"""

import json
import sys
import os

# Ensure the package root is on the path so imports work when running directly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

passed = 0
failed = 0


# ---------------------------------------------------------------------------
# Manifest: the API surface is determined dynamically at codegen time.
# scripts/render_manifest.py scans the generated SDK (itself produced from the
# live OpenAPI spec) and writes test/sdk_manifest.json listing the generated API
# modules and model exports. Reading it here keeps the tests in sync with the
# spec automatically instead of hardcoding module/model names.
# ---------------------------------------------------------------------------

MANIFEST_PATH = os.path.join(os.path.dirname(__file__), "sdk_manifest.json")


def load_manifest():
    if not os.path.isfile(MANIFEST_PATH):
        raise SystemExit(
            f"Manifest not found at {MANIFEST_PATH}. "
            "Run codegen (scripts/render_manifest.py) first."
        )
    with open(MANIFEST_PATH, encoding="utf-8") as fh:
        manifest = json.load(fh)
    if not manifest.get("api_modules"):
        raise SystemExit(f"Manifest at {MANIFEST_PATH} lists no API modules.")
    if not manifest.get("models"):
        raise SystemExit(f"Manifest at {MANIFEST_PATH} lists no models.")
    return manifest


MANIFEST = load_manifest()
API_MODULES = MANIFEST["api_modules"]
EXPECTED_MODELS = MANIFEST["models"]


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
# 1. Package-level imports
# ---------------------------------------------------------------------------

def test_import_package():
    import EulerApiSdk
    assert hasattr(EulerApiSdk, "Client"), "EulerApiSdk should export Client"
    assert hasattr(EulerApiSdk, "AuthenticatedClient"), "EulerApiSdk should export AuthenticatedClient"


def test_import_client_directly():
    from EulerApiSdk.client import Client, AuthenticatedClient
    assert Client is not None
    assert AuthenticatedClient is not None


# ---------------------------------------------------------------------------
# 2. Client instantiation
# ---------------------------------------------------------------------------

def test_client_instantiation():
    from EulerApiSdk import Client
    client = Client(base_url="https://example.com")
    assert client is not None


def test_client_with_options():
    from EulerApiSdk import Client
    client = Client(
        base_url="https://example.com",
        headers={"X-Custom": "value"},
        cookies={"session": "abc"},
    )
    assert client is not None


def test_authenticated_client_instantiation():
    from EulerApiSdk import AuthenticatedClient
    client = AuthenticatedClient(base_url="https://example.com", token="test-token-123")
    assert client is not None


def test_authenticated_client_with_custom_prefix():
    from EulerApiSdk import AuthenticatedClient
    client = AuthenticatedClient(
        base_url="https://example.com",
        token="my-token",
        prefix="Token",
        auth_header_name="X-Auth",
    )
    assert client.token == "my-token"
    assert client.prefix == "Token"
    assert client.auth_header_name == "X-Auth"


# ---------------------------------------------------------------------------
# 3. Client methods exist
# ---------------------------------------------------------------------------

EXPECTED_CLIENT_METHODS = [
    "with_headers",
    "with_cookies",
    "with_timeout",
    "get_httpx_client",
    "get_async_httpx_client",
    "set_httpx_client",
    "set_async_httpx_client",
]


def test_client_has_expected_methods():
    from EulerApiSdk import Client
    client = Client(base_url="https://example.com")
    for method_name in EXPECTED_CLIENT_METHODS:
        assert hasattr(client, method_name), f"Client missing method: {method_name}"
        assert callable(getattr(client, method_name)), f"Client.{method_name} is not callable"


def test_authenticated_client_has_expected_methods():
    from EulerApiSdk import AuthenticatedClient
    client = AuthenticatedClient(base_url="https://example.com", token="tok")
    for method_name in EXPECTED_CLIENT_METHODS:
        assert hasattr(client, method_name), f"AuthenticatedClient missing method: {method_name}"
        assert callable(getattr(client, method_name)), f"AuthenticatedClient.{method_name} is not callable"


# ---------------------------------------------------------------------------
# 4. Client builder methods return new instances
# ---------------------------------------------------------------------------

def test_with_headers_returns_client():
    from EulerApiSdk import Client
    client = Client(base_url="https://example.com")
    new_client = client.with_headers({"X-New": "header"})
    assert isinstance(new_client, Client)


def test_with_cookies_returns_client():
    from EulerApiSdk import Client
    client = Client(base_url="https://example.com")
    new_client = client.with_cookies({"new_cookie": "value"})
    assert isinstance(new_client, Client)


def test_with_timeout_returns_client():
    import httpx
    from EulerApiSdk import Client
    client = Client(base_url="https://example.com")
    new_client = client.with_timeout(httpx.Timeout(30.0))
    assert isinstance(new_client, Client)


# ---------------------------------------------------------------------------
# 5. Context manager support
# ---------------------------------------------------------------------------

def test_client_context_manager():
    from EulerApiSdk import Client
    client = Client(base_url="https://example.com")
    with client as c:
        assert c is client


def test_authenticated_client_context_manager():
    from EulerApiSdk import AuthenticatedClient
    client = AuthenticatedClient(base_url="https://example.com", token="tok")
    with client as c:
        assert c is client


# ---------------------------------------------------------------------------
# 6. httpx client creation
# ---------------------------------------------------------------------------

def test_get_httpx_client():
    import httpx
    from EulerApiSdk import Client
    client = Client(base_url="https://example.com")
    httpx_client = client.get_httpx_client()
    assert isinstance(httpx_client, httpx.Client)


def test_get_async_httpx_client():
    import httpx
    from EulerApiSdk import Client
    client = Client(base_url="https://example.com")
    async_client = client.get_async_httpx_client()
    assert isinstance(async_client, httpx.AsyncClient)


def test_authenticated_get_httpx_client_sets_auth_header():
    import httpx
    from EulerApiSdk import AuthenticatedClient
    client = AuthenticatedClient(base_url="https://example.com", token="secret")
    httpx_client = client.get_httpx_client()
    assert isinstance(httpx_client, httpx.Client)
    # The auth header should have been injected
    assert "Authorization" in httpx_client.headers
    assert "secret" in httpx_client.headers["Authorization"]


# ---------------------------------------------------------------------------
# 7. API module imports
# ---------------------------------------------------------------------------

def test_api_modules_importable():
    import importlib
    for module_name in API_MODULES:
        full_name = f"EulerApiSdk.api.{module_name}"
        mod = importlib.import_module(full_name)
        assert mod is not None, f"Failed to import {full_name}"


def test_api_package_importable():
    import EulerApiSdk.api
    assert EulerApiSdk.api is not None


# ---------------------------------------------------------------------------
# 8. Models module imports
# ---------------------------------------------------------------------------

def test_models_package_importable():
    import EulerApiSdk.models
    assert EulerApiSdk.models is not None


def test_models_has_exports():
    from EulerApiSdk import models
    # Every model the generator exported (per the manifest) must be importable.
    for name in EXPECTED_MODELS:
        assert hasattr(models, name), f"models module missing export: {name}"


# ---------------------------------------------------------------------------
# 9. raise_on_unexpected_status default
# ---------------------------------------------------------------------------

def test_client_raise_on_unexpected_status_default():
    from EulerApiSdk import Client
    client = Client(base_url="https://example.com")
    assert client.raise_on_unexpected_status is False


def test_client_raise_on_unexpected_status_override():
    from EulerApiSdk import Client
    client = Client(base_url="https://example.com", raise_on_unexpected_status=True)
    assert client.raise_on_unexpected_status is True


# ---------------------------------------------------------------------------
# Run all tests
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    tests = [
        ("Import package-level exports", test_import_package),
        ("Import Client and AuthenticatedClient directly", test_import_client_directly),
        ("Instantiate Client with base_url", test_client_instantiation),
        ("Instantiate Client with headers and cookies", test_client_with_options),
        ("Instantiate AuthenticatedClient with token", test_authenticated_client_instantiation),
        ("AuthenticatedClient custom prefix and header name", test_authenticated_client_with_custom_prefix),
        ("Client has expected methods", test_client_has_expected_methods),
        ("AuthenticatedClient has expected methods", test_authenticated_client_has_expected_methods),
        ("with_headers returns Client instance", test_with_headers_returns_client),
        ("with_cookies returns Client instance", test_with_cookies_returns_client),
        ("with_timeout returns Client instance", test_with_timeout_returns_client),
        ("Client supports context manager", test_client_context_manager),
        ("AuthenticatedClient supports context manager", test_authenticated_client_context_manager),
        ("get_httpx_client returns httpx.Client", test_get_httpx_client),
        ("get_async_httpx_client returns httpx.AsyncClient", test_get_async_httpx_client),
        ("AuthenticatedClient sets auth header on httpx client", test_authenticated_get_httpx_client_sets_auth_header),
        ("All API modules are importable", test_api_modules_importable),
        ("API package is importable", test_api_package_importable),
        ("Models package is importable", test_models_package_importable),
        ("Models module has expected exports", test_models_has_exports),
        ("Client raise_on_unexpected_status defaults to False", test_client_raise_on_unexpected_status_default),
        ("Client raise_on_unexpected_status can be set to True", test_client_raise_on_unexpected_status_override),
    ]

    print(f"\nRunning {len(tests)} tests...\n")
    for name, fn in tests:
        run_test(name, fn)

    print(f"\n{passed} passed, {failed} failed, {passed + failed} total\n")

    if failed > 0:
        sys.exit(1)
    else:
        print("All tests passed.")

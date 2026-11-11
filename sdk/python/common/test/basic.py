"""
Basic tests shared by every Python SDK package.

Each package's test/test_basic.py puts its own folder on sys.path and calls
run_basic_tests with its import name, so the same checks run against
TikTokLiveApiSdk and TikTokApiSdk.

The API surface is determined dynamically at codegen time.
scripts/render_manifest.py scans the generated SDK (itself produced from the
OpenAPI spec) and writes test/sdk_manifest.json listing the generated API
modules and model exports. Reading it here keeps the tests in sync with the
spec automatically instead of hardcoding module/model names.
"""

import importlib
import json
import os

EXPECTED_CLIENT_METHODS = [
    "with_headers",
    "with_cookies",
    "with_timeout",
    "get_httpx_client",
    "get_async_httpx_client",
    "set_httpx_client",
    "set_async_httpx_client",
]


def load_manifest(manifest_path):
    if not os.path.isfile(manifest_path):
        raise SystemExit(
            f"Manifest not found at {manifest_path}. "
            "Run codegen (pnpm run generate) first."
        )
    with open(manifest_path, encoding="utf-8") as fh:
        manifest = json.load(fh)
    if not manifest.get("api_modules"):
        raise SystemExit(f"Manifest at {manifest_path} lists no API modules.")
    if not manifest.get("models"):
        raise SystemExit(f"Manifest at {manifest_path} lists no models.")
    return manifest


def run_basic_tests(package, manifest_path):
    """Run the shared basic tests against `package`; return the exit code."""
    manifest = load_manifest(manifest_path)
    api_modules = manifest["api_modules"]
    expected_models = manifest["models"]

    def sdk():
        return importlib.import_module(package)

    # -----------------------------------------------------------------------
    # 1. Package-level imports
    # -----------------------------------------------------------------------

    def test_import_package():
        module = sdk()
        assert hasattr(module, "Client"), f"{package} should export Client"
        assert hasattr(module, "AuthenticatedClient"), f"{package} should export AuthenticatedClient"

    def test_import_client_directly():
        client_module = importlib.import_module(f"{package}.client")
        assert client_module.Client is not None
        assert client_module.AuthenticatedClient is not None

    # -----------------------------------------------------------------------
    # 2. Client instantiation
    # -----------------------------------------------------------------------

    def test_client_instantiation():
        client = sdk().Client(base_url="https://example.com")
        assert client is not None

    def test_client_with_options():
        client = sdk().Client(
            base_url="https://example.com",
            headers={"X-Custom": "value"},
            cookies={"session": "abc"},
        )
        assert client is not None

    def test_authenticated_client_instantiation():
        client = sdk().AuthenticatedClient(base_url="https://example.com", token="test-token-123")
        assert client is not None

    def test_authenticated_client_with_custom_prefix():
        client = sdk().AuthenticatedClient(
            base_url="https://example.com",
            token="my-token",
            prefix="Token",
            auth_header_name="X-Auth",
        )
        assert client.token == "my-token"
        assert client.prefix == "Token"
        assert client.auth_header_name == "X-Auth"

    # -----------------------------------------------------------------------
    # 3. Client methods exist
    # -----------------------------------------------------------------------

    def test_client_has_expected_methods():
        client = sdk().Client(base_url="https://example.com")
        for method_name in EXPECTED_CLIENT_METHODS:
            assert hasattr(client, method_name), f"Client missing method: {method_name}"
            assert callable(getattr(client, method_name)), f"Client.{method_name} is not callable"

    def test_authenticated_client_has_expected_methods():
        client = sdk().AuthenticatedClient(base_url="https://example.com", token="tok")
        for method_name in EXPECTED_CLIENT_METHODS:
            assert hasattr(client, method_name), f"AuthenticatedClient missing method: {method_name}"
            assert callable(getattr(client, method_name)), f"AuthenticatedClient.{method_name} is not callable"

    # -----------------------------------------------------------------------
    # 4. Client builder methods return new instances
    # -----------------------------------------------------------------------

    def test_with_headers_returns_client():
        Client = sdk().Client
        client = Client(base_url="https://example.com")
        new_client = client.with_headers({"X-New": "header"})
        assert isinstance(new_client, Client)

    def test_with_cookies_returns_client():
        Client = sdk().Client
        client = Client(base_url="https://example.com")
        new_client = client.with_cookies({"new_cookie": "value"})
        assert isinstance(new_client, Client)

    def test_with_timeout_returns_client():
        import httpx
        Client = sdk().Client
        client = Client(base_url="https://example.com")
        new_client = client.with_timeout(httpx.Timeout(30.0))
        assert isinstance(new_client, Client)

    # -----------------------------------------------------------------------
    # 5. Context manager support
    # -----------------------------------------------------------------------

    def test_client_context_manager():
        client = sdk().Client(base_url="https://example.com")
        with client as c:
            assert c is client

    def test_authenticated_client_context_manager():
        client = sdk().AuthenticatedClient(base_url="https://example.com", token="tok")
        with client as c:
            assert c is client

    # -----------------------------------------------------------------------
    # 6. httpx client creation
    # -----------------------------------------------------------------------

    def test_get_httpx_client():
        import httpx
        client = sdk().Client(base_url="https://example.com")
        httpx_client = client.get_httpx_client()
        assert isinstance(httpx_client, httpx.Client)

    def test_get_async_httpx_client():
        import httpx
        client = sdk().Client(base_url="https://example.com")
        async_client = client.get_async_httpx_client()
        assert isinstance(async_client, httpx.AsyncClient)

    def test_authenticated_get_httpx_client_sets_auth_header():
        import httpx
        client = sdk().AuthenticatedClient(base_url="https://example.com", token="secret")
        httpx_client = client.get_httpx_client()
        assert isinstance(httpx_client, httpx.Client)
        # By default the Euler API authenticates with an X-Api-Key header carrying the
        # raw token (no "Bearer " prefix). Not an Authorization header.
        assert "Authorization" not in httpx_client.headers
        assert httpx_client.headers["X-Api-Key"] == "secret"

    # -----------------------------------------------------------------------
    # 7. API module imports
    # -----------------------------------------------------------------------

    def test_api_modules_importable():
        for module_name in api_modules:
            full_name = f"{package}.api.{module_name}"
            mod = importlib.import_module(full_name)
            assert mod is not None, f"Failed to import {full_name}"

    def test_api_package_importable():
        assert importlib.import_module(f"{package}.api") is not None

    # -----------------------------------------------------------------------
    # 8. Models module imports
    # -----------------------------------------------------------------------

    def test_models_package_importable():
        assert importlib.import_module(f"{package}.models") is not None

    def test_models_has_exports():
        models = importlib.import_module(f"{package}.models")
        # Every model the generator exported (per the manifest) must be importable.
        for name in expected_models:
            assert hasattr(models, name), f"models module missing export: {name}"

    # -----------------------------------------------------------------------
    # 9. raise_on_unexpected_status default
    # -----------------------------------------------------------------------

    def test_client_raise_on_unexpected_status_default():
        client = sdk().Client(base_url="https://example.com")
        assert client.raise_on_unexpected_status is False

    def test_client_raise_on_unexpected_status_override():
        client = sdk().Client(base_url="https://example.com", raise_on_unexpected_status=True)
        assert client.raise_on_unexpected_status is True

    # -----------------------------------------------------------------------
    # Run all tests
    # -----------------------------------------------------------------------

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

    passed = 0
    failed = 0

    print(f"\nRunning {len(tests)} tests against {package}...\n")
    for name, fn in tests:
        print(f"  {name} ... ", end="")
        try:
            fn()
            print("OK")
            passed += 1
        except Exception as exc:
            print(f"FAILED: {exc}")
            failed += 1

    print(f"\n{passed} passed, {failed} failed, {passed + failed} total\n")

    if failed > 0:
        return 1

    print("All tests passed.")
    return 0

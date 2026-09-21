from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.decrypt_tik_tok_x_gnarly_response_429 import DecryptTikTokXGnarlyResponse429
from ...models.decrypt_tik_tok_x_gnarly_response_500 import DecryptTikTokXGnarlyResponse500
from ...models.decrypt_x_gnarly_body import DecryptXGnarlyBody
from ...models.decrypt_x_gnarly_response import DecryptXGnarlyResponse
from ...models.x_gnarly_script_version import XGnarlyScriptVersion
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: DecryptXGnarlyBody,
    version: XGnarlyScriptVersion | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_version: str | Unset = UNSET
    if not isinstance(version, Unset):
        json_version = version.value

    params["version"] = json_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tiktok/signing/decrypt/x-gnarly",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DecryptTikTokXGnarlyResponse429 | DecryptTikTokXGnarlyResponse500 | DecryptXGnarlyResponse | None:
    if response.status_code == 200:
        response_200 = DecryptXGnarlyResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = DecryptTikTokXGnarlyResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = DecryptTikTokXGnarlyResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DecryptTikTokXGnarlyResponse429 | DecryptTikTokXGnarlyResponse500 | DecryptXGnarlyResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DecryptXGnarlyBody,
    version: XGnarlyScriptVersion | Unset = UNSET,
) -> Response[DecryptTikTokXGnarlyResponse429 | DecryptTikTokXGnarlyResponse500 | DecryptXGnarlyResponse]:
    """Decode a TikTok `x-gnarly` signature payload into its fields. Only the fields a captured token
    confirms are given names; the rest are returned under their index as `unknown_<index>` rather than
    guessed at.

    Args:
        version (XGnarlyScriptVersion | Unset):
        body (DecryptXGnarlyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DecryptTikTokXGnarlyResponse429 | DecryptTikTokXGnarlyResponse500 | DecryptXGnarlyResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: DecryptXGnarlyBody,
    version: XGnarlyScriptVersion | Unset = UNSET,
) -> DecryptTikTokXGnarlyResponse429 | DecryptTikTokXGnarlyResponse500 | DecryptXGnarlyResponse | None:
    """Decode a TikTok `x-gnarly` signature payload into its fields. Only the fields a captured token
    confirms are given names; the rest are returned under their index as `unknown_<index>` rather than
    guessed at.

    Args:
        version (XGnarlyScriptVersion | Unset):
        body (DecryptXGnarlyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DecryptTikTokXGnarlyResponse429 | DecryptTikTokXGnarlyResponse500 | DecryptXGnarlyResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DecryptXGnarlyBody,
    version: XGnarlyScriptVersion | Unset = UNSET,
) -> Response[DecryptTikTokXGnarlyResponse429 | DecryptTikTokXGnarlyResponse500 | DecryptXGnarlyResponse]:
    """Decode a TikTok `x-gnarly` signature payload into its fields. Only the fields a captured token
    confirms are given names; the rest are returned under their index as `unknown_<index>` rather than
    guessed at.

    Args:
        version (XGnarlyScriptVersion | Unset):
        body (DecryptXGnarlyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DecryptTikTokXGnarlyResponse429 | DecryptTikTokXGnarlyResponse500 | DecryptXGnarlyResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DecryptXGnarlyBody,
    version: XGnarlyScriptVersion | Unset = UNSET,
) -> DecryptTikTokXGnarlyResponse429 | DecryptTikTokXGnarlyResponse500 | DecryptXGnarlyResponse | None:
    """Decode a TikTok `x-gnarly` signature payload into its fields. Only the fields a captured token
    confirms are given names; the rest are returned under their index as `unknown_<index>` rather than
    guessed at.

    Args:
        version (XGnarlyScriptVersion | Unset):
        body (DecryptXGnarlyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DecryptTikTokXGnarlyResponse429 | DecryptTikTokXGnarlyResponse500 | DecryptXGnarlyResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            version=version,
        )
    ).parsed

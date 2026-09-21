from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.decrypt_tik_tok_x_dynosaur_response_429 import DecryptTikTokXDynosaurResponse429
from ...models.decrypt_tik_tok_x_dynosaur_response_500 import DecryptTikTokXDynosaurResponse500
from ...models.decrypt_x_dynosaur_body import DecryptXDynosaurBody
from ...models.decrypt_x_dynosaur_response import DecryptXDynosaurResponse
from ...models.x_dynosaur_script_version import XDynosaurScriptVersion
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: DecryptXDynosaurBody,
    version: XDynosaurScriptVersion | Unset = UNSET,
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
        "url": "/tiktok/signing/decrypt/x-dynosaur",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DecryptTikTokXDynosaurResponse429 | DecryptTikTokXDynosaurResponse500 | DecryptXDynosaurResponse | None:
    if response.status_code == 200:
        response_200 = DecryptXDynosaurResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = DecryptTikTokXDynosaurResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = DecryptTikTokXDynosaurResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DecryptTikTokXDynosaurResponse429 | DecryptTikTokXDynosaurResponse500 | DecryptXDynosaurResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DecryptXDynosaurBody,
    version: XDynosaurScriptVersion | Unset = UNSET,
) -> Response[DecryptTikTokXDynosaurResponse429 | DecryptTikTokXDynosaurResponse500 | DecryptXDynosaurResponse]:
    """Decode a TikTok `x-dynosaur` signature payload into its records. Unlike the other signing payloads
    its leading byte is a bit-field rather than a constant marker, so the sign type and mode are
    returned alongside the records.

    Args:
        version (XDynosaurScriptVersion | Unset):
        body (DecryptXDynosaurBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DecryptTikTokXDynosaurResponse429 | DecryptTikTokXDynosaurResponse500 | DecryptXDynosaurResponse]
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
    body: DecryptXDynosaurBody,
    version: XDynosaurScriptVersion | Unset = UNSET,
) -> DecryptTikTokXDynosaurResponse429 | DecryptTikTokXDynosaurResponse500 | DecryptXDynosaurResponse | None:
    """Decode a TikTok `x-dynosaur` signature payload into its records. Unlike the other signing payloads
    its leading byte is a bit-field rather than a constant marker, so the sign type and mode are
    returned alongside the records.

    Args:
        version (XDynosaurScriptVersion | Unset):
        body (DecryptXDynosaurBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DecryptTikTokXDynosaurResponse429 | DecryptTikTokXDynosaurResponse500 | DecryptXDynosaurResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DecryptXDynosaurBody,
    version: XDynosaurScriptVersion | Unset = UNSET,
) -> Response[DecryptTikTokXDynosaurResponse429 | DecryptTikTokXDynosaurResponse500 | DecryptXDynosaurResponse]:
    """Decode a TikTok `x-dynosaur` signature payload into its records. Unlike the other signing payloads
    its leading byte is a bit-field rather than a constant marker, so the sign type and mode are
    returned alongside the records.

    Args:
        version (XDynosaurScriptVersion | Unset):
        body (DecryptXDynosaurBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DecryptTikTokXDynosaurResponse429 | DecryptTikTokXDynosaurResponse500 | DecryptXDynosaurResponse]
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
    body: DecryptXDynosaurBody,
    version: XDynosaurScriptVersion | Unset = UNSET,
) -> DecryptTikTokXDynosaurResponse429 | DecryptTikTokXDynosaurResponse500 | DecryptXDynosaurResponse | None:
    """Decode a TikTok `x-dynosaur` signature payload into its records. Unlike the other signing payloads
    its leading byte is a bit-field rather than a constant marker, so the sign type and mode are
    returned alongside the records.

    Args:
        version (XDynosaurScriptVersion | Unset):
        body (DecryptXDynosaurBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DecryptTikTokXDynosaurResponse429 | DecryptTikTokXDynosaurResponse500 | DecryptXDynosaurResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            version=version,
        )
    ).parsed

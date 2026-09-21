from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.decrypt_str_data_body import DecryptStrDataBody
from ...models.decrypt_str_data_response import DecryptStrDataResponse
from ...models.decrypt_tik_tok_str_data_response_429 import DecryptTikTokStrDataResponse429
from ...models.decrypt_tik_tok_str_data_response_500 import DecryptTikTokStrDataResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: DecryptStrDataBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tiktok/signing/decrypt/str-data",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DecryptStrDataResponse | DecryptTikTokStrDataResponse429 | DecryptTikTokStrDataResponse500 | None:
    if response.status_code == 200:
        response_200 = DecryptStrDataResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = DecryptTikTokStrDataResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = DecryptTikTokStrDataResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DecryptStrDataResponse | DecryptTikTokStrDataResponse429 | DecryptTikTokStrDataResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DecryptStrDataBody,
) -> Response[DecryptStrDataResponse | DecryptTikTokStrDataResponse429 | DecryptTikTokStrDataResponse500]:
    """Decode a TikTok `str-data` payload into the behaviour telemetry object it encodes.

    Args:
        body (DecryptStrDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DecryptStrDataResponse | DecryptTikTokStrDataResponse429 | DecryptTikTokStrDataResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: DecryptStrDataBody,
) -> DecryptStrDataResponse | DecryptTikTokStrDataResponse429 | DecryptTikTokStrDataResponse500 | None:
    """Decode a TikTok `str-data` payload into the behaviour telemetry object it encodes.

    Args:
        body (DecryptStrDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DecryptStrDataResponse | DecryptTikTokStrDataResponse429 | DecryptTikTokStrDataResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DecryptStrDataBody,
) -> Response[DecryptStrDataResponse | DecryptTikTokStrDataResponse429 | DecryptTikTokStrDataResponse500]:
    """Decode a TikTok `str-data` payload into the behaviour telemetry object it encodes.

    Args:
        body (DecryptStrDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DecryptStrDataResponse | DecryptTikTokStrDataResponse429 | DecryptTikTokStrDataResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DecryptStrDataBody,
) -> DecryptStrDataResponse | DecryptTikTokStrDataResponse429 | DecryptTikTokStrDataResponse500 | None:
    """Decode a TikTok `str-data` payload into the behaviour telemetry object it encodes.

    Args:
        body (DecryptStrDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DecryptStrDataResponse | DecryptTikTokStrDataResponse429 | DecryptTikTokStrDataResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

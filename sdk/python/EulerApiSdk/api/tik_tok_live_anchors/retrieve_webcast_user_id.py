from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_webcast_user_id_response_429 import RetrieveWebcastUserIdResponse429
from ...models.retrieve_webcast_user_id_response_500 import RetrieveWebcastUserIdResponse500
from ...models.retrieve_webcast_user_id_response_503 import RetrieveWebcastUserIdResponse503
from ...models.webcast_user_id_response import WebcastUserIdResponse
from ...types import Response


def _get_kwargs(
    unique_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/anchors/{unique_id}/user_id".format(
            unique_id=quote(str(unique_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RetrieveWebcastUserIdResponse429
    | RetrieveWebcastUserIdResponse500
    | RetrieveWebcastUserIdResponse503
    | WebcastUserIdResponse
    | None
):
    if response.status_code == 200:
        response_200 = WebcastUserIdResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveWebcastUserIdResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveWebcastUserIdResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RetrieveWebcastUserIdResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RetrieveWebcastUserIdResponse429
    | RetrieveWebcastUserIdResponse500
    | RetrieveWebcastUserIdResponse503
    | WebcastUserIdResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    unique_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    RetrieveWebcastUserIdResponse429
    | RetrieveWebcastUserIdResponse500
    | RetrieveWebcastUserIdResponse503
    | WebcastUserIdResponse
]:
    """Resolve a TikTok @unique_id (handle) to its numeric TikTok user ID.

    Args:
        unique_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveWebcastUserIdResponse429 | RetrieveWebcastUserIdResponse500 | RetrieveWebcastUserIdResponse503 | WebcastUserIdResponse]
    """

    kwargs = _get_kwargs(
        unique_id=unique_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    unique_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    RetrieveWebcastUserIdResponse429
    | RetrieveWebcastUserIdResponse500
    | RetrieveWebcastUserIdResponse503
    | WebcastUserIdResponse
    | None
):
    """Resolve a TikTok @unique_id (handle) to its numeric TikTok user ID.

    Args:
        unique_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveWebcastUserIdResponse429 | RetrieveWebcastUserIdResponse500 | RetrieveWebcastUserIdResponse503 | WebcastUserIdResponse
    """

    return sync_detailed(
        unique_id=unique_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    unique_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    RetrieveWebcastUserIdResponse429
    | RetrieveWebcastUserIdResponse500
    | RetrieveWebcastUserIdResponse503
    | WebcastUserIdResponse
]:
    """Resolve a TikTok @unique_id (handle) to its numeric TikTok user ID.

    Args:
        unique_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveWebcastUserIdResponse429 | RetrieveWebcastUserIdResponse500 | RetrieveWebcastUserIdResponse503 | WebcastUserIdResponse]
    """

    kwargs = _get_kwargs(
        unique_id=unique_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    unique_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    RetrieveWebcastUserIdResponse429
    | RetrieveWebcastUserIdResponse500
    | RetrieveWebcastUserIdResponse503
    | WebcastUserIdResponse
    | None
):
    """Resolve a TikTok @unique_id (handle) to its numeric TikTok user ID.

    Args:
        unique_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveWebcastUserIdResponse429 | RetrieveWebcastUserIdResponse500 | RetrieveWebcastUserIdResponse503 | WebcastUserIdResponse
    """

    return (
        await asyncio_detailed(
            unique_id=unique_id,
            client=client,
        )
    ).parsed

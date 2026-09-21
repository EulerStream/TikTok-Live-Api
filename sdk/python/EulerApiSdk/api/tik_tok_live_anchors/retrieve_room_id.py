from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_room_id_response_429 import RetrieveRoomIdResponse429
from ...models.retrieve_room_id_response_500 import RetrieveRoomIdResponse500
from ...models.retrieve_room_id_response_503 import RetrieveRoomIdResponse503
from ...models.webcast_room_id_route_response import WebcastRoomIdRouteResponse
from ...types import Response


def _get_kwargs(
    unique_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/anchors/{unique_id}/room_id".format(
            unique_id=quote(str(unique_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RetrieveRoomIdResponse429
    | RetrieveRoomIdResponse500
    | RetrieveRoomIdResponse503
    | WebcastRoomIdRouteResponse
    | None
):
    if response.status_code == 200:
        response_200 = WebcastRoomIdRouteResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveRoomIdResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveRoomIdResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RetrieveRoomIdResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RetrieveRoomIdResponse429 | RetrieveRoomIdResponse500 | RetrieveRoomIdResponse503 | WebcastRoomIdRouteResponse
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
    RetrieveRoomIdResponse429 | RetrieveRoomIdResponse500 | RetrieveRoomIdResponse503 | WebcastRoomIdRouteResponse
]:
    """Fetch Room ID for a given uniqueId & whether that user is live.

    Args:
        unique_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveRoomIdResponse429 | RetrieveRoomIdResponse500 | RetrieveRoomIdResponse503 | WebcastRoomIdRouteResponse]
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
    RetrieveRoomIdResponse429
    | RetrieveRoomIdResponse500
    | RetrieveRoomIdResponse503
    | WebcastRoomIdRouteResponse
    | None
):
    """Fetch Room ID for a given uniqueId & whether that user is live.

    Args:
        unique_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveRoomIdResponse429 | RetrieveRoomIdResponse500 | RetrieveRoomIdResponse503 | WebcastRoomIdRouteResponse
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
    RetrieveRoomIdResponse429 | RetrieveRoomIdResponse500 | RetrieveRoomIdResponse503 | WebcastRoomIdRouteResponse
]:
    """Fetch Room ID for a given uniqueId & whether that user is live.

    Args:
        unique_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveRoomIdResponse429 | RetrieveRoomIdResponse500 | RetrieveRoomIdResponse503 | WebcastRoomIdRouteResponse]
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
    RetrieveRoomIdResponse429
    | RetrieveRoomIdResponse500
    | RetrieveRoomIdResponse503
    | WebcastRoomIdRouteResponse
    | None
):
    """Fetch Room ID for a given uniqueId & whether that user is live.

    Args:
        unique_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveRoomIdResponse429 | RetrieveRoomIdResponse500 | RetrieveRoomIdResponse503 | WebcastRoomIdRouteResponse
    """

    return (
        await asyncio_detailed(
            unique_id=unique_id,
            client=client,
        )
    ).parsed

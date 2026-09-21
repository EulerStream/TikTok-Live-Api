from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_room_gifts_response_429 import RetrieveRoomGiftsResponse429
from ...models.retrieve_room_gifts_response_500 import RetrieveRoomGiftsResponse500
from ...models.retrieve_room_gifts_response_503 import RetrieveRoomGiftsResponse503
from ...models.room_gifts_response import RoomGiftsResponse
from ...models.webcast_language import WebcastLanguage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    room_id: str,
    *,
    webcast_language: WebcastLanguage | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_webcast_language: str | Unset = UNSET
    if not isinstance(webcast_language, Unset):
        json_webcast_language = webcast_language.value

    params["webcast_language"] = json_webcast_language

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/rooms/{room_id}/gifts".format(
            room_id=quote(str(room_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RetrieveRoomGiftsResponse429
    | RetrieveRoomGiftsResponse500
    | RetrieveRoomGiftsResponse503
    | RoomGiftsResponse
    | None
):
    if response.status_code == 200:
        response_200 = RoomGiftsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveRoomGiftsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveRoomGiftsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RetrieveRoomGiftsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RetrieveRoomGiftsResponse429 | RetrieveRoomGiftsResponse500 | RetrieveRoomGiftsResponse503 | RoomGiftsResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    room_id: str,
    *,
    client: AuthenticatedClient,
    webcast_language: WebcastLanguage | Unset = UNSET,
) -> Response[
    RetrieveRoomGiftsResponse429 | RetrieveRoomGiftsResponse500 | RetrieveRoomGiftsResponse503 | RoomGiftsResponse
]:
    """Retrieve room-specific TikTok LIVE gift data.

    Returns the ordered gift list for a specific room, along with room-specific
    overrides (sponsor info, gallery status, panel visibility). Use this alongside
    the /webcast/gift_info endpoint which provides the full gift catalog.

    Args:
        room_id (str):
        webcast_language (WebcastLanguage | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveRoomGiftsResponse429 | RetrieveRoomGiftsResponse500 | RetrieveRoomGiftsResponse503 | RoomGiftsResponse]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        webcast_language=webcast_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    room_id: str,
    *,
    client: AuthenticatedClient,
    webcast_language: WebcastLanguage | Unset = UNSET,
) -> (
    RetrieveRoomGiftsResponse429
    | RetrieveRoomGiftsResponse500
    | RetrieveRoomGiftsResponse503
    | RoomGiftsResponse
    | None
):
    """Retrieve room-specific TikTok LIVE gift data.

    Returns the ordered gift list for a specific room, along with room-specific
    overrides (sponsor info, gallery status, panel visibility). Use this alongside
    the /webcast/gift_info endpoint which provides the full gift catalog.

    Args:
        room_id (str):
        webcast_language (WebcastLanguage | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveRoomGiftsResponse429 | RetrieveRoomGiftsResponse500 | RetrieveRoomGiftsResponse503 | RoomGiftsResponse
    """

    return sync_detailed(
        room_id=room_id,
        client=client,
        webcast_language=webcast_language,
    ).parsed


async def asyncio_detailed(
    room_id: str,
    *,
    client: AuthenticatedClient,
    webcast_language: WebcastLanguage | Unset = UNSET,
) -> Response[
    RetrieveRoomGiftsResponse429 | RetrieveRoomGiftsResponse500 | RetrieveRoomGiftsResponse503 | RoomGiftsResponse
]:
    """Retrieve room-specific TikTok LIVE gift data.

    Returns the ordered gift list for a specific room, along with room-specific
    overrides (sponsor info, gallery status, panel visibility). Use this alongside
    the /webcast/gift_info endpoint which provides the full gift catalog.

    Args:
        room_id (str):
        webcast_language (WebcastLanguage | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveRoomGiftsResponse429 | RetrieveRoomGiftsResponse500 | RetrieveRoomGiftsResponse503 | RoomGiftsResponse]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        webcast_language=webcast_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    room_id: str,
    *,
    client: AuthenticatedClient,
    webcast_language: WebcastLanguage | Unset = UNSET,
) -> (
    RetrieveRoomGiftsResponse429
    | RetrieveRoomGiftsResponse500
    | RetrieveRoomGiftsResponse503
    | RoomGiftsResponse
    | None
):
    """Retrieve room-specific TikTok LIVE gift data.

    Returns the ordered gift list for a specific room, along with room-specific
    overrides (sponsor info, gallery status, panel visibility). Use this alongside
    the /webcast/gift_info endpoint which provides the full gift catalog.

    Args:
        room_id (str):
        webcast_language (WebcastLanguage | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveRoomGiftsResponse429 | RetrieveRoomGiftsResponse500 | RetrieveRoomGiftsResponse503 | RoomGiftsResponse
    """

    return (
        await asyncio_detailed(
            room_id=room_id,
            client=client,
            webcast_language=webcast_language,
        )
    ).parsed

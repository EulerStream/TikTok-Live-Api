from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.kick_room_user_response_429 import KickRoomUserResponse429
from ...models.kick_room_user_response_500 import KickRoomUserResponse500
from ...models.kick_room_user_response_503 import KickRoomUserResponse503
from ...models.room_kick_user_api_response import RoomKickUserAPIResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    room_id: str,
    *,
    tiktok_user_id: str,
    comment_msg_id: str | Unset = UNSET,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_oauth_token, Unset):
        headers["x-oauth-token"] = x_oauth_token

    if not isinstance(x_cookie_header, Unset):
        headers["x-cookie-header"] = x_cookie_header

    params: dict[str, Any] = {}

    params["tiktok_user_id"] = tiktok_user_id

    params["comment_msg_id"] = comment_msg_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/webcast/rooms/{room_id}/moderation/bans".format(
            room_id=quote(str(room_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> KickRoomUserResponse429 | KickRoomUserResponse500 | KickRoomUserResponse503 | RoomKickUserAPIResponse | None:
    if response.status_code == 200:
        response_200 = RoomKickUserAPIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = KickRoomUserResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = KickRoomUserResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = KickRoomUserResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[KickRoomUserResponse429 | KickRoomUserResponse500 | KickRoomUserResponse503 | RoomKickUserAPIResponse]:
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
    tiktok_user_id: str,
    comment_msg_id: str | Unset = UNSET,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Response[KickRoomUserResponse429 | KickRoomUserResponse500 | KickRoomUserResponse503 | RoomKickUserAPIResponse]:
    """Kick a user from a livestream room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        tiktok_user_id (str):
        comment_msg_id (str | Unset):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KickRoomUserResponse429 | KickRoomUserResponse500 | KickRoomUserResponse503 | RoomKickUserAPIResponse]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        tiktok_user_id=tiktok_user_id,
        comment_msg_id=comment_msg_id,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    room_id: str,
    *,
    client: AuthenticatedClient,
    tiktok_user_id: str,
    comment_msg_id: str | Unset = UNSET,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> KickRoomUserResponse429 | KickRoomUserResponse500 | KickRoomUserResponse503 | RoomKickUserAPIResponse | None:
    """Kick a user from a livestream room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        tiktok_user_id (str):
        comment_msg_id (str | Unset):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KickRoomUserResponse429 | KickRoomUserResponse500 | KickRoomUserResponse503 | RoomKickUserAPIResponse
    """

    return sync_detailed(
        room_id=room_id,
        client=client,
        tiktok_user_id=tiktok_user_id,
        comment_msg_id=comment_msg_id,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    ).parsed


async def asyncio_detailed(
    room_id: str,
    *,
    client: AuthenticatedClient,
    tiktok_user_id: str,
    comment_msg_id: str | Unset = UNSET,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Response[KickRoomUserResponse429 | KickRoomUserResponse500 | KickRoomUserResponse503 | RoomKickUserAPIResponse]:
    """Kick a user from a livestream room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        tiktok_user_id (str):
        comment_msg_id (str | Unset):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KickRoomUserResponse429 | KickRoomUserResponse500 | KickRoomUserResponse503 | RoomKickUserAPIResponse]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        tiktok_user_id=tiktok_user_id,
        comment_msg_id=comment_msg_id,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    room_id: str,
    *,
    client: AuthenticatedClient,
    tiktok_user_id: str,
    comment_msg_id: str | Unset = UNSET,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> KickRoomUserResponse429 | KickRoomUserResponse500 | KickRoomUserResponse503 | RoomKickUserAPIResponse | None:
    """Kick a user from a livestream room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        tiktok_user_id (str):
        comment_msg_id (str | Unset):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KickRoomUserResponse429 | KickRoomUserResponse500 | KickRoomUserResponse503 | RoomKickUserAPIResponse
    """

    return (
        await asyncio_detailed(
            room_id=room_id,
            client=client,
            tiktok_user_id=tiktok_user_id,
            comment_msg_id=comment_msg_id,
            x_oauth_token=x_oauth_token,
            x_cookie_header=x_cookie_header,
        )
    ).parsed

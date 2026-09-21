from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.room_unmute_user_api_response import RoomUnmuteUserAPIResponse
from ...models.unmute_room_user_response_429 import UnmuteRoomUserResponse429
from ...models.unmute_room_user_response_500 import UnmuteRoomUserResponse500
from ...models.unmute_room_user_response_503 import UnmuteRoomUserResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    room_id: str,
    *,
    user_id: str,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_oauth_token, Unset):
        headers["x-oauth-token"] = x_oauth_token

    if not isinstance(x_cookie_header, Unset):
        headers["x-cookie-header"] = x_cookie_header

    params: dict[str, Any] = {}

    params["user_id"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/webcast/rooms/{room_id}/moderation/mutes".format(
            room_id=quote(str(room_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RoomUnmuteUserAPIResponse | UnmuteRoomUserResponse429 | UnmuteRoomUserResponse500 | UnmuteRoomUserResponse503 | None
):
    if response.status_code == 200:
        response_200 = RoomUnmuteUserAPIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = UnmuteRoomUserResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = UnmuteRoomUserResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = UnmuteRoomUserResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RoomUnmuteUserAPIResponse | UnmuteRoomUserResponse429 | UnmuteRoomUserResponse500 | UnmuteRoomUserResponse503
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
    user_id: str,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Response[
    RoomUnmuteUserAPIResponse | UnmuteRoomUserResponse429 | UnmuteRoomUserResponse500 | UnmuteRoomUserResponse503
]:
    """Unmute a user in a livestream room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        user_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RoomUnmuteUserAPIResponse | UnmuteRoomUserResponse429 | UnmuteRoomUserResponse500 | UnmuteRoomUserResponse503]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        user_id=user_id,
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
    user_id: str,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> (
    RoomUnmuteUserAPIResponse | UnmuteRoomUserResponse429 | UnmuteRoomUserResponse500 | UnmuteRoomUserResponse503 | None
):
    """Unmute a user in a livestream room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        user_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RoomUnmuteUserAPIResponse | UnmuteRoomUserResponse429 | UnmuteRoomUserResponse500 | UnmuteRoomUserResponse503
    """

    return sync_detailed(
        room_id=room_id,
        client=client,
        user_id=user_id,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    ).parsed


async def asyncio_detailed(
    room_id: str,
    *,
    client: AuthenticatedClient,
    user_id: str,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Response[
    RoomUnmuteUserAPIResponse | UnmuteRoomUserResponse429 | UnmuteRoomUserResponse500 | UnmuteRoomUserResponse503
]:
    """Unmute a user in a livestream room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        user_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RoomUnmuteUserAPIResponse | UnmuteRoomUserResponse429 | UnmuteRoomUserResponse500 | UnmuteRoomUserResponse503]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        user_id=user_id,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    room_id: str,
    *,
    client: AuthenticatedClient,
    user_id: str,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> (
    RoomUnmuteUserAPIResponse | UnmuteRoomUserResponse429 | UnmuteRoomUserResponse500 | UnmuteRoomUserResponse503 | None
):
    """Unmute a user in a livestream room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        user_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RoomUnmuteUserAPIResponse | UnmuteRoomUserResponse429 | UnmuteRoomUserResponse500 | UnmuteRoomUserResponse503
    """

    return (
        await asyncio_detailed(
            room_id=room_id,
            client=client,
            user_id=user_id,
            x_oauth_token=x_oauth_token,
            x_cookie_header=x_cookie_header,
        )
    ).parsed

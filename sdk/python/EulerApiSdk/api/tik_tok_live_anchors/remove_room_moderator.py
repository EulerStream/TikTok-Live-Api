from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_room_moderator_response_429 import RemoveRoomModeratorResponse429
from ...models.remove_room_moderator_response_500 import RemoveRoomModeratorResponse500
from ...models.remove_room_moderator_response_503 import RemoveRoomModeratorResponse503
from ...models.room_admin_update_api_response import RoomAdminUpdateAPIResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    anchor_id: str,
    *,
    to_user_id: str,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_oauth_token, Unset):
        headers["x-oauth-token"] = x_oauth_token

    if not isinstance(x_cookie_header, Unset):
        headers["x-cookie-header"] = x_cookie_header

    params: dict[str, Any] = {}

    params["to_user_id"] = to_user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/webcast/anchors/{anchor_id}/moderation/moderators".format(
            anchor_id=quote(str(anchor_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RemoveRoomModeratorResponse429
    | RemoveRoomModeratorResponse500
    | RemoveRoomModeratorResponse503
    | RoomAdminUpdateAPIResponse
    | None
):
    if response.status_code == 200:
        response_200 = RoomAdminUpdateAPIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RemoveRoomModeratorResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RemoveRoomModeratorResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RemoveRoomModeratorResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RemoveRoomModeratorResponse429
    | RemoveRoomModeratorResponse500
    | RemoveRoomModeratorResponse503
    | RoomAdminUpdateAPIResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    anchor_id: str,
    *,
    client: AuthenticatedClient,
    to_user_id: str,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Response[
    RemoveRoomModeratorResponse429
    | RemoveRoomModeratorResponse500
    | RemoveRoomModeratorResponse503
    | RoomAdminUpdateAPIResponse
]:
    """Remove a moderator from a livestream room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        anchor_id (str):
        to_user_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveRoomModeratorResponse429 | RemoveRoomModeratorResponse500 | RemoveRoomModeratorResponse503 | RoomAdminUpdateAPIResponse]
    """

    kwargs = _get_kwargs(
        anchor_id=anchor_id,
        to_user_id=to_user_id,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    anchor_id: str,
    *,
    client: AuthenticatedClient,
    to_user_id: str,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> (
    RemoveRoomModeratorResponse429
    | RemoveRoomModeratorResponse500
    | RemoveRoomModeratorResponse503
    | RoomAdminUpdateAPIResponse
    | None
):
    """Remove a moderator from a livestream room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        anchor_id (str):
        to_user_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveRoomModeratorResponse429 | RemoveRoomModeratorResponse500 | RemoveRoomModeratorResponse503 | RoomAdminUpdateAPIResponse
    """

    return sync_detailed(
        anchor_id=anchor_id,
        client=client,
        to_user_id=to_user_id,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    ).parsed


async def asyncio_detailed(
    anchor_id: str,
    *,
    client: AuthenticatedClient,
    to_user_id: str,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Response[
    RemoveRoomModeratorResponse429
    | RemoveRoomModeratorResponse500
    | RemoveRoomModeratorResponse503
    | RoomAdminUpdateAPIResponse
]:
    """Remove a moderator from a livestream room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        anchor_id (str):
        to_user_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveRoomModeratorResponse429 | RemoveRoomModeratorResponse500 | RemoveRoomModeratorResponse503 | RoomAdminUpdateAPIResponse]
    """

    kwargs = _get_kwargs(
        anchor_id=anchor_id,
        to_user_id=to_user_id,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    anchor_id: str,
    *,
    client: AuthenticatedClient,
    to_user_id: str,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> (
    RemoveRoomModeratorResponse429
    | RemoveRoomModeratorResponse500
    | RemoveRoomModeratorResponse503
    | RoomAdminUpdateAPIResponse
    | None
):
    """Remove a moderator from a livestream room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        anchor_id (str):
        to_user_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveRoomModeratorResponse429 | RemoveRoomModeratorResponse500 | RemoveRoomModeratorResponse503 | RoomAdminUpdateAPIResponse
    """

    return (
        await asyncio_detailed(
            anchor_id=anchor_id,
            client=client,
            to_user_id=to_user_id,
            x_oauth_token=x_oauth_token,
            x_cookie_header=x_cookie_header,
        )
    ).parsed

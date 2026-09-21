from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_room_muted_users_response_429 import RetrieveRoomMutedUsersResponse429
from ...models.retrieve_room_muted_users_response_500 import RetrieveRoomMutedUsersResponse500
from ...models.retrieve_room_muted_users_response_503 import RetrieveRoomMutedUsersResponse503
from ...models.room_muted_users_api_response import RoomMutedUsersAPIResponse
from ...models.route_image_source import RouteImageSource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    room_id: str,
    *,
    page: float | Unset = 0.0,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_oauth_token, Unset):
        headers["x-oauth-token"] = x_oauth_token

    if not isinstance(x_cookie_header, Unset):
        headers["x-cookie-header"] = x_cookie_header

    if not isinstance(x_image_source, Unset):
        headers["x-image-source"] = str(x_image_source)

    params: dict[str, Any] = {}

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
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
    RetrieveRoomMutedUsersResponse429
    | RetrieveRoomMutedUsersResponse500
    | RetrieveRoomMutedUsersResponse503
    | RoomMutedUsersAPIResponse
    | None
):
    if response.status_code == 200:
        response_200 = RoomMutedUsersAPIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveRoomMutedUsersResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveRoomMutedUsersResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RetrieveRoomMutedUsersResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RetrieveRoomMutedUsersResponse429
    | RetrieveRoomMutedUsersResponse500
    | RetrieveRoomMutedUsersResponse503
    | RoomMutedUsersAPIResponse
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
    page: float | Unset = 0.0,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[
    RetrieveRoomMutedUsersResponse429
    | RetrieveRoomMutedUsersResponse500
    | RetrieveRoomMutedUsersResponse503
    | RoomMutedUsersAPIResponse
]:
    """Retrieve the list of muted users in a livestream room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        page (float | Unset):  Default: 0.0.
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveRoomMutedUsersResponse429 | RetrieveRoomMutedUsersResponse500 | RetrieveRoomMutedUsersResponse503 | RoomMutedUsersAPIResponse]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        page=page,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
        x_image_source=x_image_source,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    room_id: str,
    *,
    client: AuthenticatedClient,
    page: float | Unset = 0.0,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> (
    RetrieveRoomMutedUsersResponse429
    | RetrieveRoomMutedUsersResponse500
    | RetrieveRoomMutedUsersResponse503
    | RoomMutedUsersAPIResponse
    | None
):
    """Retrieve the list of muted users in a livestream room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        page (float | Unset):  Default: 0.0.
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveRoomMutedUsersResponse429 | RetrieveRoomMutedUsersResponse500 | RetrieveRoomMutedUsersResponse503 | RoomMutedUsersAPIResponse
    """

    return sync_detailed(
        room_id=room_id,
        client=client,
        page=page,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
        x_image_source=x_image_source,
    ).parsed


async def asyncio_detailed(
    room_id: str,
    *,
    client: AuthenticatedClient,
    page: float | Unset = 0.0,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[
    RetrieveRoomMutedUsersResponse429
    | RetrieveRoomMutedUsersResponse500
    | RetrieveRoomMutedUsersResponse503
    | RoomMutedUsersAPIResponse
]:
    """Retrieve the list of muted users in a livestream room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        page (float | Unset):  Default: 0.0.
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveRoomMutedUsersResponse429 | RetrieveRoomMutedUsersResponse500 | RetrieveRoomMutedUsersResponse503 | RoomMutedUsersAPIResponse]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        page=page,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
        x_image_source=x_image_source,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    room_id: str,
    *,
    client: AuthenticatedClient,
    page: float | Unset = 0.0,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> (
    RetrieveRoomMutedUsersResponse429
    | RetrieveRoomMutedUsersResponse500
    | RetrieveRoomMutedUsersResponse503
    | RoomMutedUsersAPIResponse
    | None
):
    """Retrieve the list of muted users in a livestream room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        page (float | Unset):  Default: 0.0.
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveRoomMutedUsersResponse429 | RetrieveRoomMutedUsersResponse500 | RetrieveRoomMutedUsersResponse503 | RoomMutedUsersAPIResponse
    """

    return (
        await asyncio_detailed(
            room_id=room_id,
            client=client,
            page=page,
            x_oauth_token=x_oauth_token,
            x_cookie_header=x_cookie_header,
            x_image_source=x_image_source,
        )
    ).parsed

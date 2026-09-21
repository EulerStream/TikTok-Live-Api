from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_room_moderators_response_429 import RetrieveRoomModeratorsResponse429
from ...models.retrieve_room_moderators_response_500 import RetrieveRoomModeratorsResponse500
from ...models.retrieve_room_moderators_response_503 import RetrieveRoomModeratorsResponse503
from ...models.room_moderators_api_response import RoomModeratorsAPIResponse
from ...models.route_image_source import RouteImageSource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    anchor_id: str,
    *,
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

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/anchors/{anchor_id}/moderation/moderators".format(
            anchor_id=quote(str(anchor_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RetrieveRoomModeratorsResponse429
    | RetrieveRoomModeratorsResponse500
    | RetrieveRoomModeratorsResponse503
    | RoomModeratorsAPIResponse
    | None
):
    if response.status_code == 200:
        response_200 = RoomModeratorsAPIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveRoomModeratorsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveRoomModeratorsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RetrieveRoomModeratorsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RetrieveRoomModeratorsResponse429
    | RetrieveRoomModeratorsResponse500
    | RetrieveRoomModeratorsResponse503
    | RoomModeratorsAPIResponse
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
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[
    RetrieveRoomModeratorsResponse429
    | RetrieveRoomModeratorsResponse500
    | RetrieveRoomModeratorsResponse503
    | RoomModeratorsAPIResponse
]:
    """Retrieve the list of moderators in a livestream room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        anchor_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveRoomModeratorsResponse429 | RetrieveRoomModeratorsResponse500 | RetrieveRoomModeratorsResponse503 | RoomModeratorsAPIResponse]
    """

    kwargs = _get_kwargs(
        anchor_id=anchor_id,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
        x_image_source=x_image_source,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    anchor_id: str,
    *,
    client: AuthenticatedClient,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> (
    RetrieveRoomModeratorsResponse429
    | RetrieveRoomModeratorsResponse500
    | RetrieveRoomModeratorsResponse503
    | RoomModeratorsAPIResponse
    | None
):
    """Retrieve the list of moderators in a livestream room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        anchor_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveRoomModeratorsResponse429 | RetrieveRoomModeratorsResponse500 | RetrieveRoomModeratorsResponse503 | RoomModeratorsAPIResponse
    """

    return sync_detailed(
        anchor_id=anchor_id,
        client=client,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
        x_image_source=x_image_source,
    ).parsed


async def asyncio_detailed(
    anchor_id: str,
    *,
    client: AuthenticatedClient,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[
    RetrieveRoomModeratorsResponse429
    | RetrieveRoomModeratorsResponse500
    | RetrieveRoomModeratorsResponse503
    | RoomModeratorsAPIResponse
]:
    """Retrieve the list of moderators in a livestream room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        anchor_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveRoomModeratorsResponse429 | RetrieveRoomModeratorsResponse500 | RetrieveRoomModeratorsResponse503 | RoomModeratorsAPIResponse]
    """

    kwargs = _get_kwargs(
        anchor_id=anchor_id,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
        x_image_source=x_image_source,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    anchor_id: str,
    *,
    client: AuthenticatedClient,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> (
    RetrieveRoomModeratorsResponse429
    | RetrieveRoomModeratorsResponse500
    | RetrieveRoomModeratorsResponse503
    | RoomModeratorsAPIResponse
    | None
):
    """Retrieve the list of moderators in a livestream room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        anchor_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveRoomModeratorsResponse429 | RetrieveRoomModeratorsResponse500 | RetrieveRoomModeratorsResponse503 | RoomModeratorsAPIResponse
    """

    return (
        await asyncio_detailed(
            anchor_id=anchor_id,
            client=client,
            x_oauth_token=x_oauth_token,
            x_cookie_header=x_cookie_header,
            x_image_source=x_image_source,
        )
    ).parsed

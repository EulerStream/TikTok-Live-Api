from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.live_analytics_video_list_api_response import LiveAnalyticsVideoListAPIResponse
from ...models.retrieve_live_analytics_video_list_response_429 import RetrieveLiveAnalyticsVideoListResponse429
from ...models.retrieve_live_analytics_video_list_response_500 import RetrieveLiveAnalyticsVideoListResponse500
from ...models.retrieve_live_analytics_video_list_response_503 import RetrieveLiveAnalyticsVideoListResponse503
from ...models.route_image_source import RouteImageSource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    count: float | Unset = 10.0,
    offset: float | Unset = 0.0,
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

    params["count"] = count

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/anchors/me/rooms",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    LiveAnalyticsVideoListAPIResponse
    | RetrieveLiveAnalyticsVideoListResponse429
    | RetrieveLiveAnalyticsVideoListResponse500
    | RetrieveLiveAnalyticsVideoListResponse503
    | None
):
    if response.status_code == 200:
        response_200 = LiveAnalyticsVideoListAPIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveLiveAnalyticsVideoListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveLiveAnalyticsVideoListResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RetrieveLiveAnalyticsVideoListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    LiveAnalyticsVideoListAPIResponse
    | RetrieveLiveAnalyticsVideoListResponse429
    | RetrieveLiveAnalyticsVideoListResponse500
    | RetrieveLiveAnalyticsVideoListResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    count: float | Unset = 10.0,
    offset: float | Unset = 0.0,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[
    LiveAnalyticsVideoListAPIResponse
    | RetrieveLiveAnalyticsVideoListResponse429
    | RetrieveLiveAnalyticsVideoListResponse500
    | RetrieveLiveAnalyticsVideoListResponse503
]:
    """Retrieve the list of past livestreams with analytics for the authenticated user.

    **Note:** The session you attach must own the livestream to check analytics for a given `room_id`.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        count (float | Unset):  Default: 10.0.
        offset (float | Unset):  Default: 0.0.
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiveAnalyticsVideoListAPIResponse | RetrieveLiveAnalyticsVideoListResponse429 | RetrieveLiveAnalyticsVideoListResponse500 | RetrieveLiveAnalyticsVideoListResponse503]
    """

    kwargs = _get_kwargs(
        count=count,
        offset=offset,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
        x_image_source=x_image_source,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    count: float | Unset = 10.0,
    offset: float | Unset = 0.0,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> (
    LiveAnalyticsVideoListAPIResponse
    | RetrieveLiveAnalyticsVideoListResponse429
    | RetrieveLiveAnalyticsVideoListResponse500
    | RetrieveLiveAnalyticsVideoListResponse503
    | None
):
    """Retrieve the list of past livestreams with analytics for the authenticated user.

    **Note:** The session you attach must own the livestream to check analytics for a given `room_id`.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        count (float | Unset):  Default: 10.0.
        offset (float | Unset):  Default: 0.0.
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiveAnalyticsVideoListAPIResponse | RetrieveLiveAnalyticsVideoListResponse429 | RetrieveLiveAnalyticsVideoListResponse500 | RetrieveLiveAnalyticsVideoListResponse503
    """

    return sync_detailed(
        client=client,
        count=count,
        offset=offset,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
        x_image_source=x_image_source,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    count: float | Unset = 10.0,
    offset: float | Unset = 0.0,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[
    LiveAnalyticsVideoListAPIResponse
    | RetrieveLiveAnalyticsVideoListResponse429
    | RetrieveLiveAnalyticsVideoListResponse500
    | RetrieveLiveAnalyticsVideoListResponse503
]:
    """Retrieve the list of past livestreams with analytics for the authenticated user.

    **Note:** The session you attach must own the livestream to check analytics for a given `room_id`.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        count (float | Unset):  Default: 10.0.
        offset (float | Unset):  Default: 0.0.
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiveAnalyticsVideoListAPIResponse | RetrieveLiveAnalyticsVideoListResponse429 | RetrieveLiveAnalyticsVideoListResponse500 | RetrieveLiveAnalyticsVideoListResponse503]
    """

    kwargs = _get_kwargs(
        count=count,
        offset=offset,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
        x_image_source=x_image_source,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    count: float | Unset = 10.0,
    offset: float | Unset = 0.0,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> (
    LiveAnalyticsVideoListAPIResponse
    | RetrieveLiveAnalyticsVideoListResponse429
    | RetrieveLiveAnalyticsVideoListResponse500
    | RetrieveLiveAnalyticsVideoListResponse503
    | None
):
    """Retrieve the list of past livestreams with analytics for the authenticated user.

    **Note:** The session you attach must own the livestream to check analytics for a given `room_id`.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        count (float | Unset):  Default: 10.0.
        offset (float | Unset):  Default: 0.0.
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiveAnalyticsVideoListAPIResponse | RetrieveLiveAnalyticsVideoListResponse429 | RetrieveLiveAnalyticsVideoListResponse500 | RetrieveLiveAnalyticsVideoListResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            count=count,
            offset=offset,
            x_oauth_token=x_oauth_token,
            x_cookie_header=x_cookie_header,
            x_image_source=x_image_source,
        )
    ).parsed

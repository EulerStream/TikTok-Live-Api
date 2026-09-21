from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fetch_webcast_url_response_429 import FetchWebcastURLResponse429
from ...models.fetch_webcast_url_response_500 import FetchWebcastURLResponse500
from ...models.fetch_webcast_url_response_503 import FetchWebcastURLResponse503
from ...models.webcast_fetch_platform import WebcastFetchPlatform
from ...types import UNSET, Response, Unset


def _get_kwargs(
    room_id: str,
    *,
    client_query: str | Unset = "ttlive-other",
    cursor: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    client_enter: bool | Unset = True,
    platform: WebcastFetchPlatform | Unset = UNSET,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_oauth_token, Unset):
        headers["x-oauth-token"] = x_oauth_token

    if not isinstance(x_cookie_header, Unset):
        headers["x-cookie-header"] = x_cookie_header

    params: dict[str, Any] = {}

    params["client"] = client_query

    params["cursor"] = cursor

    params["user_agent"] = user_agent

    params["client_enter"] = client_enter

    json_platform: str | Unset = UNSET
    if not isinstance(platform, Unset):
        json_platform = platform.value

    params["platform"] = json_platform

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/rooms/{room_id}/connect".format(
            room_id=quote(str(room_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FetchWebcastURLResponse429 | FetchWebcastURLResponse500 | FetchWebcastURLResponse503 | None:
    if response.status_code == 429:
        response_429 = FetchWebcastURLResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = FetchWebcastURLResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = FetchWebcastURLResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FetchWebcastURLResponse429 | FetchWebcastURLResponse500 | FetchWebcastURLResponse503]:
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
    client_query: str | Unset = "ttlive-other",
    cursor: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    client_enter: bool | Unset = True,
    platform: WebcastFetchPlatform | Unset = UNSET,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Response[FetchWebcastURLResponse429 | FetchWebcastURLResponse500 | FetchWebcastURLResponse503]:
    """Fetch the WebSocket URL & first payload for a TikTok LIVE Room given a Room ID.

    **Authentication (Optional):** Anonymous access is supported. For authenticated requests, provide
    exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        client_query (str | Unset):  Default: 'ttlive-other'.
        cursor (str | Unset):
        user_agent (str | Unset):
        client_enter (bool | Unset):  Default: True.
        platform (WebcastFetchPlatform | Unset): Transport for a webcast fetch, and this API's own
            query contract. The scrape server's `webcastFetch` route is web-only and carries no
            platform, so mobile is served by the mobile signing API (see `fetchWebcastMobileUrl`)
            instead.
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FetchWebcastURLResponse429 | FetchWebcastURLResponse500 | FetchWebcastURLResponse503]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        client_query=client_query,
        cursor=cursor,
        user_agent=user_agent,
        client_enter=client_enter,
        platform=platform,
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
    client_query: str | Unset = "ttlive-other",
    cursor: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    client_enter: bool | Unset = True,
    platform: WebcastFetchPlatform | Unset = UNSET,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> FetchWebcastURLResponse429 | FetchWebcastURLResponse500 | FetchWebcastURLResponse503 | None:
    """Fetch the WebSocket URL & first payload for a TikTok LIVE Room given a Room ID.

    **Authentication (Optional):** Anonymous access is supported. For authenticated requests, provide
    exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        client_query (str | Unset):  Default: 'ttlive-other'.
        cursor (str | Unset):
        user_agent (str | Unset):
        client_enter (bool | Unset):  Default: True.
        platform (WebcastFetchPlatform | Unset): Transport for a webcast fetch, and this API's own
            query contract. The scrape server's `webcastFetch` route is web-only and carries no
            platform, so mobile is served by the mobile signing API (see `fetchWebcastMobileUrl`)
            instead.
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FetchWebcastURLResponse429 | FetchWebcastURLResponse500 | FetchWebcastURLResponse503
    """

    return sync_detailed(
        room_id=room_id,
        client=client,
        client_query=client_query,
        cursor=cursor,
        user_agent=user_agent,
        client_enter=client_enter,
        platform=platform,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    ).parsed


async def asyncio_detailed(
    room_id: str,
    *,
    client: AuthenticatedClient,
    client_query: str | Unset = "ttlive-other",
    cursor: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    client_enter: bool | Unset = True,
    platform: WebcastFetchPlatform | Unset = UNSET,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Response[FetchWebcastURLResponse429 | FetchWebcastURLResponse500 | FetchWebcastURLResponse503]:
    """Fetch the WebSocket URL & first payload for a TikTok LIVE Room given a Room ID.

    **Authentication (Optional):** Anonymous access is supported. For authenticated requests, provide
    exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        client_query (str | Unset):  Default: 'ttlive-other'.
        cursor (str | Unset):
        user_agent (str | Unset):
        client_enter (bool | Unset):  Default: True.
        platform (WebcastFetchPlatform | Unset): Transport for a webcast fetch, and this API's own
            query contract. The scrape server's `webcastFetch` route is web-only and carries no
            platform, so mobile is served by the mobile signing API (see `fetchWebcastMobileUrl`)
            instead.
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FetchWebcastURLResponse429 | FetchWebcastURLResponse500 | FetchWebcastURLResponse503]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        client_query=client_query,
        cursor=cursor,
        user_agent=user_agent,
        client_enter=client_enter,
        platform=platform,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    room_id: str,
    *,
    client: AuthenticatedClient,
    client_query: str | Unset = "ttlive-other",
    cursor: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    client_enter: bool | Unset = True,
    platform: WebcastFetchPlatform | Unset = UNSET,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> FetchWebcastURLResponse429 | FetchWebcastURLResponse500 | FetchWebcastURLResponse503 | None:
    """Fetch the WebSocket URL & first payload for a TikTok LIVE Room given a Room ID.

    **Authentication (Optional):** Anonymous access is supported. For authenticated requests, provide
    exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        client_query (str | Unset):  Default: 'ttlive-other'.
        cursor (str | Unset):
        user_agent (str | Unset):
        client_enter (bool | Unset):  Default: True.
        platform (WebcastFetchPlatform | Unset): Transport for a webcast fetch, and this API's own
            query contract. The scrape server's `webcastFetch` route is web-only and carries no
            platform, so mobile is served by the mobile signing API (see `fetchWebcastMobileUrl`)
            instead.
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FetchWebcastURLResponse429 | FetchWebcastURLResponse500 | FetchWebcastURLResponse503
    """

    return (
        await asyncio_detailed(
            room_id=room_id,
            client=client,
            client_query=client_query,
            cursor=cursor,
            user_agent=user_agent,
            client_enter=client_enter,
            platform=platform,
            x_oauth_token=x_oauth_token,
            x_cookie_header=x_cookie_header,
        )
    ).parsed

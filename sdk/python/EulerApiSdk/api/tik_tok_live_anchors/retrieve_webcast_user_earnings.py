from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_webcast_user_earnings_response_429 import RetrieveWebcastUserEarningsResponse429
from ...models.retrieve_webcast_user_earnings_response_500 import RetrieveWebcastUserEarningsResponse500
from ...models.retrieve_webcast_user_earnings_response_503 import RetrieveWebcastUserEarningsResponse503
from ...models.route_image_source import RouteImageSource
from ...models.webcast_user_earnings_output_period import WebcastUserEarningsOutputPeriod
from ...models.webcast_user_earnings_response import WebcastUserEarningsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    unique_id: str,
    *,
    period: WebcastUserEarningsOutputPeriod | Unset = UNSET,
    session_id: str | Unset = UNSET,
    tt_target_idc: str | Unset = UNSET,
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

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    params["session_id"] = session_id

    params["tt_target_idc"] = tt_target_idc

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/anchors/{unique_id}/earnings".format(
            unique_id=quote(str(unique_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RetrieveWebcastUserEarningsResponse429
    | RetrieveWebcastUserEarningsResponse500
    | RetrieveWebcastUserEarningsResponse503
    | WebcastUserEarningsResponse
    | None
):
    if response.status_code == 200:
        response_200 = WebcastUserEarningsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveWebcastUserEarningsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveWebcastUserEarningsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RetrieveWebcastUserEarningsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RetrieveWebcastUserEarningsResponse429
    | RetrieveWebcastUserEarningsResponse500
    | RetrieveWebcastUserEarningsResponse503
    | WebcastUserEarningsResponse
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
    period: WebcastUserEarningsOutputPeriod | Unset = UNSET,
    session_id: str | Unset = UNSET,
    tt_target_idc: str | Unset = UNSET,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[
    RetrieveWebcastUserEarningsResponse429
    | RetrieveWebcastUserEarningsResponse500
    | RetrieveWebcastUserEarningsResponse503
    | WebcastUserEarningsResponse
]:
    """Retrieve TikTok LIVE earnings for a specific user.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        unique_id (str):
        period (WebcastUserEarningsOutputPeriod | Unset):
        session_id (str | Unset):
        tt_target_idc (str | Unset):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveWebcastUserEarningsResponse429 | RetrieveWebcastUserEarningsResponse500 | RetrieveWebcastUserEarningsResponse503 | WebcastUserEarningsResponse]
    """

    kwargs = _get_kwargs(
        unique_id=unique_id,
        period=period,
        session_id=session_id,
        tt_target_idc=tt_target_idc,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
        x_image_source=x_image_source,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    unique_id: str,
    *,
    client: AuthenticatedClient,
    period: WebcastUserEarningsOutputPeriod | Unset = UNSET,
    session_id: str | Unset = UNSET,
    tt_target_idc: str | Unset = UNSET,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> (
    RetrieveWebcastUserEarningsResponse429
    | RetrieveWebcastUserEarningsResponse500
    | RetrieveWebcastUserEarningsResponse503
    | WebcastUserEarningsResponse
    | None
):
    """Retrieve TikTok LIVE earnings for a specific user.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        unique_id (str):
        period (WebcastUserEarningsOutputPeriod | Unset):
        session_id (str | Unset):
        tt_target_idc (str | Unset):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveWebcastUserEarningsResponse429 | RetrieveWebcastUserEarningsResponse500 | RetrieveWebcastUserEarningsResponse503 | WebcastUserEarningsResponse
    """

    return sync_detailed(
        unique_id=unique_id,
        client=client,
        period=period,
        session_id=session_id,
        tt_target_idc=tt_target_idc,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
        x_image_source=x_image_source,
    ).parsed


async def asyncio_detailed(
    unique_id: str,
    *,
    client: AuthenticatedClient,
    period: WebcastUserEarningsOutputPeriod | Unset = UNSET,
    session_id: str | Unset = UNSET,
    tt_target_idc: str | Unset = UNSET,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[
    RetrieveWebcastUserEarningsResponse429
    | RetrieveWebcastUserEarningsResponse500
    | RetrieveWebcastUserEarningsResponse503
    | WebcastUserEarningsResponse
]:
    """Retrieve TikTok LIVE earnings for a specific user.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        unique_id (str):
        period (WebcastUserEarningsOutputPeriod | Unset):
        session_id (str | Unset):
        tt_target_idc (str | Unset):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveWebcastUserEarningsResponse429 | RetrieveWebcastUserEarningsResponse500 | RetrieveWebcastUserEarningsResponse503 | WebcastUserEarningsResponse]
    """

    kwargs = _get_kwargs(
        unique_id=unique_id,
        period=period,
        session_id=session_id,
        tt_target_idc=tt_target_idc,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
        x_image_source=x_image_source,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    unique_id: str,
    *,
    client: AuthenticatedClient,
    period: WebcastUserEarningsOutputPeriod | Unset = UNSET,
    session_id: str | Unset = UNSET,
    tt_target_idc: str | Unset = UNSET,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> (
    RetrieveWebcastUserEarningsResponse429
    | RetrieveWebcastUserEarningsResponse500
    | RetrieveWebcastUserEarningsResponse503
    | WebcastUserEarningsResponse
    | None
):
    """Retrieve TikTok LIVE earnings for a specific user.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        unique_id (str):
        period (WebcastUserEarningsOutputPeriod | Unset):
        session_id (str | Unset):
        tt_target_idc (str | Unset):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveWebcastUserEarningsResponse429 | RetrieveWebcastUserEarningsResponse500 | RetrieveWebcastUserEarningsResponse503 | WebcastUserEarningsResponse
    """

    return (
        await asyncio_detailed(
            unique_id=unique_id,
            client=client,
            period=period,
            session_id=session_id,
            tt_target_idc=tt_target_idc,
            x_oauth_token=x_oauth_token,
            x_cookie_header=x_cookie_header,
            x_image_source=x_image_source,
        )
    ).parsed

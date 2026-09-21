from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pooled_proxy_region import PooledProxyRegion
from ...models.retrieve_webcast_feed_response_429 import RetrieveWebcastFeedResponse429
from ...models.retrieve_webcast_feed_response_500 import RetrieveWebcastFeedResponse500
from ...models.retrieve_webcast_feed_response_503 import RetrieveWebcastFeedResponse503
from ...models.route_image_source import RouteImageSource
from ...models.webcast_feed_route_response import WebcastFeedRouteResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    region: PooledProxyRegion,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_image_source, Unset):
        headers["x-image-source"] = str(x_image_source)

    params: dict[str, Any] = {}

    json_region = region.value
    params["region"] = json_region

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/feed",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RetrieveWebcastFeedResponse429
    | RetrieveWebcastFeedResponse500
    | RetrieveWebcastFeedResponse503
    | WebcastFeedRouteResponse
    | None
):
    if response.status_code == 200:
        response_200 = WebcastFeedRouteResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveWebcastFeedResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveWebcastFeedResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RetrieveWebcastFeedResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RetrieveWebcastFeedResponse429
    | RetrieveWebcastFeedResponse500
    | RetrieveWebcastFeedResponse503
    | WebcastFeedRouteResponse
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
    region: PooledProxyRegion,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[
    RetrieveWebcastFeedResponse429
    | RetrieveWebcastFeedResponse500
    | RetrieveWebcastFeedResponse503
    | WebcastFeedRouteResponse
]:
    """Fetch the TikTok LIVE webcast feed for a specific region. Gets a random sampling of creators for a
    region.

    Args:
        region (PooledProxyRegion):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveWebcastFeedResponse429 | RetrieveWebcastFeedResponse500 | RetrieveWebcastFeedResponse503 | WebcastFeedRouteResponse]
    """

    kwargs = _get_kwargs(
        region=region,
        x_image_source=x_image_source,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    region: PooledProxyRegion,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> (
    RetrieveWebcastFeedResponse429
    | RetrieveWebcastFeedResponse500
    | RetrieveWebcastFeedResponse503
    | WebcastFeedRouteResponse
    | None
):
    """Fetch the TikTok LIVE webcast feed for a specific region. Gets a random sampling of creators for a
    region.

    Args:
        region (PooledProxyRegion):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveWebcastFeedResponse429 | RetrieveWebcastFeedResponse500 | RetrieveWebcastFeedResponse503 | WebcastFeedRouteResponse
    """

    return sync_detailed(
        client=client,
        region=region,
        x_image_source=x_image_source,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    region: PooledProxyRegion,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[
    RetrieveWebcastFeedResponse429
    | RetrieveWebcastFeedResponse500
    | RetrieveWebcastFeedResponse503
    | WebcastFeedRouteResponse
]:
    """Fetch the TikTok LIVE webcast feed for a specific region. Gets a random sampling of creators for a
    region.

    Args:
        region (PooledProxyRegion):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveWebcastFeedResponse429 | RetrieveWebcastFeedResponse500 | RetrieveWebcastFeedResponse503 | WebcastFeedRouteResponse]
    """

    kwargs = _get_kwargs(
        region=region,
        x_image_source=x_image_source,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    region: PooledProxyRegion,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> (
    RetrieveWebcastFeedResponse429
    | RetrieveWebcastFeedResponse500
    | RetrieveWebcastFeedResponse503
    | WebcastFeedRouteResponse
    | None
):
    """Fetch the TikTok LIVE webcast feed for a specific region. Gets a random sampling of creators for a
    region.

    Args:
        region (PooledProxyRegion):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveWebcastFeedResponse429 | RetrieveWebcastFeedResponse500 | RetrieveWebcastFeedResponse503 | WebcastFeedRouteResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            region=region,
            x_image_source=x_image_source,
        )
    ).parsed

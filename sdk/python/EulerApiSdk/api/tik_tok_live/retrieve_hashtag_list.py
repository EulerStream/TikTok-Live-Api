from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hashtag_list_api_response import HashtagListAPIResponse
from ...models.retrieve_hashtag_list_response_429 import RetrieveHashtagListResponse429
from ...models.retrieve_hashtag_list_response_500 import RetrieveHashtagListResponse500
from ...models.retrieve_hashtag_list_response_503 import RetrieveHashtagListResponse503
from ...models.route_image_source import RouteImageSource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_image_source, Unset):
        headers["x-image-source"] = str(x_image_source)

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/hashtags",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HashtagListAPIResponse
    | RetrieveHashtagListResponse429
    | RetrieveHashtagListResponse500
    | RetrieveHashtagListResponse503
    | None
):
    if response.status_code == 200:
        response_200 = HashtagListAPIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveHashtagListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveHashtagListResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RetrieveHashtagListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    HashtagListAPIResponse
    | RetrieveHashtagListResponse429
    | RetrieveHashtagListResponse500
    | RetrieveHashtagListResponse503
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
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[
    HashtagListAPIResponse
    | RetrieveHashtagListResponse429
    | RetrieveHashtagListResponse500
    | RetrieveHashtagListResponse503
]:
    """Retrieve the list of available hashtags for TikTok LIVE streams.

    Args:
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HashtagListAPIResponse | RetrieveHashtagListResponse429 | RetrieveHashtagListResponse500 | RetrieveHashtagListResponse503]
    """

    kwargs = _get_kwargs(
        x_image_source=x_image_source,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> (
    HashtagListAPIResponse
    | RetrieveHashtagListResponse429
    | RetrieveHashtagListResponse500
    | RetrieveHashtagListResponse503
    | None
):
    """Retrieve the list of available hashtags for TikTok LIVE streams.

    Args:
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HashtagListAPIResponse | RetrieveHashtagListResponse429 | RetrieveHashtagListResponse500 | RetrieveHashtagListResponse503
    """

    return sync_detailed(
        client=client,
        x_image_source=x_image_source,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[
    HashtagListAPIResponse
    | RetrieveHashtagListResponse429
    | RetrieveHashtagListResponse500
    | RetrieveHashtagListResponse503
]:
    """Retrieve the list of available hashtags for TikTok LIVE streams.

    Args:
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HashtagListAPIResponse | RetrieveHashtagListResponse429 | RetrieveHashtagListResponse500 | RetrieveHashtagListResponse503]
    """

    kwargs = _get_kwargs(
        x_image_source=x_image_source,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> (
    HashtagListAPIResponse
    | RetrieveHashtagListResponse429
    | RetrieveHashtagListResponse500
    | RetrieveHashtagListResponse503
    | None
):
    """Retrieve the list of available hashtags for TikTok LIVE streams.

    Args:
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HashtagListAPIResponse | RetrieveHashtagListResponse429 | RetrieveHashtagListResponse500 | RetrieveHashtagListResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            x_image_source=x_image_source,
        )
    ).parsed

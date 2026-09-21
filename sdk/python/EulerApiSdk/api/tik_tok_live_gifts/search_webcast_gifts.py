from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_webcast_gifts_response_429 import SearchWebcastGiftsResponse429
from ...models.search_webcast_gifts_response_500 import SearchWebcastGiftsResponse500
from ...models.search_webcast_gifts_response_503 import SearchWebcastGiftsResponse503
from ...models.webcast_gift_search_response import WebcastGiftSearchResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    query: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["query"] = query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webcast/gifts/catalog/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    SearchWebcastGiftsResponse429
    | SearchWebcastGiftsResponse500
    | SearchWebcastGiftsResponse503
    | WebcastGiftSearchResponse
    | None
):
    if response.status_code == 200:
        response_200 = WebcastGiftSearchResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = SearchWebcastGiftsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = SearchWebcastGiftsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = SearchWebcastGiftsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    SearchWebcastGiftsResponse429
    | SearchWebcastGiftsResponse500
    | SearchWebcastGiftsResponse503
    | WebcastGiftSearchResponse
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
    query: str,
) -> Response[
    SearchWebcastGiftsResponse429
    | SearchWebcastGiftsResponse500
    | SearchWebcastGiftsResponse503
    | WebcastGiftSearchResponse
]:
    """Search the TikTok LIVE gift catalogue by gift name.

    This is a special route, it does NOT fetch data live, and therefore does not count to your
    hourly/daily rate limits.

    Args:
        query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchWebcastGiftsResponse429 | SearchWebcastGiftsResponse500 | SearchWebcastGiftsResponse503 | WebcastGiftSearchResponse]
    """

    kwargs = _get_kwargs(
        query=query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    query: str,
) -> (
    SearchWebcastGiftsResponse429
    | SearchWebcastGiftsResponse500
    | SearchWebcastGiftsResponse503
    | WebcastGiftSearchResponse
    | None
):
    """Search the TikTok LIVE gift catalogue by gift name.

    This is a special route, it does NOT fetch data live, and therefore does not count to your
    hourly/daily rate limits.

    Args:
        query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchWebcastGiftsResponse429 | SearchWebcastGiftsResponse500 | SearchWebcastGiftsResponse503 | WebcastGiftSearchResponse
    """

    return sync_detailed(
        client=client,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    query: str,
) -> Response[
    SearchWebcastGiftsResponse429
    | SearchWebcastGiftsResponse500
    | SearchWebcastGiftsResponse503
    | WebcastGiftSearchResponse
]:
    """Search the TikTok LIVE gift catalogue by gift name.

    This is a special route, it does NOT fetch data live, and therefore does not count to your
    hourly/daily rate limits.

    Args:
        query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchWebcastGiftsResponse429 | SearchWebcastGiftsResponse500 | SearchWebcastGiftsResponse503 | WebcastGiftSearchResponse]
    """

    kwargs = _get_kwargs(
        query=query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    query: str,
) -> (
    SearchWebcastGiftsResponse429
    | SearchWebcastGiftsResponse500
    | SearchWebcastGiftsResponse503
    | WebcastGiftSearchResponse
    | None
):
    """Search the TikTok LIVE gift catalogue by gift name.

    This is a special route, it does NOT fetch data live, and therefore does not count to your
    hourly/daily rate limits.

    Args:
        query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchWebcastGiftsResponse429 | SearchWebcastGiftsResponse500 | SearchWebcastGiftsResponse503 | WebcastGiftSearchResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
        )
    ).parsed

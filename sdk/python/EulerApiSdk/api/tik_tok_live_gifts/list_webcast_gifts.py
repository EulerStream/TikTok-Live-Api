from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.gift_catalog_order_by import GiftCatalogOrderBy
from ...models.list_webcast_gifts_response_429 import ListWebcastGiftsResponse429
from ...models.list_webcast_gifts_response_500 import ListWebcastGiftsResponse500
from ...models.list_webcast_gifts_response_503 import ListWebcastGiftsResponse503
from ...models.webcast_giftcatalog_response import WebcastGiftcatalogResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: float | Unset = 50.0,
    page_number: float | Unset = 1.0,
    order_by: GiftCatalogOrderBy | Unset = UNSET,
    ascending: bool | Unset = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["orderBy"] = json_order_by

    params["ascending"] = ascending

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/gifts/catalog",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListWebcastGiftsResponse429
    | ListWebcastGiftsResponse500
    | ListWebcastGiftsResponse503
    | WebcastGiftcatalogResponse
    | None
):
    if response.status_code == 200:
        response_200 = WebcastGiftcatalogResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = ListWebcastGiftsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListWebcastGiftsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListWebcastGiftsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListWebcastGiftsResponse429 | ListWebcastGiftsResponse500 | ListWebcastGiftsResponse503 | WebcastGiftcatalogResponse
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
    page_size: float | Unset = 50.0,
    page_number: float | Unset = 1.0,
    order_by: GiftCatalogOrderBy | Unset = UNSET,
    ascending: bool | Unset = True,
) -> Response[
    ListWebcastGiftsResponse429 | ListWebcastGiftsResponse500 | ListWebcastGiftsResponse503 | WebcastGiftcatalogResponse
]:
    """List the full TikTok LIVE gift catalog, paginated.

    This is a special route, it does NOT fetch data live, and therefore does not count to your
    hourly/daily rate limits.

    Args:
        page_size (float | Unset):  Default: 50.0.
        page_number (float | Unset):  Default: 1.0.
        order_by (GiftCatalogOrderBy | Unset): Friendly catalog sort options, mapped to the gifts-
            server enum below.
        ascending (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListWebcastGiftsResponse429 | ListWebcastGiftsResponse500 | ListWebcastGiftsResponse503 | WebcastGiftcatalogResponse]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_number=page_number,
        order_by=order_by,
        ascending=ascending,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page_size: float | Unset = 50.0,
    page_number: float | Unset = 1.0,
    order_by: GiftCatalogOrderBy | Unset = UNSET,
    ascending: bool | Unset = True,
) -> (
    ListWebcastGiftsResponse429
    | ListWebcastGiftsResponse500
    | ListWebcastGiftsResponse503
    | WebcastGiftcatalogResponse
    | None
):
    """List the full TikTok LIVE gift catalog, paginated.

    This is a special route, it does NOT fetch data live, and therefore does not count to your
    hourly/daily rate limits.

    Args:
        page_size (float | Unset):  Default: 50.0.
        page_number (float | Unset):  Default: 1.0.
        order_by (GiftCatalogOrderBy | Unset): Friendly catalog sort options, mapped to the gifts-
            server enum below.
        ascending (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListWebcastGiftsResponse429 | ListWebcastGiftsResponse500 | ListWebcastGiftsResponse503 | WebcastGiftcatalogResponse
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        page_number=page_number,
        order_by=order_by,
        ascending=ascending,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page_size: float | Unset = 50.0,
    page_number: float | Unset = 1.0,
    order_by: GiftCatalogOrderBy | Unset = UNSET,
    ascending: bool | Unset = True,
) -> Response[
    ListWebcastGiftsResponse429 | ListWebcastGiftsResponse500 | ListWebcastGiftsResponse503 | WebcastGiftcatalogResponse
]:
    """List the full TikTok LIVE gift catalog, paginated.

    This is a special route, it does NOT fetch data live, and therefore does not count to your
    hourly/daily rate limits.

    Args:
        page_size (float | Unset):  Default: 50.0.
        page_number (float | Unset):  Default: 1.0.
        order_by (GiftCatalogOrderBy | Unset): Friendly catalog sort options, mapped to the gifts-
            server enum below.
        ascending (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListWebcastGiftsResponse429 | ListWebcastGiftsResponse500 | ListWebcastGiftsResponse503 | WebcastGiftcatalogResponse]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_number=page_number,
        order_by=order_by,
        ascending=ascending,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page_size: float | Unset = 50.0,
    page_number: float | Unset = 1.0,
    order_by: GiftCatalogOrderBy | Unset = UNSET,
    ascending: bool | Unset = True,
) -> (
    ListWebcastGiftsResponse429
    | ListWebcastGiftsResponse500
    | ListWebcastGiftsResponse503
    | WebcastGiftcatalogResponse
    | None
):
    """List the full TikTok LIVE gift catalog, paginated.

    This is a special route, it does NOT fetch data live, and therefore does not count to your
    hourly/daily rate limits.

    Args:
        page_size (float | Unset):  Default: 50.0.
        page_number (float | Unset):  Default: 1.0.
        order_by (GiftCatalogOrderBy | Unset): Friendly catalog sort options, mapped to the gifts-
            server enum below.
        ascending (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListWebcastGiftsResponse429 | ListWebcastGiftsResponse500 | ListWebcastGiftsResponse503 | WebcastGiftcatalogResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            page_number=page_number,
            order_by=order_by,
            ascending=ascending,
        )
    ).parsed

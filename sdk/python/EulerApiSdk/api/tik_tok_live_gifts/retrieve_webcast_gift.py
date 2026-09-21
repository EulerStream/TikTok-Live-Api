from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_webcast_gift_response_429 import RetrieveWebcastGiftResponse429
from ...models.retrieve_webcast_gift_response_500 import RetrieveWebcastGiftResponse500
from ...models.retrieve_webcast_gift_response_503 import RetrieveWebcastGiftResponse503
from ...models.webcast_gift_response import WebcastGiftResponse
from ...types import Response


def _get_kwargs(
    gift_id: float,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/gifts/catalog/{gift_id}".format(
            gift_id=quote(str(gift_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RetrieveWebcastGiftResponse429
    | RetrieveWebcastGiftResponse500
    | RetrieveWebcastGiftResponse503
    | WebcastGiftResponse
    | None
):
    if response.status_code == 200:
        response_200 = WebcastGiftResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveWebcastGiftResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveWebcastGiftResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RetrieveWebcastGiftResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RetrieveWebcastGiftResponse429
    | RetrieveWebcastGiftResponse500
    | RetrieveWebcastGiftResponse503
    | WebcastGiftResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    gift_id: float,
    *,
    client: AuthenticatedClient,
) -> Response[
    RetrieveWebcastGiftResponse429
    | RetrieveWebcastGiftResponse500
    | RetrieveWebcastGiftResponse503
    | WebcastGiftResponse
]:
    """Retrieve a single TikTok LIVE gift by its numeric gift ID.

    This is a special route, it does NOT fetch data live, and therefore does not count to your
    hourly/daily rate limits.

    Args:
        gift_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveWebcastGiftResponse429 | RetrieveWebcastGiftResponse500 | RetrieveWebcastGiftResponse503 | WebcastGiftResponse]
    """

    kwargs = _get_kwargs(
        gift_id=gift_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    gift_id: float,
    *,
    client: AuthenticatedClient,
) -> (
    RetrieveWebcastGiftResponse429
    | RetrieveWebcastGiftResponse500
    | RetrieveWebcastGiftResponse503
    | WebcastGiftResponse
    | None
):
    """Retrieve a single TikTok LIVE gift by its numeric gift ID.

    This is a special route, it does NOT fetch data live, and therefore does not count to your
    hourly/daily rate limits.

    Args:
        gift_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveWebcastGiftResponse429 | RetrieveWebcastGiftResponse500 | RetrieveWebcastGiftResponse503 | WebcastGiftResponse
    """

    return sync_detailed(
        gift_id=gift_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    gift_id: float,
    *,
    client: AuthenticatedClient,
) -> Response[
    RetrieveWebcastGiftResponse429
    | RetrieveWebcastGiftResponse500
    | RetrieveWebcastGiftResponse503
    | WebcastGiftResponse
]:
    """Retrieve a single TikTok LIVE gift by its numeric gift ID.

    This is a special route, it does NOT fetch data live, and therefore does not count to your
    hourly/daily rate limits.

    Args:
        gift_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveWebcastGiftResponse429 | RetrieveWebcastGiftResponse500 | RetrieveWebcastGiftResponse503 | WebcastGiftResponse]
    """

    kwargs = _get_kwargs(
        gift_id=gift_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    gift_id: float,
    *,
    client: AuthenticatedClient,
) -> (
    RetrieveWebcastGiftResponse429
    | RetrieveWebcastGiftResponse500
    | RetrieveWebcastGiftResponse503
    | WebcastGiftResponse
    | None
):
    """Retrieve a single TikTok LIVE gift by its numeric gift ID.

    This is a special route, it does NOT fetch data live, and therefore does not count to your
    hourly/daily rate limits.

    Args:
        gift_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveWebcastGiftResponse429 | RetrieveWebcastGiftResponse500 | RetrieveWebcastGiftResponse503 | WebcastGiftResponse
    """

    return (
        await asyncio_detailed(
            gift_id=gift_id,
            client=client,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_room_info_response_429 import RetrieveRoomInfoResponse429
from ...models.retrieve_room_info_response_500 import RetrieveRoomInfoResponse500
from ...models.retrieve_room_info_response_503 import RetrieveRoomInfoResponse503
from ...models.route_image_source import RouteImageSource
from ...models.webcast_room_info_route_response import WebcastRoomInfoRouteResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    unique_id: str,
    *,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_image_source, Unset):
        headers["x-image-source"] = str(x_image_source)

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/anchors/{unique_id}/room_info".format(
            unique_id=quote(str(unique_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RetrieveRoomInfoResponse429
    | RetrieveRoomInfoResponse500
    | RetrieveRoomInfoResponse503
    | WebcastRoomInfoRouteResponse
    | None
):
    if response.status_code == 200:
        response_200 = WebcastRoomInfoRouteResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveRoomInfoResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveRoomInfoResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RetrieveRoomInfoResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RetrieveRoomInfoResponse429
    | RetrieveRoomInfoResponse500
    | RetrieveRoomInfoResponse503
    | WebcastRoomInfoRouteResponse
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
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[
    RetrieveRoomInfoResponse429
    | RetrieveRoomInfoResponse500
    | RetrieveRoomInfoResponse503
    | WebcastRoomInfoRouteResponse
]:
    """Retrieve TikTok Live Room Information

    Args:
        unique_id (str):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveRoomInfoResponse429 | RetrieveRoomInfoResponse500 | RetrieveRoomInfoResponse503 | WebcastRoomInfoRouteResponse]
    """

    kwargs = _get_kwargs(
        unique_id=unique_id,
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
    x_image_source: RouteImageSource | Unset = UNSET,
) -> (
    RetrieveRoomInfoResponse429
    | RetrieveRoomInfoResponse500
    | RetrieveRoomInfoResponse503
    | WebcastRoomInfoRouteResponse
    | None
):
    """Retrieve TikTok Live Room Information

    Args:
        unique_id (str):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveRoomInfoResponse429 | RetrieveRoomInfoResponse500 | RetrieveRoomInfoResponse503 | WebcastRoomInfoRouteResponse
    """

    return sync_detailed(
        unique_id=unique_id,
        client=client,
        x_image_source=x_image_source,
    ).parsed


async def asyncio_detailed(
    unique_id: str,
    *,
    client: AuthenticatedClient,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[
    RetrieveRoomInfoResponse429
    | RetrieveRoomInfoResponse500
    | RetrieveRoomInfoResponse503
    | WebcastRoomInfoRouteResponse
]:
    """Retrieve TikTok Live Room Information

    Args:
        unique_id (str):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveRoomInfoResponse429 | RetrieveRoomInfoResponse500 | RetrieveRoomInfoResponse503 | WebcastRoomInfoRouteResponse]
    """

    kwargs = _get_kwargs(
        unique_id=unique_id,
        x_image_source=x_image_source,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    unique_id: str,
    *,
    client: AuthenticatedClient,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> (
    RetrieveRoomInfoResponse429
    | RetrieveRoomInfoResponse500
    | RetrieveRoomInfoResponse503
    | WebcastRoomInfoRouteResponse
    | None
):
    """Retrieve TikTok Live Room Information

    Args:
        unique_id (str):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveRoomInfoResponse429 | RetrieveRoomInfoResponse500 | RetrieveRoomInfoResponse503 | WebcastRoomInfoRouteResponse
    """

    return (
        await asyncio_detailed(
            unique_id=unique_id,
            client=client,
            x_image_source=x_image_source,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_webcast_event_response import RetrieveWebcastEventResponse
from ...models.retrieve_webcast_event_response_429 import RetrieveWebcastEventResponse429
from ...models.retrieve_webcast_event_response_500 import RetrieveWebcastEventResponse500
from ...models.retrieve_webcast_event_response_503 import RetrieveWebcastEventResponse503
from ...models.route_image_source import RouteImageSource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    event_id: str,
    *,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_image_source, Unset):
        headers["x-image-source"] = str(x_image_source)

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/events/{event_id}".format(
            event_id=quote(str(event_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RetrieveWebcastEventResponse
    | RetrieveWebcastEventResponse429
    | RetrieveWebcastEventResponse500
    | RetrieveWebcastEventResponse503
    | None
):
    if response.status_code == 200:
        response_200 = RetrieveWebcastEventResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveWebcastEventResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveWebcastEventResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RetrieveWebcastEventResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RetrieveWebcastEventResponse
    | RetrieveWebcastEventResponse429
    | RetrieveWebcastEventResponse500
    | RetrieveWebcastEventResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_id: str,
    *,
    client: AuthenticatedClient,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[
    RetrieveWebcastEventResponse
    | RetrieveWebcastEventResponse429
    | RetrieveWebcastEventResponse500
    | RetrieveWebcastEventResponse503
]:
    """Retrieve a single TikTok LIVE event (a scheduled/subscription stream) by
    its event ID.

    Args:
        event_id (str):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveWebcastEventResponse | RetrieveWebcastEventResponse429 | RetrieveWebcastEventResponse500 | RetrieveWebcastEventResponse503]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        x_image_source=x_image_source,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_id: str,
    *,
    client: AuthenticatedClient,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> (
    RetrieveWebcastEventResponse
    | RetrieveWebcastEventResponse429
    | RetrieveWebcastEventResponse500
    | RetrieveWebcastEventResponse503
    | None
):
    """Retrieve a single TikTok LIVE event (a scheduled/subscription stream) by
    its event ID.

    Args:
        event_id (str):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveWebcastEventResponse | RetrieveWebcastEventResponse429 | RetrieveWebcastEventResponse500 | RetrieveWebcastEventResponse503
    """

    return sync_detailed(
        event_id=event_id,
        client=client,
        x_image_source=x_image_source,
    ).parsed


async def asyncio_detailed(
    event_id: str,
    *,
    client: AuthenticatedClient,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[
    RetrieveWebcastEventResponse
    | RetrieveWebcastEventResponse429
    | RetrieveWebcastEventResponse500
    | RetrieveWebcastEventResponse503
]:
    """Retrieve a single TikTok LIVE event (a scheduled/subscription stream) by
    its event ID.

    Args:
        event_id (str):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveWebcastEventResponse | RetrieveWebcastEventResponse429 | RetrieveWebcastEventResponse500 | RetrieveWebcastEventResponse503]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        x_image_source=x_image_source,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_id: str,
    *,
    client: AuthenticatedClient,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> (
    RetrieveWebcastEventResponse
    | RetrieveWebcastEventResponse429
    | RetrieveWebcastEventResponse500
    | RetrieveWebcastEventResponse503
    | None
):
    """Retrieve a single TikTok LIVE event (a scheduled/subscription stream) by
    its event ID.

    Args:
        event_id (str):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveWebcastEventResponse | RetrieveWebcastEventResponse429 | RetrieveWebcastEventResponse500 | RetrieveWebcastEventResponse503
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            client=client,
            x_image_source=x_image_source,
        )
    ).parsed

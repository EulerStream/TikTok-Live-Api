from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_room_cover_response import RetrieveRoomCoverResponse
from ...models.retrieve_room_cover_response_429 import RetrieveRoomCoverResponse429
from ...models.retrieve_room_cover_response_500 import RetrieveRoomCoverResponse500
from ...models.retrieve_room_cover_response_503 import RetrieveRoomCoverResponse503
from ...models.route_image_source import RouteImageSource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    unique_id: str,
    *,
    redirect: bool | Unset = True,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_image_source, Unset):
        headers["x-image-source"] = str(x_image_source)

    params: dict[str, Any] = {}

    params["redirect"] = redirect

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/anchors/{unique_id}/room_cover".format(
            unique_id=quote(str(unique_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | RetrieveRoomCoverResponse
    | RetrieveRoomCoverResponse429
    | RetrieveRoomCoverResponse500
    | RetrieveRoomCoverResponse503
    | None
):
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Any | RetrieveRoomCoverResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = RetrieveRoomCoverResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Any | RetrieveRoomCoverResponse, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveRoomCoverResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveRoomCoverResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RetrieveRoomCoverResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | RetrieveRoomCoverResponse
    | RetrieveRoomCoverResponse429
    | RetrieveRoomCoverResponse500
    | RetrieveRoomCoverResponse503
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
    redirect: bool | Unset = True,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[
    Any
    | RetrieveRoomCoverResponse
    | RetrieveRoomCoverResponse429
    | RetrieveRoomCoverResponse500
    | RetrieveRoomCoverResponse503
]:
    """Fetch TikTok LIVE Stream Cover URL given a uniqueId.

    Args:
        unique_id (str):
        redirect (bool | Unset):  Default: True.
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RetrieveRoomCoverResponse | RetrieveRoomCoverResponse429 | RetrieveRoomCoverResponse500 | RetrieveRoomCoverResponse503]
    """

    kwargs = _get_kwargs(
        unique_id=unique_id,
        redirect=redirect,
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
    redirect: bool | Unset = True,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> (
    Any
    | RetrieveRoomCoverResponse
    | RetrieveRoomCoverResponse429
    | RetrieveRoomCoverResponse500
    | RetrieveRoomCoverResponse503
    | None
):
    """Fetch TikTok LIVE Stream Cover URL given a uniqueId.

    Args:
        unique_id (str):
        redirect (bool | Unset):  Default: True.
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RetrieveRoomCoverResponse | RetrieveRoomCoverResponse429 | RetrieveRoomCoverResponse500 | RetrieveRoomCoverResponse503
    """

    return sync_detailed(
        unique_id=unique_id,
        client=client,
        redirect=redirect,
        x_image_source=x_image_source,
    ).parsed


async def asyncio_detailed(
    unique_id: str,
    *,
    client: AuthenticatedClient,
    redirect: bool | Unset = True,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[
    Any
    | RetrieveRoomCoverResponse
    | RetrieveRoomCoverResponse429
    | RetrieveRoomCoverResponse500
    | RetrieveRoomCoverResponse503
]:
    """Fetch TikTok LIVE Stream Cover URL given a uniqueId.

    Args:
        unique_id (str):
        redirect (bool | Unset):  Default: True.
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RetrieveRoomCoverResponse | RetrieveRoomCoverResponse429 | RetrieveRoomCoverResponse500 | RetrieveRoomCoverResponse503]
    """

    kwargs = _get_kwargs(
        unique_id=unique_id,
        redirect=redirect,
        x_image_source=x_image_source,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    unique_id: str,
    *,
    client: AuthenticatedClient,
    redirect: bool | Unset = True,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> (
    Any
    | RetrieveRoomCoverResponse
    | RetrieveRoomCoverResponse429
    | RetrieveRoomCoverResponse500
    | RetrieveRoomCoverResponse503
    | None
):
    """Fetch TikTok LIVE Stream Cover URL given a uniqueId.

    Args:
        unique_id (str):
        redirect (bool | Unset):  Default: True.
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RetrieveRoomCoverResponse | RetrieveRoomCoverResponse429 | RetrieveRoomCoverResponse500 | RetrieveRoomCoverResponse503
    """

    return (
        await asyncio_detailed(
            unique_id=unique_id,
            client=client,
            redirect=redirect,
            x_image_source=x_image_source,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_tik_tok_video_basic_response import RetrieveTikTokVideoBasicResponse
from ...models.retrieve_tik_tok_video_basic_response_429 import RetrieveTikTokVideoBasicResponse429
from ...models.retrieve_tik_tok_video_basic_response_500 import RetrieveTikTokVideoBasicResponse500
from ...models.route_image_source import RouteImageSource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    video_id: str,
    *,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_image_source, Unset):
        headers["x-image-source"] = str(x_image_source)

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tiktok/videos/{video_id}/basic".format(
            video_id=quote(str(video_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RetrieveTikTokVideoBasicResponse | RetrieveTikTokVideoBasicResponse429 | RetrieveTikTokVideoBasicResponse500 | None
):
    if response.status_code == 200:
        response_200 = RetrieveTikTokVideoBasicResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveTikTokVideoBasicResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveTikTokVideoBasicResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RetrieveTikTokVideoBasicResponse | RetrieveTikTokVideoBasicResponse429 | RetrieveTikTokVideoBasicResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    video_id: str,
    *,
    client: AuthenticatedClient,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[
    RetrieveTikTokVideoBasicResponse | RetrieveTikTokVideoBasicResponse429 | RetrieveTikTokVideoBasicResponse500
]:
    """Retrieve basic public info (thumbnail, description, hashtags, music, author) for a TikTok video by
    its numeric video ID.

    Args:
        video_id (str):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveTikTokVideoBasicResponse | RetrieveTikTokVideoBasicResponse429 | RetrieveTikTokVideoBasicResponse500]
    """

    kwargs = _get_kwargs(
        video_id=video_id,
        x_image_source=x_image_source,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    video_id: str,
    *,
    client: AuthenticatedClient,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> (
    RetrieveTikTokVideoBasicResponse | RetrieveTikTokVideoBasicResponse429 | RetrieveTikTokVideoBasicResponse500 | None
):
    """Retrieve basic public info (thumbnail, description, hashtags, music, author) for a TikTok video by
    its numeric video ID.

    Args:
        video_id (str):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveTikTokVideoBasicResponse | RetrieveTikTokVideoBasicResponse429 | RetrieveTikTokVideoBasicResponse500
    """

    return sync_detailed(
        video_id=video_id,
        client=client,
        x_image_source=x_image_source,
    ).parsed


async def asyncio_detailed(
    video_id: str,
    *,
    client: AuthenticatedClient,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[
    RetrieveTikTokVideoBasicResponse | RetrieveTikTokVideoBasicResponse429 | RetrieveTikTokVideoBasicResponse500
]:
    """Retrieve basic public info (thumbnail, description, hashtags, music, author) for a TikTok video by
    its numeric video ID.

    Args:
        video_id (str):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveTikTokVideoBasicResponse | RetrieveTikTokVideoBasicResponse429 | RetrieveTikTokVideoBasicResponse500]
    """

    kwargs = _get_kwargs(
        video_id=video_id,
        x_image_source=x_image_source,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    video_id: str,
    *,
    client: AuthenticatedClient,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> (
    RetrieveTikTokVideoBasicResponse | RetrieveTikTokVideoBasicResponse429 | RetrieveTikTokVideoBasicResponse500 | None
):
    """Retrieve basic public info (thumbnail, description, hashtags, music, author) for a TikTok video by
    its numeric video ID.

    Args:
        video_id (str):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveTikTokVideoBasicResponse | RetrieveTikTokVideoBasicResponse429 | RetrieveTikTokVideoBasicResponse500
    """

    return (
        await asyncio_detailed(
            video_id=video_id,
            client=client,
            x_image_source=x_image_source,
        )
    ).parsed

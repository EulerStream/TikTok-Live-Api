from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_tik_tok_user_info_response import RetrieveTikTokUserInfoResponse
from ...models.retrieve_tik_tok_user_info_response_429 import RetrieveTikTokUserInfoResponse429
from ...models.retrieve_tik_tok_user_info_response_500 import RetrieveTikTokUserInfoResponse500
from ...models.route_image_source import RouteImageSource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    numeric_user_id: str,
    *,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_image_source, Unset):
        headers["x-image-source"] = str(x_image_source)

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tiktok/users/{numeric_user_id}".format(
            numeric_user_id=quote(str(numeric_user_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RetrieveTikTokUserInfoResponse | RetrieveTikTokUserInfoResponse429 | RetrieveTikTokUserInfoResponse500 | None:
    if response.status_code == 200:
        response_200 = RetrieveTikTokUserInfoResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveTikTokUserInfoResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveTikTokUserInfoResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RetrieveTikTokUserInfoResponse | RetrieveTikTokUserInfoResponse429 | RetrieveTikTokUserInfoResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    numeric_user_id: str,
    *,
    client: AuthenticatedClient,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[RetrieveTikTokUserInfoResponse | RetrieveTikTokUserInfoResponse429 | RetrieveTikTokUserInfoResponse500]:
    """Retrieve profile info (avatars, follow counts, verification) for a TikTok user by their numeric user
    ID.

    Args:
        numeric_user_id (str):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveTikTokUserInfoResponse | RetrieveTikTokUserInfoResponse429 | RetrieveTikTokUserInfoResponse500]
    """

    kwargs = _get_kwargs(
        numeric_user_id=numeric_user_id,
        x_image_source=x_image_source,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    numeric_user_id: str,
    *,
    client: AuthenticatedClient,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> RetrieveTikTokUserInfoResponse | RetrieveTikTokUserInfoResponse429 | RetrieveTikTokUserInfoResponse500 | None:
    """Retrieve profile info (avatars, follow counts, verification) for a TikTok user by their numeric user
    ID.

    Args:
        numeric_user_id (str):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveTikTokUserInfoResponse | RetrieveTikTokUserInfoResponse429 | RetrieveTikTokUserInfoResponse500
    """

    return sync_detailed(
        numeric_user_id=numeric_user_id,
        client=client,
        x_image_source=x_image_source,
    ).parsed


async def asyncio_detailed(
    numeric_user_id: str,
    *,
    client: AuthenticatedClient,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> Response[RetrieveTikTokUserInfoResponse | RetrieveTikTokUserInfoResponse429 | RetrieveTikTokUserInfoResponse500]:
    """Retrieve profile info (avatars, follow counts, verification) for a TikTok user by their numeric user
    ID.

    Args:
        numeric_user_id (str):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveTikTokUserInfoResponse | RetrieveTikTokUserInfoResponse429 | RetrieveTikTokUserInfoResponse500]
    """

    kwargs = _get_kwargs(
        numeric_user_id=numeric_user_id,
        x_image_source=x_image_source,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    numeric_user_id: str,
    *,
    client: AuthenticatedClient,
    x_image_source: RouteImageSource | Unset = UNSET,
) -> RetrieveTikTokUserInfoResponse | RetrieveTikTokUserInfoResponse429 | RetrieveTikTokUserInfoResponse500 | None:
    """Retrieve profile info (avatars, follow counts, verification) for a TikTok user by their numeric user
    ID.

    Args:
        numeric_user_id (str):
        x_image_source (RouteImageSource | Unset): Where a scraped image URL should be served
            from. Selected per-request via the `x-image-source` header. Defaults to {@link
            RouteImageSource.ORIGIN}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveTikTokUserInfoResponse | RetrieveTikTokUserInfoResponse429 | RetrieveTikTokUserInfoResponse500
    """

    return (
        await asyncio_detailed(
            numeric_user_id=numeric_user_id,
            client=client,
            x_image_source=x_image_source,
        )
    ).parsed

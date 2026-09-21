from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pooled_proxy_region import PooledProxyRegion
from ...models.retrieve_webcast_gifts_response_429 import RetrieveWebcastGiftsResponse429
from ...models.retrieve_webcast_gifts_response_500 import RetrieveWebcastGiftsResponse500
from ...models.retrieve_webcast_gifts_response_503 import RetrieveWebcastGiftsResponse503
from ...models.retrieve_webcast_gifts_webcast_language import RetrieveWebcastGiftsWebcastLanguage
from ...models.webcast_gifts_response import WebcastGiftsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    region: PooledProxyRegion | Unset = UNSET,
    webcast_language: RetrieveWebcastGiftsWebcastLanguage | Unset = RetrieveWebcastGiftsWebcastLanguage.EN,
    redirect: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_region: str | Unset = UNSET
    if not isinstance(region, Unset):
        json_region = region.value

    params["region"] = json_region

    json_webcast_language: str | Unset = UNSET
    if not isinstance(webcast_language, Unset):
        json_webcast_language = webcast_language.value

    params["webcast_language"] = json_webcast_language

    params["redirect"] = redirect

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/gifts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | WebcastGiftsResponse
    | RetrieveWebcastGiftsResponse429
    | RetrieveWebcastGiftsResponse500
    | RetrieveWebcastGiftsResponse503
    | None
):
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Any | WebcastGiftsResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = WebcastGiftsResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Any | WebcastGiftsResponse, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveWebcastGiftsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveWebcastGiftsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RetrieveWebcastGiftsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | WebcastGiftsResponse
    | RetrieveWebcastGiftsResponse429
    | RetrieveWebcastGiftsResponse500
    | RetrieveWebcastGiftsResponse503
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
    region: PooledProxyRegion | Unset = UNSET,
    webcast_language: RetrieveWebcastGiftsWebcastLanguage | Unset = RetrieveWebcastGiftsWebcastLanguage.EN,
    redirect: bool | Unset = False,
) -> Response[
    Any
    | WebcastGiftsResponse
    | RetrieveWebcastGiftsResponse429
    | RetrieveWebcastGiftsResponse500
    | RetrieveWebcastGiftsResponse503
]:
    """Retrieve Webcast gifts for a given region

    Args:
        region (PooledProxyRegion | Unset):
        webcast_language (RetrieveWebcastGiftsWebcastLanguage | Unset):  Default:
            RetrieveWebcastGiftsWebcastLanguage.EN.
        redirect (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WebcastGiftsResponse | RetrieveWebcastGiftsResponse429 | RetrieveWebcastGiftsResponse500 | RetrieveWebcastGiftsResponse503]
    """

    kwargs = _get_kwargs(
        region=region,
        webcast_language=webcast_language,
        redirect=redirect,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    region: PooledProxyRegion | Unset = UNSET,
    webcast_language: RetrieveWebcastGiftsWebcastLanguage | Unset = RetrieveWebcastGiftsWebcastLanguage.EN,
    redirect: bool | Unset = False,
) -> (
    Any
    | WebcastGiftsResponse
    | RetrieveWebcastGiftsResponse429
    | RetrieveWebcastGiftsResponse500
    | RetrieveWebcastGiftsResponse503
    | None
):
    """Retrieve Webcast gifts for a given region

    Args:
        region (PooledProxyRegion | Unset):
        webcast_language (RetrieveWebcastGiftsWebcastLanguage | Unset):  Default:
            RetrieveWebcastGiftsWebcastLanguage.EN.
        redirect (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WebcastGiftsResponse | RetrieveWebcastGiftsResponse429 | RetrieveWebcastGiftsResponse500 | RetrieveWebcastGiftsResponse503
    """

    return sync_detailed(
        client=client,
        region=region,
        webcast_language=webcast_language,
        redirect=redirect,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    region: PooledProxyRegion | Unset = UNSET,
    webcast_language: RetrieveWebcastGiftsWebcastLanguage | Unset = RetrieveWebcastGiftsWebcastLanguage.EN,
    redirect: bool | Unset = False,
) -> Response[
    Any
    | WebcastGiftsResponse
    | RetrieveWebcastGiftsResponse429
    | RetrieveWebcastGiftsResponse500
    | RetrieveWebcastGiftsResponse503
]:
    """Retrieve Webcast gifts for a given region

    Args:
        region (PooledProxyRegion | Unset):
        webcast_language (RetrieveWebcastGiftsWebcastLanguage | Unset):  Default:
            RetrieveWebcastGiftsWebcastLanguage.EN.
        redirect (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WebcastGiftsResponse | RetrieveWebcastGiftsResponse429 | RetrieveWebcastGiftsResponse500 | RetrieveWebcastGiftsResponse503]
    """

    kwargs = _get_kwargs(
        region=region,
        webcast_language=webcast_language,
        redirect=redirect,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    region: PooledProxyRegion | Unset = UNSET,
    webcast_language: RetrieveWebcastGiftsWebcastLanguage | Unset = RetrieveWebcastGiftsWebcastLanguage.EN,
    redirect: bool | Unset = False,
) -> (
    Any
    | WebcastGiftsResponse
    | RetrieveWebcastGiftsResponse429
    | RetrieveWebcastGiftsResponse500
    | RetrieveWebcastGiftsResponse503
    | None
):
    """Retrieve Webcast gifts for a given region

    Args:
        region (PooledProxyRegion | Unset):
        webcast_language (RetrieveWebcastGiftsWebcastLanguage | Unset):  Default:
            RetrieveWebcastGiftsWebcastLanguage.EN.
        redirect (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WebcastGiftsResponse | RetrieveWebcastGiftsResponse429 | RetrieveWebcastGiftsResponse500 | RetrieveWebcastGiftsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            region=region,
            webcast_language=webcast_language,
            redirect=redirect,
        )
    ).parsed

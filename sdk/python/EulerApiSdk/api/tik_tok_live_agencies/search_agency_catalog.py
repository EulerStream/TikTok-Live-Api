from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agency_catalog_search_response import AgencyCatalogSearchResponse
from ...models.search_agency_catalog_response_429 import SearchAgencyCatalogResponse429
from ...models.search_agency_catalog_response_500 import SearchAgencyCatalogResponse500
from ...models.search_agency_catalog_response_503 import SearchAgencyCatalogResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str,
    page: float | Unset = 1.0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["query"] = query

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/agencies/catalog/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AgencyCatalogSearchResponse
    | SearchAgencyCatalogResponse429
    | SearchAgencyCatalogResponse500
    | SearchAgencyCatalogResponse503
    | None
):
    if response.status_code == 200:
        response_200 = AgencyCatalogSearchResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = SearchAgencyCatalogResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = SearchAgencyCatalogResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = SearchAgencyCatalogResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AgencyCatalogSearchResponse
    | SearchAgencyCatalogResponse429
    | SearchAgencyCatalogResponse500
    | SearchAgencyCatalogResponse503
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
    page: float | Unset = 1.0,
) -> Response[
    AgencyCatalogSearchResponse
    | SearchAgencyCatalogResponse429
    | SearchAgencyCatalogResponse500
    | SearchAgencyCatalogResponse503
]:
    """Search the TikTok LIVE agency catalog by agency name.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        query (str):
        page (float | Unset):  Default: 1.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgencyCatalogSearchResponse | SearchAgencyCatalogResponse429 | SearchAgencyCatalogResponse500 | SearchAgencyCatalogResponse503]
    """

    kwargs = _get_kwargs(
        query=query,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    query: str,
    page: float | Unset = 1.0,
) -> (
    AgencyCatalogSearchResponse
    | SearchAgencyCatalogResponse429
    | SearchAgencyCatalogResponse500
    | SearchAgencyCatalogResponse503
    | None
):
    """Search the TikTok LIVE agency catalog by agency name.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        query (str):
        page (float | Unset):  Default: 1.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgencyCatalogSearchResponse | SearchAgencyCatalogResponse429 | SearchAgencyCatalogResponse500 | SearchAgencyCatalogResponse503
    """

    return sync_detailed(
        client=client,
        query=query,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    query: str,
    page: float | Unset = 1.0,
) -> Response[
    AgencyCatalogSearchResponse
    | SearchAgencyCatalogResponse429
    | SearchAgencyCatalogResponse500
    | SearchAgencyCatalogResponse503
]:
    """Search the TikTok LIVE agency catalog by agency name.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        query (str):
        page (float | Unset):  Default: 1.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgencyCatalogSearchResponse | SearchAgencyCatalogResponse429 | SearchAgencyCatalogResponse500 | SearchAgencyCatalogResponse503]
    """

    kwargs = _get_kwargs(
        query=query,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    query: str,
    page: float | Unset = 1.0,
) -> (
    AgencyCatalogSearchResponse
    | SearchAgencyCatalogResponse429
    | SearchAgencyCatalogResponse500
    | SearchAgencyCatalogResponse503
    | None
):
    """Search the TikTok LIVE agency catalog by agency name.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        query (str):
        page (float | Unset):  Default: 1.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgencyCatalogSearchResponse | SearchAgencyCatalogResponse429 | SearchAgencyCatalogResponse500 | SearchAgencyCatalogResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            page=page,
        )
    ).parsed

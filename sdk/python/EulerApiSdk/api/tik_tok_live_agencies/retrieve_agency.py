from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agency_catalog_entry_response import AgencyCatalogEntryResponse
from ...models.retrieve_agency_response_429 import RetrieveAgencyResponse429
from ...models.retrieve_agency_response_500 import RetrieveAgencyResponse500
from ...models.retrieve_agency_response_503 import RetrieveAgencyResponse503
from ...types import Response


def _get_kwargs(
    agency_id: float,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/agencies/catalog/{agency_id}".format(
            agency_id=quote(str(agency_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AgencyCatalogEntryResponse
    | RetrieveAgencyResponse429
    | RetrieveAgencyResponse500
    | RetrieveAgencyResponse503
    | None
):
    if response.status_code == 200:
        response_200 = AgencyCatalogEntryResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveAgencyResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveAgencyResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RetrieveAgencyResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AgencyCatalogEntryResponse | RetrieveAgencyResponse429 | RetrieveAgencyResponse500 | RetrieveAgencyResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agency_id: float,
    *,
    client: AuthenticatedClient,
) -> Response[
    AgencyCatalogEntryResponse | RetrieveAgencyResponse429 | RetrieveAgencyResponse500 | RetrieveAgencyResponse503
]:
    """Retrieve a single TikTok LIVE agency by its numeric catalog id.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        agency_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgencyCatalogEntryResponse | RetrieveAgencyResponse429 | RetrieveAgencyResponse500 | RetrieveAgencyResponse503]
    """

    kwargs = _get_kwargs(
        agency_id=agency_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agency_id: float,
    *,
    client: AuthenticatedClient,
) -> (
    AgencyCatalogEntryResponse
    | RetrieveAgencyResponse429
    | RetrieveAgencyResponse500
    | RetrieveAgencyResponse503
    | None
):
    """Retrieve a single TikTok LIVE agency by its numeric catalog id.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        agency_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgencyCatalogEntryResponse | RetrieveAgencyResponse429 | RetrieveAgencyResponse500 | RetrieveAgencyResponse503
    """

    return sync_detailed(
        agency_id=agency_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    agency_id: float,
    *,
    client: AuthenticatedClient,
) -> Response[
    AgencyCatalogEntryResponse | RetrieveAgencyResponse429 | RetrieveAgencyResponse500 | RetrieveAgencyResponse503
]:
    """Retrieve a single TikTok LIVE agency by its numeric catalog id.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        agency_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgencyCatalogEntryResponse | RetrieveAgencyResponse429 | RetrieveAgencyResponse500 | RetrieveAgencyResponse503]
    """

    kwargs = _get_kwargs(
        agency_id=agency_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agency_id: float,
    *,
    client: AuthenticatedClient,
) -> (
    AgencyCatalogEntryResponse
    | RetrieveAgencyResponse429
    | RetrieveAgencyResponse500
    | RetrieveAgencyResponse503
    | None
):
    """Retrieve a single TikTok LIVE agency by its numeric catalog id.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        agency_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgencyCatalogEntryResponse | RetrieveAgencyResponse429 | RetrieveAgencyResponse500 | RetrieveAgencyResponse503
    """

    return (
        await asyncio_detailed(
            agency_id=agency_id,
            client=client,
        )
    ).parsed

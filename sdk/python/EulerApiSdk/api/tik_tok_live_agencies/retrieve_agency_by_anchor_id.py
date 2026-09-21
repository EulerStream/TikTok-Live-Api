from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agency_catalog_entry_response import AgencyCatalogEntryResponse
from ...models.retrieve_agency_by_anchor_id_response_429 import RetrieveAgencyByAnchorIdResponse429
from ...models.retrieve_agency_by_anchor_id_response_500 import RetrieveAgencyByAnchorIdResponse500
from ...models.retrieve_agency_by_anchor_id_response_503 import RetrieveAgencyByAnchorIdResponse503
from ...types import Response


def _get_kwargs(
    anchor_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/agencies/catalog/anchors/{anchor_id}".format(
            anchor_id=quote(str(anchor_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AgencyCatalogEntryResponse
    | RetrieveAgencyByAnchorIdResponse429
    | RetrieveAgencyByAnchorIdResponse500
    | RetrieveAgencyByAnchorIdResponse503
    | None
):
    if response.status_code == 200:
        response_200 = AgencyCatalogEntryResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveAgencyByAnchorIdResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveAgencyByAnchorIdResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RetrieveAgencyByAnchorIdResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AgencyCatalogEntryResponse
    | RetrieveAgencyByAnchorIdResponse429
    | RetrieveAgencyByAnchorIdResponse500
    | RetrieveAgencyByAnchorIdResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    anchor_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    AgencyCatalogEntryResponse
    | RetrieveAgencyByAnchorIdResponse429
    | RetrieveAgencyByAnchorIdResponse500
    | RetrieveAgencyByAnchorIdResponse503
]:
    """Reverse-look up a TikTok LIVE agency by the numeric TikTok user id of its linked creator (anchor).

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        anchor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgencyCatalogEntryResponse | RetrieveAgencyByAnchorIdResponse429 | RetrieveAgencyByAnchorIdResponse500 | RetrieveAgencyByAnchorIdResponse503]
    """

    kwargs = _get_kwargs(
        anchor_id=anchor_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    anchor_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    AgencyCatalogEntryResponse
    | RetrieveAgencyByAnchorIdResponse429
    | RetrieveAgencyByAnchorIdResponse500
    | RetrieveAgencyByAnchorIdResponse503
    | None
):
    """Reverse-look up a TikTok LIVE agency by the numeric TikTok user id of its linked creator (anchor).

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        anchor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgencyCatalogEntryResponse | RetrieveAgencyByAnchorIdResponse429 | RetrieveAgencyByAnchorIdResponse500 | RetrieveAgencyByAnchorIdResponse503
    """

    return sync_detailed(
        anchor_id=anchor_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    anchor_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    AgencyCatalogEntryResponse
    | RetrieveAgencyByAnchorIdResponse429
    | RetrieveAgencyByAnchorIdResponse500
    | RetrieveAgencyByAnchorIdResponse503
]:
    """Reverse-look up a TikTok LIVE agency by the numeric TikTok user id of its linked creator (anchor).

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        anchor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgencyCatalogEntryResponse | RetrieveAgencyByAnchorIdResponse429 | RetrieveAgencyByAnchorIdResponse500 | RetrieveAgencyByAnchorIdResponse503]
    """

    kwargs = _get_kwargs(
        anchor_id=anchor_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    anchor_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    AgencyCatalogEntryResponse
    | RetrieveAgencyByAnchorIdResponse429
    | RetrieveAgencyByAnchorIdResponse500
    | RetrieveAgencyByAnchorIdResponse503
    | None
):
    """Reverse-look up a TikTok LIVE agency by the numeric TikTok user id of its linked creator (anchor).

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        anchor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgencyCatalogEntryResponse | RetrieveAgencyByAnchorIdResponse429 | RetrieveAgencyByAnchorIdResponse500 | RetrieveAgencyByAnchorIdResponse503
    """

    return (
        await asyncio_detailed(
            anchor_id=anchor_id,
            client=client,
        )
    ).parsed

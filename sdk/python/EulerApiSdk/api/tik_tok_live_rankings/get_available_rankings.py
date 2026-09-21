from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.available_rankings_response import AvailableRankingsResponse
from ...models.get_available_rankings_response_429 import GetAvailableRankingsResponse429
from ...models.get_available_rankings_response_500 import GetAvailableRankingsResponse500
from ...models.get_available_rankings_response_503 import GetAvailableRankingsResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/rankings/catalog/leaderboards",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AvailableRankingsResponse
    | GetAvailableRankingsResponse429
    | GetAvailableRankingsResponse500
    | GetAvailableRankingsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = AvailableRankingsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = GetAvailableRankingsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetAvailableRankingsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetAvailableRankingsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AvailableRankingsResponse
    | GetAvailableRankingsResponse429
    | GetAvailableRankingsResponse500
    | GetAvailableRankingsResponse503
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
) -> Response[
    AvailableRankingsResponse
    | GetAvailableRankingsResponse429
    | GetAvailableRankingsResponse500
    | GetAvailableRankingsResponse503
]:
    """Returns the available ranking types and league tiers for each tracked region,
    based on each leaderboard's most recent day of data in the ranking service
    (boards with no data for several days age out of the catalog).

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailableRankingsResponse | GetAvailableRankingsResponse429 | GetAvailableRankingsResponse500 | GetAvailableRankingsResponse503]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> (
    AvailableRankingsResponse
    | GetAvailableRankingsResponse429
    | GetAvailableRankingsResponse500
    | GetAvailableRankingsResponse503
    | None
):
    """Returns the available ranking types and league tiers for each tracked region,
    based on each leaderboard's most recent day of data in the ranking service
    (boards with no data for several days age out of the catalog).

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AvailableRankingsResponse | GetAvailableRankingsResponse429 | GetAvailableRankingsResponse500 | GetAvailableRankingsResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    AvailableRankingsResponse
    | GetAvailableRankingsResponse429
    | GetAvailableRankingsResponse500
    | GetAvailableRankingsResponse503
]:
    """Returns the available ranking types and league tiers for each tracked region,
    based on each leaderboard's most recent day of data in the ranking service
    (boards with no data for several days age out of the catalog).

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailableRankingsResponse | GetAvailableRankingsResponse429 | GetAvailableRankingsResponse500 | GetAvailableRankingsResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> (
    AvailableRankingsResponse
    | GetAvailableRankingsResponse429
    | GetAvailableRankingsResponse500
    | GetAvailableRankingsResponse503
    | None
):
    """Returns the available ranking types and league tiers for each tracked region,
    based on each leaderboard's most recent day of data in the ranking service
    (boards with no data for several days age out of the catalog).

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AvailableRankingsResponse | GetAvailableRankingsResponse429 | GetAvailableRankingsResponse500 | GetAvailableRankingsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

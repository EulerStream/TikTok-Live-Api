from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.available_dates_response import AvailableDatesResponse
from ...models.available_webcast_rank_name import AvailableWebcastRankName
from ...models.get_available_dates_response_429 import GetAvailableDatesResponse429
from ...models.get_available_dates_response_500 import GetAvailableDatesResponse500
from ...models.get_available_dates_response_503 import GetAvailableDatesResponse503
from ...models.ranking_league_name import RankingLeagueName
from ...types import UNSET, Response, Unset


def _get_kwargs(
    region: str,
    rank_name: AvailableWebcastRankName,
    *,
    league: RankingLeagueName | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_league: str | Unset = UNSET
    if not isinstance(league, Unset):
        json_league = league.value

    params["league"] = json_league

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/rankings/catalog/leaderboards/{region}/{rank_name}/dates".format(
            region=quote(str(region), safe=""),
            rank_name=quote(str(rank_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AvailableDatesResponse
    | GetAvailableDatesResponse429
    | GetAvailableDatesResponse500
    | GetAvailableDatesResponse503
    | None
):
    if response.status_code == 200:
        response_200 = AvailableDatesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = GetAvailableDatesResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetAvailableDatesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetAvailableDatesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AvailableDatesResponse | GetAvailableDatesResponse429 | GetAvailableDatesResponse500 | GetAvailableDatesResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    region: str,
    rank_name: AvailableWebcastRankName,
    *,
    client: AuthenticatedClient,
    league: RankingLeagueName | Unset = UNSET,
) -> Response[
    AvailableDatesResponse | GetAvailableDatesResponse429 | GetAvailableDatesResponse500 | GetAvailableDatesResponse503
]:
    """Retrieve the list of dates that have leaderboard data for a given rank type and region.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        region (str):
        rank_name (AvailableWebcastRankName):
        league (RankingLeagueName | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailableDatesResponse | GetAvailableDatesResponse429 | GetAvailableDatesResponse500 | GetAvailableDatesResponse503]
    """

    kwargs = _get_kwargs(
        region=region,
        rank_name=rank_name,
        league=league,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    region: str,
    rank_name: AvailableWebcastRankName,
    *,
    client: AuthenticatedClient,
    league: RankingLeagueName | Unset = UNSET,
) -> (
    AvailableDatesResponse
    | GetAvailableDatesResponse429
    | GetAvailableDatesResponse500
    | GetAvailableDatesResponse503
    | None
):
    """Retrieve the list of dates that have leaderboard data for a given rank type and region.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        region (str):
        rank_name (AvailableWebcastRankName):
        league (RankingLeagueName | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AvailableDatesResponse | GetAvailableDatesResponse429 | GetAvailableDatesResponse500 | GetAvailableDatesResponse503
    """

    return sync_detailed(
        region=region,
        rank_name=rank_name,
        client=client,
        league=league,
    ).parsed


async def asyncio_detailed(
    region: str,
    rank_name: AvailableWebcastRankName,
    *,
    client: AuthenticatedClient,
    league: RankingLeagueName | Unset = UNSET,
) -> Response[
    AvailableDatesResponse | GetAvailableDatesResponse429 | GetAvailableDatesResponse500 | GetAvailableDatesResponse503
]:
    """Retrieve the list of dates that have leaderboard data for a given rank type and region.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        region (str):
        rank_name (AvailableWebcastRankName):
        league (RankingLeagueName | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailableDatesResponse | GetAvailableDatesResponse429 | GetAvailableDatesResponse500 | GetAvailableDatesResponse503]
    """

    kwargs = _get_kwargs(
        region=region,
        rank_name=rank_name,
        league=league,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    region: str,
    rank_name: AvailableWebcastRankName,
    *,
    client: AuthenticatedClient,
    league: RankingLeagueName | Unset = UNSET,
) -> (
    AvailableDatesResponse
    | GetAvailableDatesResponse429
    | GetAvailableDatesResponse500
    | GetAvailableDatesResponse503
    | None
):
    """Retrieve the list of dates that have leaderboard data for a given rank type and region.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        region (str):
        rank_name (AvailableWebcastRankName):
        league (RankingLeagueName | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AvailableDatesResponse | GetAvailableDatesResponse429 | GetAvailableDatesResponse500 | GetAvailableDatesResponse503
    """

    return (
        await asyncio_detailed(
            region=region,
            rank_name=rank_name,
            client=client,
            league=league,
        )
    ).parsed

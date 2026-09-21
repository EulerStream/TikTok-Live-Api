import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.available_webcast_rank_name import AvailableWebcastRankName
from ...models.get_leaderboard_response_429 import GetLeaderboardResponse429
from ...models.get_leaderboard_response_500 import GetLeaderboardResponse500
from ...models.get_leaderboard_response_503 import GetLeaderboardResponse503
from ...models.leaderboard_response import LeaderboardResponse
from ...models.ranking_league_name import RankingLeagueName
from ...types import UNSET, Response, Unset


def _get_kwargs(
    region: str,
    rank_name: AvailableWebcastRankName,
    *,
    date: datetime.datetime | Unset = UNSET,
    league: RankingLeagueName | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date: str | Unset = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    json_league: str | Unset = UNSET
    if not isinstance(league, Unset):
        json_league = league.value

    params["league"] = json_league

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/rankings/catalog/leaderboards/{region}/{rank_name}".format(
            region=quote(str(region), safe=""),
            rank_name=quote(str(rank_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetLeaderboardResponse429 | GetLeaderboardResponse500 | GetLeaderboardResponse503 | LeaderboardResponse | None:
    if response.status_code == 200:
        response_200 = LeaderboardResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = GetLeaderboardResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetLeaderboardResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetLeaderboardResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetLeaderboardResponse429 | GetLeaderboardResponse500 | GetLeaderboardResponse503 | LeaderboardResponse]:
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
    date: datetime.datetime | Unset = UNSET,
    league: RankingLeagueName | Unset = UNSET,
) -> Response[GetLeaderboardResponse429 | GetLeaderboardResponse500 | GetLeaderboardResponse503 | LeaderboardResponse]:
    """Retrieve the most recent leaderboard snapshot for a given rank type, region, and date.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        region (str):
        rank_name (AvailableWebcastRankName):
        date (datetime.datetime | Unset):
        league (RankingLeagueName | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLeaderboardResponse429 | GetLeaderboardResponse500 | GetLeaderboardResponse503 | LeaderboardResponse]
    """

    kwargs = _get_kwargs(
        region=region,
        rank_name=rank_name,
        date=date,
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
    date: datetime.datetime | Unset = UNSET,
    league: RankingLeagueName | Unset = UNSET,
) -> GetLeaderboardResponse429 | GetLeaderboardResponse500 | GetLeaderboardResponse503 | LeaderboardResponse | None:
    """Retrieve the most recent leaderboard snapshot for a given rank type, region, and date.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        region (str):
        rank_name (AvailableWebcastRankName):
        date (datetime.datetime | Unset):
        league (RankingLeagueName | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLeaderboardResponse429 | GetLeaderboardResponse500 | GetLeaderboardResponse503 | LeaderboardResponse
    """

    return sync_detailed(
        region=region,
        rank_name=rank_name,
        client=client,
        date=date,
        league=league,
    ).parsed


async def asyncio_detailed(
    region: str,
    rank_name: AvailableWebcastRankName,
    *,
    client: AuthenticatedClient,
    date: datetime.datetime | Unset = UNSET,
    league: RankingLeagueName | Unset = UNSET,
) -> Response[GetLeaderboardResponse429 | GetLeaderboardResponse500 | GetLeaderboardResponse503 | LeaderboardResponse]:
    """Retrieve the most recent leaderboard snapshot for a given rank type, region, and date.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        region (str):
        rank_name (AvailableWebcastRankName):
        date (datetime.datetime | Unset):
        league (RankingLeagueName | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLeaderboardResponse429 | GetLeaderboardResponse500 | GetLeaderboardResponse503 | LeaderboardResponse]
    """

    kwargs = _get_kwargs(
        region=region,
        rank_name=rank_name,
        date=date,
        league=league,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    region: str,
    rank_name: AvailableWebcastRankName,
    *,
    client: AuthenticatedClient,
    date: datetime.datetime | Unset = UNSET,
    league: RankingLeagueName | Unset = UNSET,
) -> GetLeaderboardResponse429 | GetLeaderboardResponse500 | GetLeaderboardResponse503 | LeaderboardResponse | None:
    """Retrieve the most recent leaderboard snapshot for a given rank type, region, and date.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        region (str):
        rank_name (AvailableWebcastRankName):
        date (datetime.datetime | Unset):
        league (RankingLeagueName | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLeaderboardResponse429 | GetLeaderboardResponse500 | GetLeaderboardResponse503 | LeaderboardResponse
    """

    return (
        await asyncio_detailed(
            region=region,
            rank_name=rank_name,
            client=client,
            date=date,
            league=league,
        )
    ).parsed

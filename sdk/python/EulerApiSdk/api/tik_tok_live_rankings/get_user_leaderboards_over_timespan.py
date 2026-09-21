import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_user_leaderboards_over_timespan_response_429 import GetUserLeaderboardsOverTimespanResponse429
from ...models.get_user_leaderboards_over_timespan_response_500 import GetUserLeaderboardsOverTimespanResponse500
from ...models.get_user_leaderboards_over_timespan_response_503 import GetUserLeaderboardsOverTimespanResponse503
from ...models.user_leaderboards_response import UserLeaderboardsResponse
from ...types import UNSET, Response


def _get_kwargs(
    anchor_id: str,
    *,
    from_: datetime.datetime,
    to: datetime.datetime,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to = to.isoformat()
    params["to"] = json_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/rankings/catalog/anchors/{anchor_id}/rank_names".format(
            anchor_id=quote(str(anchor_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetUserLeaderboardsOverTimespanResponse429
    | GetUserLeaderboardsOverTimespanResponse500
    | GetUserLeaderboardsOverTimespanResponse503
    | UserLeaderboardsResponse
    | None
):
    if response.status_code == 200:
        response_200 = UserLeaderboardsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = GetUserLeaderboardsOverTimespanResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetUserLeaderboardsOverTimespanResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetUserLeaderboardsOverTimespanResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetUserLeaderboardsOverTimespanResponse429
    | GetUserLeaderboardsOverTimespanResponse500
    | GetUserLeaderboardsOverTimespanResponse503
    | UserLeaderboardsResponse
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
    from_: datetime.datetime,
    to: datetime.datetime,
) -> Response[
    GetUserLeaderboardsOverTimespanResponse429
    | GetUserLeaderboardsOverTimespanResponse500
    | GetUserLeaderboardsOverTimespanResponse503
    | UserLeaderboardsResponse
]:
    """Discovery: The leaderboards a creator appears on within a UTC date range,
    returned as a map of region to rank_types.

    Rate limited to 30 requests/min. Does NOT count towards normal API limits.

    Args:
        anchor_id (str):
        from_ (datetime.datetime):
        to (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserLeaderboardsOverTimespanResponse429 | GetUserLeaderboardsOverTimespanResponse500 | GetUserLeaderboardsOverTimespanResponse503 | UserLeaderboardsResponse]
    """

    kwargs = _get_kwargs(
        anchor_id=anchor_id,
        from_=from_,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    anchor_id: str,
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime,
    to: datetime.datetime,
) -> (
    GetUserLeaderboardsOverTimespanResponse429
    | GetUserLeaderboardsOverTimespanResponse500
    | GetUserLeaderboardsOverTimespanResponse503
    | UserLeaderboardsResponse
    | None
):
    """Discovery: The leaderboards a creator appears on within a UTC date range,
    returned as a map of region to rank_types.

    Rate limited to 30 requests/min. Does NOT count towards normal API limits.

    Args:
        anchor_id (str):
        from_ (datetime.datetime):
        to (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserLeaderboardsOverTimespanResponse429 | GetUserLeaderboardsOverTimespanResponse500 | GetUserLeaderboardsOverTimespanResponse503 | UserLeaderboardsResponse
    """

    return sync_detailed(
        anchor_id=anchor_id,
        client=client,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    anchor_id: str,
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime,
    to: datetime.datetime,
) -> Response[
    GetUserLeaderboardsOverTimespanResponse429
    | GetUserLeaderboardsOverTimespanResponse500
    | GetUserLeaderboardsOverTimespanResponse503
    | UserLeaderboardsResponse
]:
    """Discovery: The leaderboards a creator appears on within a UTC date range,
    returned as a map of region to rank_types.

    Rate limited to 30 requests/min. Does NOT count towards normal API limits.

    Args:
        anchor_id (str):
        from_ (datetime.datetime):
        to (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserLeaderboardsOverTimespanResponse429 | GetUserLeaderboardsOverTimespanResponse500 | GetUserLeaderboardsOverTimespanResponse503 | UserLeaderboardsResponse]
    """

    kwargs = _get_kwargs(
        anchor_id=anchor_id,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    anchor_id: str,
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime,
    to: datetime.datetime,
) -> (
    GetUserLeaderboardsOverTimespanResponse429
    | GetUserLeaderboardsOverTimespanResponse500
    | GetUserLeaderboardsOverTimespanResponse503
    | UserLeaderboardsResponse
    | None
):
    """Discovery: The leaderboards a creator appears on within a UTC date range,
    returned as a map of region to rank_types.

    Rate limited to 30 requests/min. Does NOT count towards normal API limits.

    Args:
        anchor_id (str):
        from_ (datetime.datetime):
        to (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserLeaderboardsOverTimespanResponse429 | GetUserLeaderboardsOverTimespanResponse500 | GetUserLeaderboardsOverTimespanResponse503 | UserLeaderboardsResponse
    """

    return (
        await asyncio_detailed(
            anchor_id=anchor_id,
            client=client,
            from_=from_,
            to=to,
        )
    ).parsed

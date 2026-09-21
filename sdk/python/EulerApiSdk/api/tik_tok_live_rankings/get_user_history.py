import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.available_webcast_rank_name import AvailableWebcastRankName
from ...models.get_user_history_response_429 import GetUserHistoryResponse429
from ...models.get_user_history_response_500 import GetUserHistoryResponse500
from ...models.get_user_history_response_503 import GetUserHistoryResponse503
from ...models.user_history_response import UserHistoryResponse
from ...types import UNSET, Response


def _get_kwargs(
    region: str,
    rank_name: AvailableWebcastRankName,
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
        "url": "/webcast/rankings/catalog/leaderboards/{region}/{rank_name}/anchors/{anchor_id}/history".format(
            region=quote(str(region), safe=""),
            rank_name=quote(str(rank_name), safe=""),
            anchor_id=quote(str(anchor_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetUserHistoryResponse429 | GetUserHistoryResponse500 | GetUserHistoryResponse503 | UserHistoryResponse | None:
    if response.status_code == 200:
        response_200 = UserHistoryResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = GetUserHistoryResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetUserHistoryResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetUserHistoryResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetUserHistoryResponse429 | GetUserHistoryResponse500 | GetUserHistoryResponse503 | UserHistoryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    region: str,
    rank_name: AvailableWebcastRankName,
    anchor_id: str,
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime,
    to: datetime.datetime,
) -> Response[GetUserHistoryResponse429 | GetUserHistoryResponse500 | GetUserHistoryResponse503 | UserHistoryResponse]:
    """Retrieve a creator's daily standing on a given board over a UTC date range,
    oldest first.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        region (str):
        rank_name (AvailableWebcastRankName):
        anchor_id (str):
        from_ (datetime.datetime):
        to (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserHistoryResponse429 | GetUserHistoryResponse500 | GetUserHistoryResponse503 | UserHistoryResponse]
    """

    kwargs = _get_kwargs(
        region=region,
        rank_name=rank_name,
        anchor_id=anchor_id,
        from_=from_,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    region: str,
    rank_name: AvailableWebcastRankName,
    anchor_id: str,
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime,
    to: datetime.datetime,
) -> GetUserHistoryResponse429 | GetUserHistoryResponse500 | GetUserHistoryResponse503 | UserHistoryResponse | None:
    """Retrieve a creator's daily standing on a given board over a UTC date range,
    oldest first.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        region (str):
        rank_name (AvailableWebcastRankName):
        anchor_id (str):
        from_ (datetime.datetime):
        to (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserHistoryResponse429 | GetUserHistoryResponse500 | GetUserHistoryResponse503 | UserHistoryResponse
    """

    return sync_detailed(
        region=region,
        rank_name=rank_name,
        anchor_id=anchor_id,
        client=client,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    region: str,
    rank_name: AvailableWebcastRankName,
    anchor_id: str,
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime,
    to: datetime.datetime,
) -> Response[GetUserHistoryResponse429 | GetUserHistoryResponse500 | GetUserHistoryResponse503 | UserHistoryResponse]:
    """Retrieve a creator's daily standing on a given board over a UTC date range,
    oldest first.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        region (str):
        rank_name (AvailableWebcastRankName):
        anchor_id (str):
        from_ (datetime.datetime):
        to (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserHistoryResponse429 | GetUserHistoryResponse500 | GetUserHistoryResponse503 | UserHistoryResponse]
    """

    kwargs = _get_kwargs(
        region=region,
        rank_name=rank_name,
        anchor_id=anchor_id,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    region: str,
    rank_name: AvailableWebcastRankName,
    anchor_id: str,
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime,
    to: datetime.datetime,
) -> GetUserHistoryResponse429 | GetUserHistoryResponse500 | GetUserHistoryResponse503 | UserHistoryResponse | None:
    """Retrieve a creator's daily standing on a given board over a UTC date range,
    oldest first.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        region (str):
        rank_name (AvailableWebcastRankName):
        anchor_id (str):
        from_ (datetime.datetime):
        to (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserHistoryResponse429 | GetUserHistoryResponse500 | GetUserHistoryResponse503 | UserHistoryResponse
    """

    return (
        await asyncio_detailed(
            region=region,
            rank_name=rank_name,
            anchor_id=anchor_id,
            client=client,
            from_=from_,
            to=to,
        )
    ).parsed

from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_user_response import SearchUserResponse
from ...models.search_user_response_429 import SearchUserResponse429
from ...models.search_user_response_500 import SearchUserResponse500
from ...models.search_user_response_503 import SearchUserResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str,
    limit: float | Unset = 1.0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["query"] = query

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/rankings/catalog/anchors/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SearchUserResponse | SearchUserResponse429 | SearchUserResponse500 | SearchUserResponse503 | None:
    if response.status_code == 200:
        response_200 = SearchUserResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = SearchUserResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = SearchUserResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = SearchUserResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SearchUserResponse | SearchUserResponse429 | SearchUserResponse500 | SearchUserResponse503]:
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
    limit: float | Unset = 1.0,
) -> Response[SearchUserResponse | SearchUserResponse429 | SearchUserResponse500 | SearchUserResponse503]:
    """Search for users in the rankings data by username or nickname prefix.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        query (str):
        limit (float | Unset):  Default: 1.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchUserResponse | SearchUserResponse429 | SearchUserResponse500 | SearchUserResponse503]
    """

    kwargs = _get_kwargs(
        query=query,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    query: str,
    limit: float | Unset = 1.0,
) -> SearchUserResponse | SearchUserResponse429 | SearchUserResponse500 | SearchUserResponse503 | None:
    """Search for users in the rankings data by username or nickname prefix.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        query (str):
        limit (float | Unset):  Default: 1.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchUserResponse | SearchUserResponse429 | SearchUserResponse500 | SearchUserResponse503
    """

    return sync_detailed(
        client=client,
        query=query,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    query: str,
    limit: float | Unset = 1.0,
) -> Response[SearchUserResponse | SearchUserResponse429 | SearchUserResponse500 | SearchUserResponse503]:
    """Search for users in the rankings data by username or nickname prefix.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        query (str):
        limit (float | Unset):  Default: 1.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchUserResponse | SearchUserResponse429 | SearchUserResponse500 | SearchUserResponse503]
    """

    kwargs = _get_kwargs(
        query=query,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    query: str,
    limit: float | Unset = 1.0,
) -> SearchUserResponse | SearchUserResponse429 | SearchUserResponse500 | SearchUserResponse503 | None:
    """Search for users in the rankings data by username or nickname prefix.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        query (str):
        limit (float | Unset):  Default: 1.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchUserResponse | SearchUserResponse429 | SearchUserResponse500 | SearchUserResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            limit=limit,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_web_sockets_response_429 import GetWebSocketsResponse429
from ...models.get_web_sockets_response_500 import GetWebSocketsResponse500
from ...models.get_web_sockets_response_503 import GetWebSocketsResponse503
from ...models.retrieve_web_sockets_route_response import RetrieveWebSocketsRouteResponse
from ...types import Response


def _get_kwargs(
    account_id: float,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/websockets/{account_id}".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetWebSocketsResponse429
    | GetWebSocketsResponse500
    | GetWebSocketsResponse503
    | RetrieveWebSocketsRouteResponse
    | None
):
    if response.status_code == 200:
        response_200 = RetrieveWebSocketsRouteResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = GetWebSocketsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetWebSocketsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetWebSocketsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetWebSocketsResponse429 | GetWebSocketsResponse500 | GetWebSocketsResponse503 | RetrieveWebSocketsRouteResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: float,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetWebSocketsResponse429 | GetWebSocketsResponse500 | GetWebSocketsResponse503 | RetrieveWebSocketsRouteResponse
]:
    """Retrieve the currently connected WebSocket clients for your account.

    Args:
        account_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWebSocketsResponse429 | GetWebSocketsResponse500 | GetWebSocketsResponse503 | RetrieveWebSocketsRouteResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: float,
    *,
    client: AuthenticatedClient,
) -> (
    GetWebSocketsResponse429
    | GetWebSocketsResponse500
    | GetWebSocketsResponse503
    | RetrieveWebSocketsRouteResponse
    | None
):
    """Retrieve the currently connected WebSocket clients for your account.

    Args:
        account_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWebSocketsResponse429 | GetWebSocketsResponse500 | GetWebSocketsResponse503 | RetrieveWebSocketsRouteResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: float,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetWebSocketsResponse429 | GetWebSocketsResponse500 | GetWebSocketsResponse503 | RetrieveWebSocketsRouteResponse
]:
    """Retrieve the currently connected WebSocket clients for your account.

    Args:
        account_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWebSocketsResponse429 | GetWebSocketsResponse500 | GetWebSocketsResponse503 | RetrieveWebSocketsRouteResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: float,
    *,
    client: AuthenticatedClient,
) -> (
    GetWebSocketsResponse429
    | GetWebSocketsResponse500
    | GetWebSocketsResponse503
    | RetrieveWebSocketsRouteResponse
    | None
):
    """Retrieve the currently connected WebSocket clients for your account.

    Args:
        account_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWebSocketsResponse429 | GetWebSocketsResponse500 | GetWebSocketsResponse503 | RetrieveWebSocketsRouteResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
        )
    ).parsed

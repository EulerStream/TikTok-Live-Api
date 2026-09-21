from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_web_socket_route_response import RetrieveWebSocketRouteResponse
from ...models.retrieve_web_socket_state_response_429 import RetrieveWebSocketStateResponse429
from ...models.retrieve_web_socket_state_response_500 import RetrieveWebSocketStateResponse500
from ...models.retrieve_web_socket_state_response_503 import RetrieveWebSocketStateResponse503
from ...types import Response


def _get_kwargs(
    account_id: float,
    websocket_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/websockets/{account_id}/{websocket_id}".format(
            account_id=quote(str(account_id), safe=""),
            websocket_id=quote(str(websocket_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RetrieveWebSocketRouteResponse
    | RetrieveWebSocketStateResponse429
    | RetrieveWebSocketStateResponse500
    | RetrieveWebSocketStateResponse503
    | None
):
    if response.status_code == 200:
        response_200 = RetrieveWebSocketRouteResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveWebSocketStateResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveWebSocketStateResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RetrieveWebSocketStateResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RetrieveWebSocketRouteResponse
    | RetrieveWebSocketStateResponse429
    | RetrieveWebSocketStateResponse500
    | RetrieveWebSocketStateResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: float,
    websocket_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    RetrieveWebSocketRouteResponse
    | RetrieveWebSocketStateResponse429
    | RetrieveWebSocketStateResponse500
    | RetrieveWebSocketStateResponse503
]:
    """Retrieve the currently connected WebSocket clients for your account.

    Args:
        account_id (float):
        websocket_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveWebSocketRouteResponse | RetrieveWebSocketStateResponse429 | RetrieveWebSocketStateResponse500 | RetrieveWebSocketStateResponse503]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        websocket_id=websocket_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: float,
    websocket_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    RetrieveWebSocketRouteResponse
    | RetrieveWebSocketStateResponse429
    | RetrieveWebSocketStateResponse500
    | RetrieveWebSocketStateResponse503
    | None
):
    """Retrieve the currently connected WebSocket clients for your account.

    Args:
        account_id (float):
        websocket_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveWebSocketRouteResponse | RetrieveWebSocketStateResponse429 | RetrieveWebSocketStateResponse500 | RetrieveWebSocketStateResponse503
    """

    return sync_detailed(
        account_id=account_id,
        websocket_id=websocket_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: float,
    websocket_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    RetrieveWebSocketRouteResponse
    | RetrieveWebSocketStateResponse429
    | RetrieveWebSocketStateResponse500
    | RetrieveWebSocketStateResponse503
]:
    """Retrieve the currently connected WebSocket clients for your account.

    Args:
        account_id (float):
        websocket_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveWebSocketRouteResponse | RetrieveWebSocketStateResponse429 | RetrieveWebSocketStateResponse500 | RetrieveWebSocketStateResponse503]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        websocket_id=websocket_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: float,
    websocket_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    RetrieveWebSocketRouteResponse
    | RetrieveWebSocketStateResponse429
    | RetrieveWebSocketStateResponse500
    | RetrieveWebSocketStateResponse503
    | None
):
    """Retrieve the currently connected WebSocket clients for your account.

    Args:
        account_id (float):
        websocket_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveWebSocketRouteResponse | RetrieveWebSocketStateResponse429 | RetrieveWebSocketStateResponse500 | RetrieveWebSocketStateResponse503
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            websocket_id=websocket_id,
            client=client,
        )
    ).parsed

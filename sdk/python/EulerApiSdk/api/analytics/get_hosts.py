from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_hosts_response_429 import GetHostsResponse429
from ...models.get_hosts_response_500 import GetHostsResponse500
from ...models.hosts_response import HostsResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/hosts",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetHostsResponse429 | GetHostsResponse500 | HostsResponse | None:
    if response.status_code == 200:
        response_200 = HostsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = GetHostsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetHostsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetHostsResponse429 | GetHostsResponse500 | HostsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetHostsResponse429 | GetHostsResponse500 | HostsResponse]:
    """Retrieve the list of API hosts (used for horizontal scaling)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetHostsResponse429 | GetHostsResponse500 | HostsResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetHostsResponse429 | GetHostsResponse500 | HostsResponse | None:
    """Retrieve the list of API hosts (used for horizontal scaling)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetHostsResponse429 | GetHostsResponse500 | HostsResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetHostsResponse429 | GetHostsResponse500 | HostsResponse]:
    """Retrieve the list of API hosts (used for horizontal scaling)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetHostsResponse429 | GetHostsResponse500 | HostsResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetHostsResponse429 | GetHostsResponse500 | HostsResponse | None:
    """Retrieve the list of API hosts (used for horizontal scaling)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetHostsResponse429 | GetHostsResponse500 | HostsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

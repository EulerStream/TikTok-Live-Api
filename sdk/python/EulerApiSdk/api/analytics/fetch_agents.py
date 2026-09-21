from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fetch_agents_response_429 import FetchAgentsResponse429
from ...models.fetch_agents_response_500 import FetchAgentsResponse500
from ...models.retrieve_agent_hosts_response import RetrieveAgentHostsResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/agents",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FetchAgentsResponse429 | FetchAgentsResponse500 | RetrieveAgentHostsResponse | None:
    if response.status_code == 200:
        response_200 = RetrieveAgentHostsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = FetchAgentsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = FetchAgentsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FetchAgentsResponse429 | FetchAgentsResponse500 | RetrieveAgentHostsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[FetchAgentsResponse429 | FetchAgentsResponse500 | RetrieveAgentHostsResponse]:
    """Retrieve the currently connected agents

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FetchAgentsResponse429 | FetchAgentsResponse500 | RetrieveAgentHostsResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> FetchAgentsResponse429 | FetchAgentsResponse500 | RetrieveAgentHostsResponse | None:
    """Retrieve the currently connected agents

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FetchAgentsResponse429 | FetchAgentsResponse500 | RetrieveAgentHostsResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[FetchAgentsResponse429 | FetchAgentsResponse500 | RetrieveAgentHostsResponse]:
    """Retrieve the currently connected agents

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FetchAgentsResponse429 | FetchAgentsResponse500 | RetrieveAgentHostsResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> FetchAgentsResponse429 | FetchAgentsResponse500 | RetrieveAgentHostsResponse | None:
    """Retrieve the currently connected agents

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FetchAgentsResponse429 | FetchAgentsResponse500 | RetrieveAgentHostsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

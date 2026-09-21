from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_account_response import RetrieveAccountResponse
from ...models.retrieve_account_self_response_429 import RetrieveAccountSelfResponse429
from ...models.retrieve_account_self_response_500 import RetrieveAccountSelfResponse500
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/me",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RetrieveAccountResponse | RetrieveAccountSelfResponse429 | RetrieveAccountSelfResponse500 | None:
    if response.status_code == 200:
        response_200 = RetrieveAccountResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveAccountSelfResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveAccountSelfResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RetrieveAccountResponse | RetrieveAccountSelfResponse429 | RetrieveAccountSelfResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[RetrieveAccountResponse | RetrieveAccountSelfResponse429 | RetrieveAccountSelfResponse500]:
    """Retrieve an account from the Sign API

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveAccountResponse | RetrieveAccountSelfResponse429 | RetrieveAccountSelfResponse500]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> RetrieveAccountResponse | RetrieveAccountSelfResponse429 | RetrieveAccountSelfResponse500 | None:
    """Retrieve an account from the Sign API

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveAccountResponse | RetrieveAccountSelfResponse429 | RetrieveAccountSelfResponse500
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[RetrieveAccountResponse | RetrieveAccountSelfResponse429 | RetrieveAccountSelfResponse500]:
    """Retrieve an account from the Sign API

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveAccountResponse | RetrieveAccountSelfResponse429 | RetrieveAccountSelfResponse500]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> RetrieveAccountResponse | RetrieveAccountSelfResponse429 | RetrieveAccountSelfResponse500 | None:
    """Retrieve an account from the Sign API

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveAccountResponse | RetrieveAccountSelfResponse429 | RetrieveAccountSelfResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

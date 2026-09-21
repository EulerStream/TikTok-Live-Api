from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_keys_response import ListKeysResponse
from ...models.list_keys_response_429 import ListKeysResponse429
from ...models.list_keys_response_500 import ListKeysResponse500
from ...types import Response


def _get_kwargs(
    account_id: float,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/{account_id}/api_keys/list".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListKeysResponse | ListKeysResponse429 | ListKeysResponse500 | None:
    if response.status_code == 200:
        response_200 = ListKeysResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = ListKeysResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListKeysResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListKeysResponse | ListKeysResponse429 | ListKeysResponse500]:
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
) -> Response[ListKeysResponse | ListKeysResponse429 | ListKeysResponse500]:
    """Retrieve an API key by its key value, name, or ID

    Args:
        account_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListKeysResponse | ListKeysResponse429 | ListKeysResponse500]
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
) -> ListKeysResponse | ListKeysResponse429 | ListKeysResponse500 | None:
    """Retrieve an API key by its key value, name, or ID

    Args:
        account_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListKeysResponse | ListKeysResponse429 | ListKeysResponse500
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: float,
    *,
    client: AuthenticatedClient,
) -> Response[ListKeysResponse | ListKeysResponse429 | ListKeysResponse500]:
    """Retrieve an API key by its key value, name, or ID

    Args:
        account_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListKeysResponse | ListKeysResponse429 | ListKeysResponse500]
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
) -> ListKeysResponse | ListKeysResponse429 | ListKeysResponse500 | None:
    """Retrieve an API key by its key value, name, or ID

    Args:
        account_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListKeysResponse | ListKeysResponse429 | ListKeysResponse500
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
        )
    ).parsed

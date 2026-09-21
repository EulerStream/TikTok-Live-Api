from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_key_payload import CreateKeyPayload
from ...models.create_key_response import CreateKeyResponse
from ...models.create_key_response_429 import CreateKeyResponse429
from ...models.create_key_response_500 import CreateKeyResponse500
from ...types import Response


def _get_kwargs(
    account_id: float,
    *,
    body: CreateKeyPayload,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/accounts/{account_id}/api_keys/create".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateKeyResponse | CreateKeyResponse429 | CreateKeyResponse500 | None:
    if response.status_code == 200:
        response_200 = CreateKeyResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = CreateKeyResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CreateKeyResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateKeyResponse | CreateKeyResponse429 | CreateKeyResponse500]:
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
    body: CreateKeyPayload,
) -> Response[CreateKeyResponse | CreateKeyResponse429 | CreateKeyResponse500]:
    """Create a new API key

    Args:
        account_id (float):
        body (CreateKeyPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateKeyResponse | CreateKeyResponse429 | CreateKeyResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: float,
    *,
    client: AuthenticatedClient,
    body: CreateKeyPayload,
) -> CreateKeyResponse | CreateKeyResponse429 | CreateKeyResponse500 | None:
    """Create a new API key

    Args:
        account_id (float):
        body (CreateKeyPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateKeyResponse | CreateKeyResponse429 | CreateKeyResponse500
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: float,
    *,
    client: AuthenticatedClient,
    body: CreateKeyPayload,
) -> Response[CreateKeyResponse | CreateKeyResponse429 | CreateKeyResponse500]:
    """Create a new API key

    Args:
        account_id (float):
        body (CreateKeyPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateKeyResponse | CreateKeyResponse429 | CreateKeyResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: float,
    *,
    client: AuthenticatedClient,
    body: CreateKeyPayload,
) -> CreateKeyResponse | CreateKeyResponse429 | CreateKeyResponse500 | None:
    """Create a new API key

    Args:
        account_id (float):
        body (CreateKeyPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateKeyResponse | CreateKeyResponse429 | CreateKeyResponse500
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed

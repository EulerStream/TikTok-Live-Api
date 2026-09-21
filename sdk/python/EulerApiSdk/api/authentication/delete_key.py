from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_key_delete_by import DeleteKeyDeleteBy
from ...models.delete_key_response import DeleteKeyResponse
from ...models.delete_key_response_429 import DeleteKeyResponse429
from ...models.delete_key_response_500 import DeleteKeyResponse500
from ...types import UNSET, Response


def _get_kwargs(
    account_id: float,
    *,
    delete_by: DeleteKeyDeleteBy,
    delete_param: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_delete_by = delete_by.value
    params["delete_by"] = json_delete_by

    params["delete_param"] = delete_param

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/accounts/{account_id}/api_keys/delete".format(
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteKeyResponse | DeleteKeyResponse429 | DeleteKeyResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteKeyResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = DeleteKeyResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = DeleteKeyResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteKeyResponse | DeleteKeyResponse429 | DeleteKeyResponse500]:
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
    delete_by: DeleteKeyDeleteBy,
    delete_param: str,
) -> Response[DeleteKeyResponse | DeleteKeyResponse429 | DeleteKeyResponse500]:
    """Delete an API key by its key value, name, or ID

    Args:
        account_id (float):
        delete_by (DeleteKeyDeleteBy):
        delete_param (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteKeyResponse | DeleteKeyResponse429 | DeleteKeyResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        delete_by=delete_by,
        delete_param=delete_param,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: float,
    *,
    client: AuthenticatedClient,
    delete_by: DeleteKeyDeleteBy,
    delete_param: str,
) -> DeleteKeyResponse | DeleteKeyResponse429 | DeleteKeyResponse500 | None:
    """Delete an API key by its key value, name, or ID

    Args:
        account_id (float):
        delete_by (DeleteKeyDeleteBy):
        delete_param (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteKeyResponse | DeleteKeyResponse429 | DeleteKeyResponse500
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        delete_by=delete_by,
        delete_param=delete_param,
    ).parsed


async def asyncio_detailed(
    account_id: float,
    *,
    client: AuthenticatedClient,
    delete_by: DeleteKeyDeleteBy,
    delete_param: str,
) -> Response[DeleteKeyResponse | DeleteKeyResponse429 | DeleteKeyResponse500]:
    """Delete an API key by its key value, name, or ID

    Args:
        account_id (float):
        delete_by (DeleteKeyDeleteBy):
        delete_param (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteKeyResponse | DeleteKeyResponse429 | DeleteKeyResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        delete_by=delete_by,
        delete_param=delete_param,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: float,
    *,
    client: AuthenticatedClient,
    delete_by: DeleteKeyDeleteBy,
    delete_param: str,
) -> DeleteKeyResponse | DeleteKeyResponse429 | DeleteKeyResponse500 | None:
    """Delete an API key by its key value, name, or ID

    Args:
        account_id (float):
        delete_by (DeleteKeyDeleteBy):
        delete_param (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteKeyResponse | DeleteKeyResponse429 | DeleteKeyResponse500
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            delete_by=delete_by,
            delete_param=delete_param,
        )
    ).parsed

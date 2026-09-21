from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_key_response_429 import GetKeyResponse429
from ...models.get_key_response_500 import GetKeyResponse500
from ...models.get_key_retrieve_by import GetKeyRetrieveBy
from ...models.retrieve_key_response import RetrieveKeyResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: float,
    *,
    retrieve_by: GetKeyRetrieveBy | Unset = GetKeyRetrieveBy.VALUE,
    retrieve_param: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_retrieve_by: str | Unset = UNSET
    if not isinstance(retrieve_by, Unset):
        json_retrieve_by = retrieve_by.value

    params["retrieve_by"] = json_retrieve_by

    params["retrieve_param"] = retrieve_param

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/{account_id}/api_keys/retrieve".format(
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetKeyResponse429 | GetKeyResponse500 | RetrieveKeyResponse | None:
    if response.status_code == 200:
        response_200 = RetrieveKeyResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = GetKeyResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetKeyResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetKeyResponse429 | GetKeyResponse500 | RetrieveKeyResponse]:
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
    retrieve_by: GetKeyRetrieveBy | Unset = GetKeyRetrieveBy.VALUE,
    retrieve_param: str,
) -> Response[GetKeyResponse429 | GetKeyResponse500 | RetrieveKeyResponse]:
    """Retrieve an API key by its key value, name, or ID

    Args:
        account_id (float):
        retrieve_by (GetKeyRetrieveBy | Unset):  Default: GetKeyRetrieveBy.VALUE.
        retrieve_param (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetKeyResponse429 | GetKeyResponse500 | RetrieveKeyResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        retrieve_by=retrieve_by,
        retrieve_param=retrieve_param,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: float,
    *,
    client: AuthenticatedClient,
    retrieve_by: GetKeyRetrieveBy | Unset = GetKeyRetrieveBy.VALUE,
    retrieve_param: str,
) -> GetKeyResponse429 | GetKeyResponse500 | RetrieveKeyResponse | None:
    """Retrieve an API key by its key value, name, or ID

    Args:
        account_id (float):
        retrieve_by (GetKeyRetrieveBy | Unset):  Default: GetKeyRetrieveBy.VALUE.
        retrieve_param (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetKeyResponse429 | GetKeyResponse500 | RetrieveKeyResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        retrieve_by=retrieve_by,
        retrieve_param=retrieve_param,
    ).parsed


async def asyncio_detailed(
    account_id: float,
    *,
    client: AuthenticatedClient,
    retrieve_by: GetKeyRetrieveBy | Unset = GetKeyRetrieveBy.VALUE,
    retrieve_param: str,
) -> Response[GetKeyResponse429 | GetKeyResponse500 | RetrieveKeyResponse]:
    """Retrieve an API key by its key value, name, or ID

    Args:
        account_id (float):
        retrieve_by (GetKeyRetrieveBy | Unset):  Default: GetKeyRetrieveBy.VALUE.
        retrieve_param (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetKeyResponse429 | GetKeyResponse500 | RetrieveKeyResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        retrieve_by=retrieve_by,
        retrieve_param=retrieve_param,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: float,
    *,
    client: AuthenticatedClient,
    retrieve_by: GetKeyRetrieveBy | Unset = GetKeyRetrieveBy.VALUE,
    retrieve_param: str,
) -> GetKeyResponse429 | GetKeyResponse500 | RetrieveKeyResponse | None:
    """Retrieve an API key by its key value, name, or ID

    Args:
        account_id (float):
        retrieve_by (GetKeyRetrieveBy | Unset):  Default: GetKeyRetrieveBy.VALUE.
        retrieve_param (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetKeyResponse429 | GetKeyResponse500 | RetrieveKeyResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            retrieve_by=retrieve_by,
            retrieve_param=retrieve_param,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_key_payload import UpdateKeyPayload
from ...models.update_key_response import UpdateKeyResponse
from ...models.update_key_response_429 import UpdateKeyResponse429
from ...models.update_key_response_500 import UpdateKeyResponse500
from ...models.update_key_update_by import UpdateKeyUpdateBy
from ...types import UNSET, Response


def _get_kwargs(
    account_id: float,
    *,
    body: UpdateKeyPayload,
    update_by: UpdateKeyUpdateBy,
    update_param: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_update_by = update_by.value
    params["update_by"] = json_update_by

    params["update_param"] = update_param

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/accounts/{account_id}/api_keys/update".format(
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdateKeyResponse | UpdateKeyResponse429 | UpdateKeyResponse500 | None:
    if response.status_code == 200:
        response_200 = UpdateKeyResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = UpdateKeyResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = UpdateKeyResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateKeyResponse | UpdateKeyResponse429 | UpdateKeyResponse500]:
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
    body: UpdateKeyPayload,
    update_by: UpdateKeyUpdateBy,
    update_param: str,
) -> Response[UpdateKeyResponse | UpdateKeyResponse429 | UpdateKeyResponse500]:
    """Update an existing API key

    Args:
        account_id (float):
        update_by (UpdateKeyUpdateBy):
        update_param (str):
        body (UpdateKeyPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateKeyResponse | UpdateKeyResponse429 | UpdateKeyResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        update_by=update_by,
        update_param=update_param,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: float,
    *,
    client: AuthenticatedClient,
    body: UpdateKeyPayload,
    update_by: UpdateKeyUpdateBy,
    update_param: str,
) -> UpdateKeyResponse | UpdateKeyResponse429 | UpdateKeyResponse500 | None:
    """Update an existing API key

    Args:
        account_id (float):
        update_by (UpdateKeyUpdateBy):
        update_param (str):
        body (UpdateKeyPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateKeyResponse | UpdateKeyResponse429 | UpdateKeyResponse500
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
        update_by=update_by,
        update_param=update_param,
    ).parsed


async def asyncio_detailed(
    account_id: float,
    *,
    client: AuthenticatedClient,
    body: UpdateKeyPayload,
    update_by: UpdateKeyUpdateBy,
    update_param: str,
) -> Response[UpdateKeyResponse | UpdateKeyResponse429 | UpdateKeyResponse500]:
    """Update an existing API key

    Args:
        account_id (float):
        update_by (UpdateKeyUpdateBy):
        update_param (str):
        body (UpdateKeyPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateKeyResponse | UpdateKeyResponse429 | UpdateKeyResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        update_by=update_by,
        update_param=update_param,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: float,
    *,
    client: AuthenticatedClient,
    body: UpdateKeyPayload,
    update_by: UpdateKeyUpdateBy,
    update_param: str,
) -> UpdateKeyResponse | UpdateKeyResponse429 | UpdateKeyResponse500 | None:
    """Update an existing API key

    Args:
        account_id (float):
        update_by (UpdateKeyUpdateBy):
        update_param (str):
        body (UpdateKeyPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateKeyResponse | UpdateKeyResponse429 | UpdateKeyResponse500
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
            update_by=update_by,
            update_param=update_param,
        )
    ).parsed

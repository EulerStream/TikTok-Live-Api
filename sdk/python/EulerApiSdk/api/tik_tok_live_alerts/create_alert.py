from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_alert_body import CreateAlertBody
from ...models.create_alert_response import CreateAlertResponse
from ...models.create_alert_response_429 import CreateAlertResponse429
from ...models.create_alert_response_500 import CreateAlertResponse500
from ...types import Response


def _get_kwargs(
    account_id: float,
    *,
    body: CreateAlertBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/accounts/{account_id}/alerts/create".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateAlertResponse | CreateAlertResponse429 | CreateAlertResponse500 | None:
    if response.status_code == 200:
        response_200 = CreateAlertResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = CreateAlertResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CreateAlertResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateAlertResponse | CreateAlertResponse429 | CreateAlertResponse500]:
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
    body: CreateAlertBody,
) -> Response[CreateAlertResponse | CreateAlertResponse429 | CreateAlertResponse500]:
    """Create a creator alert. These Alerts are used to notify users of a new livestream.

    Args:
        account_id (float):
        body (CreateAlertBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAlertResponse | CreateAlertResponse429 | CreateAlertResponse500]
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
    body: CreateAlertBody,
) -> CreateAlertResponse | CreateAlertResponse429 | CreateAlertResponse500 | None:
    """Create a creator alert. These Alerts are used to notify users of a new livestream.

    Args:
        account_id (float):
        body (CreateAlertBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAlertResponse | CreateAlertResponse429 | CreateAlertResponse500
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
    body: CreateAlertBody,
) -> Response[CreateAlertResponse | CreateAlertResponse429 | CreateAlertResponse500]:
    """Create a creator alert. These Alerts are used to notify users of a new livestream.

    Args:
        account_id (float):
        body (CreateAlertBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAlertResponse | CreateAlertResponse429 | CreateAlertResponse500]
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
    body: CreateAlertBody,
) -> CreateAlertResponse | CreateAlertResponse429 | CreateAlertResponse500 | None:
    """Create a creator alert. These Alerts are used to notify users of a new livestream.

    Args:
        account_id (float):
        body (CreateAlertBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAlertResponse | CreateAlertResponse429 | CreateAlertResponse500
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed

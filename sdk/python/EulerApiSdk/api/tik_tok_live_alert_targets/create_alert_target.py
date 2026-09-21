from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_alert_target_payload import CreateAlertTargetPayload
from ...models.create_alert_target_response import CreateAlertTargetResponse
from ...models.create_alert_target_response_429 import CreateAlertTargetResponse429
from ...models.create_alert_target_response_500 import CreateAlertTargetResponse500
from ...types import Response


def _get_kwargs(
    account_id: float,
    alert_id: float,
    *,
    body: CreateAlertTargetPayload,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/accounts/{account_id}/alerts/{alert_id}/targets/create".format(
            account_id=quote(str(account_id), safe=""),
            alert_id=quote(str(alert_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateAlertTargetResponse | CreateAlertTargetResponse429 | CreateAlertTargetResponse500 | None:
    if response.status_code == 200:
        response_200 = CreateAlertTargetResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = CreateAlertTargetResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CreateAlertTargetResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateAlertTargetResponse | CreateAlertTargetResponse429 | CreateAlertTargetResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: float,
    alert_id: float,
    *,
    client: AuthenticatedClient,
    body: CreateAlertTargetPayload,
) -> Response[CreateAlertTargetResponse | CreateAlertTargetResponse429 | CreateAlertTargetResponse500]:
    """Create a target for an alert. This is the HTTP endpoint that will be called when an alert is
    triggered.

    Args:
        account_id (float):
        alert_id (float):
        body (CreateAlertTargetPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAlertTargetResponse | CreateAlertTargetResponse429 | CreateAlertTargetResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        alert_id=alert_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: float,
    alert_id: float,
    *,
    client: AuthenticatedClient,
    body: CreateAlertTargetPayload,
) -> CreateAlertTargetResponse | CreateAlertTargetResponse429 | CreateAlertTargetResponse500 | None:
    """Create a target for an alert. This is the HTTP endpoint that will be called when an alert is
    triggered.

    Args:
        account_id (float):
        alert_id (float):
        body (CreateAlertTargetPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAlertTargetResponse | CreateAlertTargetResponse429 | CreateAlertTargetResponse500
    """

    return sync_detailed(
        account_id=account_id,
        alert_id=alert_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: float,
    alert_id: float,
    *,
    client: AuthenticatedClient,
    body: CreateAlertTargetPayload,
) -> Response[CreateAlertTargetResponse | CreateAlertTargetResponse429 | CreateAlertTargetResponse500]:
    """Create a target for an alert. This is the HTTP endpoint that will be called when an alert is
    triggered.

    Args:
        account_id (float):
        alert_id (float):
        body (CreateAlertTargetPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAlertTargetResponse | CreateAlertTargetResponse429 | CreateAlertTargetResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        alert_id=alert_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: float,
    alert_id: float,
    *,
    client: AuthenticatedClient,
    body: CreateAlertTargetPayload,
) -> CreateAlertTargetResponse | CreateAlertTargetResponse429 | CreateAlertTargetResponse500 | None:
    """Create a target for an alert. This is the HTTP endpoint that will be called when an alert is
    triggered.

    Args:
        account_id (float):
        alert_id (float):
        body (CreateAlertTargetPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAlertTargetResponse | CreateAlertTargetResponse429 | CreateAlertTargetResponse500
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            alert_id=alert_id,
            client=client,
            body=body,
        )
    ).parsed

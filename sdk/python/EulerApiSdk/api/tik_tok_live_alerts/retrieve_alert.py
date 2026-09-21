from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_alert_response import RetrieveAlertResponse
from ...models.retrieve_alert_response_429 import RetrieveAlertResponse429
from ...models.retrieve_alert_response_500 import RetrieveAlertResponse500
from ...types import Response


def _get_kwargs(
    account_id: float,
    alert_id: float,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/{account_id}/alerts/{alert_id}/retrieve".format(
            account_id=quote(str(account_id), safe=""),
            alert_id=quote(str(alert_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RetrieveAlertResponse | RetrieveAlertResponse429 | RetrieveAlertResponse500 | None:
    if response.status_code == 200:
        response_200 = RetrieveAlertResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveAlertResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveAlertResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RetrieveAlertResponse | RetrieveAlertResponse429 | RetrieveAlertResponse500]:
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
) -> Response[RetrieveAlertResponse | RetrieveAlertResponse429 | RetrieveAlertResponse500]:
    """Retrieve a specific alert by its ID

    Args:
        account_id (float):
        alert_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveAlertResponse | RetrieveAlertResponse429 | RetrieveAlertResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        alert_id=alert_id,
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
) -> RetrieveAlertResponse | RetrieveAlertResponse429 | RetrieveAlertResponse500 | None:
    """Retrieve a specific alert by its ID

    Args:
        account_id (float):
        alert_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveAlertResponse | RetrieveAlertResponse429 | RetrieveAlertResponse500
    """

    return sync_detailed(
        account_id=account_id,
        alert_id=alert_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: float,
    alert_id: float,
    *,
    client: AuthenticatedClient,
) -> Response[RetrieveAlertResponse | RetrieveAlertResponse429 | RetrieveAlertResponse500]:
    """Retrieve a specific alert by its ID

    Args:
        account_id (float):
        alert_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveAlertResponse | RetrieveAlertResponse429 | RetrieveAlertResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        alert_id=alert_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: float,
    alert_id: float,
    *,
    client: AuthenticatedClient,
) -> RetrieveAlertResponse | RetrieveAlertResponse429 | RetrieveAlertResponse500 | None:
    """Retrieve a specific alert by its ID

    Args:
        account_id (float):
        alert_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveAlertResponse | RetrieveAlertResponse429 | RetrieveAlertResponse500
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            alert_id=alert_id,
            client=client,
        )
    ).parsed

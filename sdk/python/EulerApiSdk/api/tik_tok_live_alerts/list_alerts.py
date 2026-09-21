from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_alerts_response import ListAlertsResponse
from ...models.list_alerts_response_429 import ListAlertsResponse429
from ...models.list_alerts_response_500 import ListAlertsResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: float,
    *,
    page: float | Unset = 0.0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/{account_id}/alerts/list".format(
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListAlertsResponse | ListAlertsResponse429 | ListAlertsResponse500 | None:
    if response.status_code == 200:
        response_200 = ListAlertsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = ListAlertsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListAlertsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListAlertsResponse | ListAlertsResponse429 | ListAlertsResponse500]:
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
    page: float | Unset = 0.0,
) -> Response[ListAlertsResponse | ListAlertsResponse429 | ListAlertsResponse500]:
    """
    Args:
        account_id (float):
        page (float | Unset):  Default: 0.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAlertsResponse | ListAlertsResponse429 | ListAlertsResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: float,
    *,
    client: AuthenticatedClient,
    page: float | Unset = 0.0,
) -> ListAlertsResponse | ListAlertsResponse429 | ListAlertsResponse500 | None:
    """
    Args:
        account_id (float):
        page (float | Unset):  Default: 0.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAlertsResponse | ListAlertsResponse429 | ListAlertsResponse500
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        page=page,
    ).parsed


async def asyncio_detailed(
    account_id: float,
    *,
    client: AuthenticatedClient,
    page: float | Unset = 0.0,
) -> Response[ListAlertsResponse | ListAlertsResponse429 | ListAlertsResponse500]:
    """
    Args:
        account_id (float):
        page (float | Unset):  Default: 0.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAlertsResponse | ListAlertsResponse429 | ListAlertsResponse500]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: float,
    *,
    client: AuthenticatedClient,
    page: float | Unset = 0.0,
) -> ListAlertsResponse | ListAlertsResponse429 | ListAlertsResponse500 | None:
    """
    Args:
        account_id (float):
        page (float | Unset):  Default: 0.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAlertsResponse | ListAlertsResponse429 | ListAlertsResponse500
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            page=page,
        )
    ).parsed

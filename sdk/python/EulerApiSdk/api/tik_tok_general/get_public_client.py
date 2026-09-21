from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_public_client_response import GetPublicClientResponse
from ...models.get_public_client_response_429 import GetPublicClientResponse429
from ...models.get_public_client_response_500 import GetPublicClientResponse500
from ...types import Response


def _get_kwargs(
    client_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tiktok/oauth/clients/{client_id}".format(
            client_id=quote(str(client_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPublicClientResponse | GetPublicClientResponse429 | GetPublicClientResponse500 | None:
    if response.status_code == 200:
        response_200 = GetPublicClientResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = GetPublicClientResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetPublicClientResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetPublicClientResponse | GetPublicClientResponse429 | GetPublicClientResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    client_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetPublicClientResponse | GetPublicClientResponse429 | GetPublicClientResponse500]:
    """Get public information about an OAuth client by client_id.
    This endpoint is used during the authorization flow to display
    client information to the user before they authorize.

    Does not require authentication.
    Does not expose sensitive information like client_secret_hash.

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPublicClientResponse | GetPublicClientResponse429 | GetPublicClientResponse500]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    client_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetPublicClientResponse | GetPublicClientResponse429 | GetPublicClientResponse500 | None:
    """Get public information about an OAuth client by client_id.
    This endpoint is used during the authorization flow to display
    client information to the user before they authorize.

    Does not require authentication.
    Does not expose sensitive information like client_secret_hash.

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPublicClientResponse | GetPublicClientResponse429 | GetPublicClientResponse500
    """

    return sync_detailed(
        client_id=client_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    client_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetPublicClientResponse | GetPublicClientResponse429 | GetPublicClientResponse500]:
    """Get public information about an OAuth client by client_id.
    This endpoint is used during the authorization flow to display
    client information to the user before they authorize.

    Does not require authentication.
    Does not expose sensitive information like client_secret_hash.

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPublicClientResponse | GetPublicClientResponse429 | GetPublicClientResponse500]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    client_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetPublicClientResponse | GetPublicClientResponse429 | GetPublicClientResponse500 | None:
    """Get public information about an OAuth client by client_id.
    This endpoint is used during the authorization flow to display
    client information to the user before they authorize.

    Does not require authentication.
    Does not expose sensitive information like client_secret_hash.

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPublicClientResponse | GetPublicClientResponse429 | GetPublicClientResponse500
    """

    return (
        await asyncio_detailed(
            client_id=client_id,
            client=client,
        )
    ).parsed

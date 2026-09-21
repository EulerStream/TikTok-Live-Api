from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exchange_token_request import ExchangeTokenRequest
from ...models.exchange_token_response_429 import ExchangeTokenResponse429
from ...models.exchange_token_response_500 import ExchangeTokenResponse500
from ...models.o_auth_token_response import OAuthTokenResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ExchangeTokenRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tiktok/oauth/token",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExchangeTokenResponse429 | ExchangeTokenResponse500 | OAuthTokenResponse | None:
    if response.status_code == 200:
        response_200 = OAuthTokenResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = ExchangeTokenResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ExchangeTokenResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExchangeTokenResponse429 | ExchangeTokenResponse500 | OAuthTokenResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExchangeTokenRequest,
) -> Response[ExchangeTokenResponse429 | ExchangeTokenResponse500 | OAuthTokenResponse]:
    """Exchange an authorization code or refresh token for access tokens.

    For authorization_code grant:
    - code: The authorization code from /oauth/complete
    - redirect_uri: Must match the original redirect_uri

    For refresh_token grant:
    - refresh_token: A valid refresh token

    Args:
        body (ExchangeTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeTokenResponse429 | ExchangeTokenResponse500 | OAuthTokenResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ExchangeTokenRequest,
) -> ExchangeTokenResponse429 | ExchangeTokenResponse500 | OAuthTokenResponse | None:
    """Exchange an authorization code or refresh token for access tokens.

    For authorization_code grant:
    - code: The authorization code from /oauth/complete
    - redirect_uri: Must match the original redirect_uri

    For refresh_token grant:
    - refresh_token: A valid refresh token

    Args:
        body (ExchangeTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeTokenResponse429 | ExchangeTokenResponse500 | OAuthTokenResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExchangeTokenRequest,
) -> Response[ExchangeTokenResponse429 | ExchangeTokenResponse500 | OAuthTokenResponse]:
    """Exchange an authorization code or refresh token for access tokens.

    For authorization_code grant:
    - code: The authorization code from /oauth/complete
    - redirect_uri: Must match the original redirect_uri

    For refresh_token grant:
    - refresh_token: A valid refresh token

    Args:
        body (ExchangeTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeTokenResponse429 | ExchangeTokenResponse500 | OAuthTokenResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ExchangeTokenRequest,
) -> ExchangeTokenResponse429 | ExchangeTokenResponse500 | OAuthTokenResponse | None:
    """Exchange an authorization code or refresh token for access tokens.

    For authorization_code grant:
    - code: The authorization code from /oauth/complete
    - redirect_uri: Must match the original redirect_uri

    For refresh_token grant:
    - refresh_token: A valid refresh token

    Args:
        body (ExchangeTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeTokenResponse429 | ExchangeTokenResponse500 | OAuthTokenResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

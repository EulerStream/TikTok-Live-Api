from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.validate_refresh_request import ValidateRefreshRequest
from ...models.validate_refresh_response import ValidateRefreshResponse
from ...models.validate_refresh_token_response_429 import ValidateRefreshTokenResponse429
from ...models.validate_refresh_token_response_500 import ValidateRefreshTokenResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: ValidateRefreshRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tiktok/oauth/validate-refresh",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ValidateRefreshResponse | ValidateRefreshTokenResponse429 | ValidateRefreshTokenResponse500 | None:
    if response.status_code == 200:
        response_200 = ValidateRefreshResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = ValidateRefreshTokenResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ValidateRefreshTokenResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ValidateRefreshResponse | ValidateRefreshTokenResponse429 | ValidateRefreshTokenResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ValidateRefreshRequest,
) -> Response[ValidateRefreshResponse | ValidateRefreshTokenResponse429 | ValidateRefreshTokenResponse500]:
    """Check if a stored refresh token is still valid without consuming it.
    Returns metadata about the session if valid.

    This is a public endpoint — no authentication required.

    Args:
        body (ValidateRefreshRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ValidateRefreshResponse | ValidateRefreshTokenResponse429 | ValidateRefreshTokenResponse500]
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
    body: ValidateRefreshRequest,
) -> ValidateRefreshResponse | ValidateRefreshTokenResponse429 | ValidateRefreshTokenResponse500 | None:
    """Check if a stored refresh token is still valid without consuming it.
    Returns metadata about the session if valid.

    This is a public endpoint — no authentication required.

    Args:
        body (ValidateRefreshRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ValidateRefreshResponse | ValidateRefreshTokenResponse429 | ValidateRefreshTokenResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ValidateRefreshRequest,
) -> Response[ValidateRefreshResponse | ValidateRefreshTokenResponse429 | ValidateRefreshTokenResponse500]:
    """Check if a stored refresh token is still valid without consuming it.
    Returns metadata about the session if valid.

    This is a public endpoint — no authentication required.

    Args:
        body (ValidateRefreshRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ValidateRefreshResponse | ValidateRefreshTokenResponse429 | ValidateRefreshTokenResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ValidateRefreshRequest,
) -> ValidateRefreshResponse | ValidateRefreshTokenResponse429 | ValidateRefreshTokenResponse500 | None:
    """Check if a stored refresh token is still valid without consuming it.
    Returns metadata about the session if valid.

    This is a public endpoint — no authentication required.

    Args:
        body (ValidateRefreshRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ValidateRefreshResponse | ValidateRefreshTokenResponse429 | ValidateRefreshTokenResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.introspect_request_body import IntrospectRequestBody
from ...models.introspect_token_response_429 import IntrospectTokenResponse429
from ...models.introspect_token_response_500 import IntrospectTokenResponse500
from ...models.o_auth_introspect_response import OAuthIntrospectResponse
from ...types import Response


def _get_kwargs(
    *,
    body: IntrospectRequestBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tiktok/oauth/introspect",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IntrospectTokenResponse429 | IntrospectTokenResponse500 | OAuthIntrospectResponse | None:
    if response.status_code == 200:
        response_200 = OAuthIntrospectResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = IntrospectTokenResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = IntrospectTokenResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IntrospectTokenResponse429 | IntrospectTokenResponse500 | OAuthIntrospectResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IntrospectRequestBody,
) -> Response[IntrospectTokenResponse429 | IntrospectTokenResponse500 | OAuthIntrospectResponse]:
    """Introspect a token to determine its state (RFC 7662).
    Returns active: true/false along with token metadata.
    Works for both access tokens and refresh tokens.

    Args:
        body (IntrospectRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntrospectTokenResponse429 | IntrospectTokenResponse500 | OAuthIntrospectResponse]
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
    body: IntrospectRequestBody,
) -> IntrospectTokenResponse429 | IntrospectTokenResponse500 | OAuthIntrospectResponse | None:
    """Introspect a token to determine its state (RFC 7662).
    Returns active: true/false along with token metadata.
    Works for both access tokens and refresh tokens.

    Args:
        body (IntrospectRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntrospectTokenResponse429 | IntrospectTokenResponse500 | OAuthIntrospectResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IntrospectRequestBody,
) -> Response[IntrospectTokenResponse429 | IntrospectTokenResponse500 | OAuthIntrospectResponse]:
    """Introspect a token to determine its state (RFC 7662).
    Returns active: true/false along with token metadata.
    Works for both access tokens and refresh tokens.

    Args:
        body (IntrospectRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntrospectTokenResponse429 | IntrospectTokenResponse500 | OAuthIntrospectResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: IntrospectRequestBody,
) -> IntrospectTokenResponse429 | IntrospectTokenResponse500 | OAuthIntrospectResponse | None:
    """Introspect a token to determine its state (RFC 7662).
    Returns active: true/false along with token metadata.
    Works for both access tokens and refresh tokens.

    Args:
        body (IntrospectRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntrospectTokenResponse429 | IntrospectTokenResponse500 | OAuthIntrospectResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

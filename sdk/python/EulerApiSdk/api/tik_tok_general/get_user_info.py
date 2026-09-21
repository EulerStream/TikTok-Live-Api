from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_user_info_response_429 import GetUserInfoResponse429
from ...models.get_user_info_response_500 import GetUserInfoResponse500
from ...models.o_auth_user_info_response import OAuthUserInfoResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    x_oauth_token: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_oauth_token, Unset):
        headers["x-oauth-token"] = x_oauth_token

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tiktok/oauth/userinfo",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetUserInfoResponse429 | GetUserInfoResponse500 | OAuthUserInfoResponse | None:
    if response.status_code == 200:
        response_200 = OAuthUserInfoResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = GetUserInfoResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetUserInfoResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetUserInfoResponse429 | GetUserInfoResponse500 | OAuthUserInfoResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_oauth_token: str | Unset = UNSET,
) -> Response[GetUserInfoResponse429 | GetUserInfoResponse500 | OAuthUserInfoResponse]:
    """Get information about the currently authenticated TikTok user.
    Requires a valid OAuth token with an active TikTok session.

    **Authentication:** Provide the following header:
    - `x-oauth-token`: An OAuth access token. [Read More](https://www.eulerstream.com/docs/oauth)

    Args:
        x_oauth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserInfoResponse429 | GetUserInfoResponse500 | OAuthUserInfoResponse]
    """

    kwargs = _get_kwargs(
        x_oauth_token=x_oauth_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    x_oauth_token: str | Unset = UNSET,
) -> GetUserInfoResponse429 | GetUserInfoResponse500 | OAuthUserInfoResponse | None:
    """Get information about the currently authenticated TikTok user.
    Requires a valid OAuth token with an active TikTok session.

    **Authentication:** Provide the following header:
    - `x-oauth-token`: An OAuth access token. [Read More](https://www.eulerstream.com/docs/oauth)

    Args:
        x_oauth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserInfoResponse429 | GetUserInfoResponse500 | OAuthUserInfoResponse
    """

    return sync_detailed(
        client=client,
        x_oauth_token=x_oauth_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_oauth_token: str | Unset = UNSET,
) -> Response[GetUserInfoResponse429 | GetUserInfoResponse500 | OAuthUserInfoResponse]:
    """Get information about the currently authenticated TikTok user.
    Requires a valid OAuth token with an active TikTok session.

    **Authentication:** Provide the following header:
    - `x-oauth-token`: An OAuth access token. [Read More](https://www.eulerstream.com/docs/oauth)

    Args:
        x_oauth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserInfoResponse429 | GetUserInfoResponse500 | OAuthUserInfoResponse]
    """

    kwargs = _get_kwargs(
        x_oauth_token=x_oauth_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    x_oauth_token: str | Unset = UNSET,
) -> GetUserInfoResponse429 | GetUserInfoResponse500 | OAuthUserInfoResponse | None:
    """Get information about the currently authenticated TikTok user.
    Requires a valid OAuth token with an active TikTok session.

    **Authentication:** Provide the following header:
    - `x-oauth-token`: An OAuth access token. [Read More](https://www.eulerstream.com/docs/oauth)

    Args:
        x_oauth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserInfoResponse429 | GetUserInfoResponse500 | OAuthUserInfoResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            x_oauth_token=x_oauth_token,
        )
    ).parsed

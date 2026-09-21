from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_rate_limits import GetRateLimits
from ...models.get_rate_limits_response_429 import GetRateLimitsResponse429
from ...models.get_rate_limits_response_500 import GetRateLimitsResponse500
from ...models.rate_limit_type import RateLimitType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: RateLimitType | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/me/rate_limits",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetRateLimits | GetRateLimitsResponse429 | GetRateLimitsResponse500 | None:
    if response.status_code == 200:
        response_200 = GetRateLimits.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = GetRateLimitsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetRateLimitsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetRateLimits | GetRateLimitsResponse429 | GetRateLimitsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    type_: RateLimitType | Unset = UNSET,
) -> Response[GetRateLimits | GetRateLimitsResponse429 | GetRateLimitsResponse500]:
    """Retrieve the rate limits for the provided API key (or the unauthenticated limits if no key is
    provided)

    Args:
        type_ (RateLimitType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRateLimits | GetRateLimitsResponse429 | GetRateLimitsResponse500]
    """

    kwargs = _get_kwargs(
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    type_: RateLimitType | Unset = UNSET,
) -> GetRateLimits | GetRateLimitsResponse429 | GetRateLimitsResponse500 | None:
    """Retrieve the rate limits for the provided API key (or the unauthenticated limits if no key is
    provided)

    Args:
        type_ (RateLimitType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRateLimits | GetRateLimitsResponse429 | GetRateLimitsResponse500
    """

    return sync_detailed(
        client=client,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    type_: RateLimitType | Unset = UNSET,
) -> Response[GetRateLimits | GetRateLimitsResponse429 | GetRateLimitsResponse500]:
    """Retrieve the rate limits for the provided API key (or the unauthenticated limits if no key is
    provided)

    Args:
        type_ (RateLimitType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRateLimits | GetRateLimitsResponse429 | GetRateLimitsResponse500]
    """

    kwargs = _get_kwargs(
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    type_: RateLimitType | Unset = UNSET,
) -> GetRateLimits | GetRateLimitsResponse429 | GetRateLimitsResponse500 | None:
    """Retrieve the rate limits for the provided API key (or the unauthenticated limits if no key is
    provided)

    Args:
        type_ (RateLimitType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRateLimits | GetRateLimitsResponse429 | GetRateLimitsResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
        )
    ).parsed

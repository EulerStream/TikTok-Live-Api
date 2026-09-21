from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.captcha_credits_response import CaptchaCreditsResponse
from ...models.retrieve_captcha_credits_response_429 import RetrieveCaptchaCreditsResponse429
from ...models.retrieve_captcha_credits_response_500 import RetrieveCaptchaCreditsResponse500
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tiktok/captchas/credits",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CaptchaCreditsResponse | RetrieveCaptchaCreditsResponse429 | RetrieveCaptchaCreditsResponse500 | None:
    if response.status_code == 200:
        response_200 = CaptchaCreditsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveCaptchaCreditsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveCaptchaCreditsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CaptchaCreditsResponse | RetrieveCaptchaCreditsResponse429 | RetrieveCaptchaCreditsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[CaptchaCreditsResponse | RetrieveCaptchaCreditsResponse429 | RetrieveCaptchaCreditsResponse500]:
    """Retrieve the rate limits for the provided API key.

    This route is deprecated as CAPTCHAs are no longer billed for usage.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CaptchaCreditsResponse | RetrieveCaptchaCreditsResponse429 | RetrieveCaptchaCreditsResponse500]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> CaptchaCreditsResponse | RetrieveCaptchaCreditsResponse429 | RetrieveCaptchaCreditsResponse500 | None:
    """Retrieve the rate limits for the provided API key.

    This route is deprecated as CAPTCHAs are no longer billed for usage.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CaptchaCreditsResponse | RetrieveCaptchaCreditsResponse429 | RetrieveCaptchaCreditsResponse500
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[CaptchaCreditsResponse | RetrieveCaptchaCreditsResponse429 | RetrieveCaptchaCreditsResponse500]:
    """Retrieve the rate limits for the provided API key.

    This route is deprecated as CAPTCHAs are no longer billed for usage.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CaptchaCreditsResponse | RetrieveCaptchaCreditsResponse429 | RetrieveCaptchaCreditsResponse500]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> CaptchaCreditsResponse | RetrieveCaptchaCreditsResponse429 | RetrieveCaptchaCreditsResponse500 | None:
    """Retrieve the rate limits for the provided API key.

    This route is deprecated as CAPTCHAs are no longer billed for usage.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CaptchaCreditsResponse | RetrieveCaptchaCreditsResponse429 | RetrieveCaptchaCreditsResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

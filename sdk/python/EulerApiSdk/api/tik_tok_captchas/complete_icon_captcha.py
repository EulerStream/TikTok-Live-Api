from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.complete_icon_captcha_body import CompleteIconCaptchaBody
from ...models.complete_icon_captcha_response_429 import CompleteIconCaptchaResponse429
from ...models.complete_icon_captcha_response_500 import CompleteIconCaptchaResponse500
from ...models.icon_captcha_response import IconCaptchaResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: CompleteIconCaptchaBody,
    prompt: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["prompt"] = prompt

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tiktok/captchas/icons",
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CompleteIconCaptchaResponse429 | CompleteIconCaptchaResponse500 | IconCaptchaResponse | None:
    if response.status_code == 200:
        response_200 = IconCaptchaResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = CompleteIconCaptchaResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CompleteIconCaptchaResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CompleteIconCaptchaResponse429 | CompleteIconCaptchaResponse500 | IconCaptchaResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CompleteIconCaptchaBody,
    prompt: str,
) -> Response[CompleteIconCaptchaResponse429 | CompleteIconCaptchaResponse500 | IconCaptchaResponse]:
    r"""The icons captcha requires just one image & a prompt string.

    ## Example Image
    <img src=\"https://www.eulerstream.com/_static/captchas/icon.png\" alt=\"Icons Captcha Example\"
    width=\"480\" />

    ## Usage

    The `prompt` is the text prompt provided by TikTok. The Icon captcha solution is provided as a list
    of points, where each point marks a location on the image that needs to be clicked.
    These points are expressed as ratios relative to the image's width and height.
    A point of (0.0, 0.0) corresponds to the image’s upper-left corner, while (1.0, 1.0) represents the
    lower-right corner. For reference, (0.5, 0.5) sits at the exact center.

    The captcha image selector is `.captcha-verify-image`

    Args:
        prompt (str):
        body (CompleteIconCaptchaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompleteIconCaptchaResponse429 | CompleteIconCaptchaResponse500 | IconCaptchaResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        prompt=prompt,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CompleteIconCaptchaBody,
    prompt: str,
) -> CompleteIconCaptchaResponse429 | CompleteIconCaptchaResponse500 | IconCaptchaResponse | None:
    r"""The icons captcha requires just one image & a prompt string.

    ## Example Image
    <img src=\"https://www.eulerstream.com/_static/captchas/icon.png\" alt=\"Icons Captcha Example\"
    width=\"480\" />

    ## Usage

    The `prompt` is the text prompt provided by TikTok. The Icon captcha solution is provided as a list
    of points, where each point marks a location on the image that needs to be clicked.
    These points are expressed as ratios relative to the image's width and height.
    A point of (0.0, 0.0) corresponds to the image’s upper-left corner, while (1.0, 1.0) represents the
    lower-right corner. For reference, (0.5, 0.5) sits at the exact center.

    The captcha image selector is `.captcha-verify-image`

    Args:
        prompt (str):
        body (CompleteIconCaptchaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompleteIconCaptchaResponse429 | CompleteIconCaptchaResponse500 | IconCaptchaResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        prompt=prompt,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CompleteIconCaptchaBody,
    prompt: str,
) -> Response[CompleteIconCaptchaResponse429 | CompleteIconCaptchaResponse500 | IconCaptchaResponse]:
    r"""The icons captcha requires just one image & a prompt string.

    ## Example Image
    <img src=\"https://www.eulerstream.com/_static/captchas/icon.png\" alt=\"Icons Captcha Example\"
    width=\"480\" />

    ## Usage

    The `prompt` is the text prompt provided by TikTok. The Icon captcha solution is provided as a list
    of points, where each point marks a location on the image that needs to be clicked.
    These points are expressed as ratios relative to the image's width and height.
    A point of (0.0, 0.0) corresponds to the image’s upper-left corner, while (1.0, 1.0) represents the
    lower-right corner. For reference, (0.5, 0.5) sits at the exact center.

    The captcha image selector is `.captcha-verify-image`

    Args:
        prompt (str):
        body (CompleteIconCaptchaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompleteIconCaptchaResponse429 | CompleteIconCaptchaResponse500 | IconCaptchaResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        prompt=prompt,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CompleteIconCaptchaBody,
    prompt: str,
) -> CompleteIconCaptchaResponse429 | CompleteIconCaptchaResponse500 | IconCaptchaResponse | None:
    r"""The icons captcha requires just one image & a prompt string.

    ## Example Image
    <img src=\"https://www.eulerstream.com/_static/captchas/icon.png\" alt=\"Icons Captcha Example\"
    width=\"480\" />

    ## Usage

    The `prompt` is the text prompt provided by TikTok. The Icon captcha solution is provided as a list
    of points, where each point marks a location on the image that needs to be clicked.
    These points are expressed as ratios relative to the image's width and height.
    A point of (0.0, 0.0) corresponds to the image’s upper-left corner, while (1.0, 1.0) represents the
    lower-right corner. For reference, (0.5, 0.5) sits at the exact center.

    The captcha image selector is `.captcha-verify-image`

    Args:
        prompt (str):
        body (CompleteIconCaptchaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompleteIconCaptchaResponse429 | CompleteIconCaptchaResponse500 | IconCaptchaResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            prompt=prompt,
        )
    ).parsed

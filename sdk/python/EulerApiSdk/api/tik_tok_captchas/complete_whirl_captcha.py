from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.complete_whirl_captcha_body import CompleteWhirlCaptchaBody
from ...models.complete_whirl_captcha_response_429 import CompleteWhirlCaptchaResponse429
from ...models.complete_whirl_captcha_response_500 import CompleteWhirlCaptchaResponse500
from ...models.whirl_captcha_response import WhirlCaptchaResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CompleteWhirlCaptchaBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tiktok/captchas/whirl",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CompleteWhirlCaptchaResponse429 | CompleteWhirlCaptchaResponse500 | WhirlCaptchaResponse | None:
    if response.status_code == 200:
        response_200 = WhirlCaptchaResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = CompleteWhirlCaptchaResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CompleteWhirlCaptchaResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CompleteWhirlCaptchaResponse429 | CompleteWhirlCaptchaResponse500 | WhirlCaptchaResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CompleteWhirlCaptchaBody,
) -> Response[CompleteWhirlCaptchaResponse429 | CompleteWhirlCaptchaResponse500 | WhirlCaptchaResponse]:
    r"""The whirl captcha requires two images: the outer image and the inner image.

    ## Example Image
    <img src=\"https://www.eulerstream.com/_static/captchas/rotate.png\" alt=\"Whirl Captcha Example\"
    width=\"480\" />

    ## Usage

    The solution to the whirl captcha is an angle from 0-360. To use it in the GUI, it must be converted
    to a slider distance:

    `px = ((sidebar_length - icon_length) * angle) / 360`

    - `sidebar_length` is the width of `.captcha_verify_slide--slidebar`
    - `icon_length` is the width of `.secsdk-captcha-drag-icon`

    Args:
        body (CompleteWhirlCaptchaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompleteWhirlCaptchaResponse429 | CompleteWhirlCaptchaResponse500 | WhirlCaptchaResponse]
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
    client: AuthenticatedClient,
    body: CompleteWhirlCaptchaBody,
) -> CompleteWhirlCaptchaResponse429 | CompleteWhirlCaptchaResponse500 | WhirlCaptchaResponse | None:
    r"""The whirl captcha requires two images: the outer image and the inner image.

    ## Example Image
    <img src=\"https://www.eulerstream.com/_static/captchas/rotate.png\" alt=\"Whirl Captcha Example\"
    width=\"480\" />

    ## Usage

    The solution to the whirl captcha is an angle from 0-360. To use it in the GUI, it must be converted
    to a slider distance:

    `px = ((sidebar_length - icon_length) * angle) / 360`

    - `sidebar_length` is the width of `.captcha_verify_slide--slidebar`
    - `icon_length` is the width of `.secsdk-captcha-drag-icon`

    Args:
        body (CompleteWhirlCaptchaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompleteWhirlCaptchaResponse429 | CompleteWhirlCaptchaResponse500 | WhirlCaptchaResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CompleteWhirlCaptchaBody,
) -> Response[CompleteWhirlCaptchaResponse429 | CompleteWhirlCaptchaResponse500 | WhirlCaptchaResponse]:
    r"""The whirl captcha requires two images: the outer image and the inner image.

    ## Example Image
    <img src=\"https://www.eulerstream.com/_static/captchas/rotate.png\" alt=\"Whirl Captcha Example\"
    width=\"480\" />

    ## Usage

    The solution to the whirl captcha is an angle from 0-360. To use it in the GUI, it must be converted
    to a slider distance:

    `px = ((sidebar_length - icon_length) * angle) / 360`

    - `sidebar_length` is the width of `.captcha_verify_slide--slidebar`
    - `icon_length` is the width of `.secsdk-captcha-drag-icon`

    Args:
        body (CompleteWhirlCaptchaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompleteWhirlCaptchaResponse429 | CompleteWhirlCaptchaResponse500 | WhirlCaptchaResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CompleteWhirlCaptchaBody,
) -> CompleteWhirlCaptchaResponse429 | CompleteWhirlCaptchaResponse500 | WhirlCaptchaResponse | None:
    r"""The whirl captcha requires two images: the outer image and the inner image.

    ## Example Image
    <img src=\"https://www.eulerstream.com/_static/captchas/rotate.png\" alt=\"Whirl Captcha Example\"
    width=\"480\" />

    ## Usage

    The solution to the whirl captcha is an angle from 0-360. To use it in the GUI, it must be converted
    to a slider distance:

    `px = ((sidebar_length - icon_length) * angle) / 360`

    - `sidebar_length` is the width of `.captcha_verify_slide--slidebar`
    - `icon_length` is the width of `.secsdk-captcha-drag-icon`

    Args:
        body (CompleteWhirlCaptchaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompleteWhirlCaptchaResponse429 | CompleteWhirlCaptchaResponse500 | WhirlCaptchaResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

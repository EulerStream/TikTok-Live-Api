from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.complete_shapes_captcha_body import CompleteShapesCaptchaBody
from ...models.complete_shapes_captcha_response_429 import CompleteShapesCaptchaResponse429
from ...models.complete_shapes_captcha_response_500 import CompleteShapesCaptchaResponse500
from ...models.shapes_captcha_response import ShapesCaptchaResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CompleteShapesCaptchaBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tiktok/captchas/shapes",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CompleteShapesCaptchaResponse429 | CompleteShapesCaptchaResponse500 | ShapesCaptchaResponse | None:
    if response.status_code == 200:
        response_200 = ShapesCaptchaResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = CompleteShapesCaptchaResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CompleteShapesCaptchaResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CompleteShapesCaptchaResponse429 | CompleteShapesCaptchaResponse500 | ShapesCaptchaResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CompleteShapesCaptchaBody,
) -> Response[CompleteShapesCaptchaResponse429 | CompleteShapesCaptchaResponse500 | ShapesCaptchaResponse]:
    r"""The shapes captcha requires just one image.

    ## Example Image
    <img src=\"https://www.eulerstream.com/_static/captchas/threed.png\" alt=\"Shapes Captcha Example\"
    width=\"480\" />

    ## Usage

    The solution to the shapes captcha are two points that need to be clicked. To use it in the GUI,
    convert the proportions to pixel values based on the image size.

    The `points` are returned as `x` and `y` proportions (0-1) of the width and height of the source
    image.
    The captcha image selector is `.captcha-verify-image`

    Args:
        body (CompleteShapesCaptchaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompleteShapesCaptchaResponse429 | CompleteShapesCaptchaResponse500 | ShapesCaptchaResponse]
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
    body: CompleteShapesCaptchaBody,
) -> CompleteShapesCaptchaResponse429 | CompleteShapesCaptchaResponse500 | ShapesCaptchaResponse | None:
    r"""The shapes captcha requires just one image.

    ## Example Image
    <img src=\"https://www.eulerstream.com/_static/captchas/threed.png\" alt=\"Shapes Captcha Example\"
    width=\"480\" />

    ## Usage

    The solution to the shapes captcha are two points that need to be clicked. To use it in the GUI,
    convert the proportions to pixel values based on the image size.

    The `points` are returned as `x` and `y` proportions (0-1) of the width and height of the source
    image.
    The captcha image selector is `.captcha-verify-image`

    Args:
        body (CompleteShapesCaptchaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompleteShapesCaptchaResponse429 | CompleteShapesCaptchaResponse500 | ShapesCaptchaResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CompleteShapesCaptchaBody,
) -> Response[CompleteShapesCaptchaResponse429 | CompleteShapesCaptchaResponse500 | ShapesCaptchaResponse]:
    r"""The shapes captcha requires just one image.

    ## Example Image
    <img src=\"https://www.eulerstream.com/_static/captchas/threed.png\" alt=\"Shapes Captcha Example\"
    width=\"480\" />

    ## Usage

    The solution to the shapes captcha are two points that need to be clicked. To use it in the GUI,
    convert the proportions to pixel values based on the image size.

    The `points` are returned as `x` and `y` proportions (0-1) of the width and height of the source
    image.
    The captcha image selector is `.captcha-verify-image`

    Args:
        body (CompleteShapesCaptchaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompleteShapesCaptchaResponse429 | CompleteShapesCaptchaResponse500 | ShapesCaptchaResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CompleteShapesCaptchaBody,
) -> CompleteShapesCaptchaResponse429 | CompleteShapesCaptchaResponse500 | ShapesCaptchaResponse | None:
    r"""The shapes captcha requires just one image.

    ## Example Image
    <img src=\"https://www.eulerstream.com/_static/captchas/threed.png\" alt=\"Shapes Captcha Example\"
    width=\"480\" />

    ## Usage

    The solution to the shapes captcha are two points that need to be clicked. To use it in the GUI,
    convert the proportions to pixel values based on the image size.

    The `points` are returned as `x` and `y` proportions (0-1) of the width and height of the source
    image.
    The captcha image selector is `.captcha-verify-image`

    Args:
        body (CompleteShapesCaptchaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompleteShapesCaptchaResponse429 | CompleteShapesCaptchaResponse500 | ShapesCaptchaResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

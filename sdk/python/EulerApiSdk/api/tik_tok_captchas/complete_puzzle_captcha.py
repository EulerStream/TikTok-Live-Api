from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.complete_puzzle_captcha_body import CompletePuzzleCaptchaBody
from ...models.complete_puzzle_captcha_response_429 import CompletePuzzleCaptchaResponse429
from ...models.complete_puzzle_captcha_response_500 import CompletePuzzleCaptchaResponse500
from ...models.puzzle_captcha_response import PuzzleCaptchaResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CompletePuzzleCaptchaBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tiktok/captchas/puzzle",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CompletePuzzleCaptchaResponse429 | CompletePuzzleCaptchaResponse500 | PuzzleCaptchaResponse | None:
    if response.status_code == 200:
        response_200 = PuzzleCaptchaResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = CompletePuzzleCaptchaResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CompletePuzzleCaptchaResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CompletePuzzleCaptchaResponse429 | CompletePuzzleCaptchaResponse500 | PuzzleCaptchaResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CompletePuzzleCaptchaBody,
) -> Response[CompletePuzzleCaptchaResponse429 | CompletePuzzleCaptchaResponse500 | PuzzleCaptchaResponse]:
    r"""The puzzle captcha requires two images

    ## Example Image
    <img src=\"https://www.eulerstream.com/_static/captchas/puzzle.png\" alt=\"Puzzle Piece Example\"
    width=\"480\" />

    ## Usage

    The solution to the puzzle captcha is the distance to move the slider to fit the puzzle piece into
    the background.

    The `backgroundImage` is the full background image with the missing piece.
    The `pieceImage` is the small puzzle piece that needs to be fit into the background.

    The captcha image selectors are:
    - Background: `.captcha-verify-image`
    - Piece: `#captcha-verify-image ~ div.cap-absolute > img`

    The solution is the `x` proportion (0-1) of the width of the background image where the piece fits.
    It is 1:1 with the slider distance proportion.

    Args:
        body (CompletePuzzleCaptchaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompletePuzzleCaptchaResponse429 | CompletePuzzleCaptchaResponse500 | PuzzleCaptchaResponse]
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
    body: CompletePuzzleCaptchaBody,
) -> CompletePuzzleCaptchaResponse429 | CompletePuzzleCaptchaResponse500 | PuzzleCaptchaResponse | None:
    r"""The puzzle captcha requires two images

    ## Example Image
    <img src=\"https://www.eulerstream.com/_static/captchas/puzzle.png\" alt=\"Puzzle Piece Example\"
    width=\"480\" />

    ## Usage

    The solution to the puzzle captcha is the distance to move the slider to fit the puzzle piece into
    the background.

    The `backgroundImage` is the full background image with the missing piece.
    The `pieceImage` is the small puzzle piece that needs to be fit into the background.

    The captcha image selectors are:
    - Background: `.captcha-verify-image`
    - Piece: `#captcha-verify-image ~ div.cap-absolute > img`

    The solution is the `x` proportion (0-1) of the width of the background image where the piece fits.
    It is 1:1 with the slider distance proportion.

    Args:
        body (CompletePuzzleCaptchaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompletePuzzleCaptchaResponse429 | CompletePuzzleCaptchaResponse500 | PuzzleCaptchaResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CompletePuzzleCaptchaBody,
) -> Response[CompletePuzzleCaptchaResponse429 | CompletePuzzleCaptchaResponse500 | PuzzleCaptchaResponse]:
    r"""The puzzle captcha requires two images

    ## Example Image
    <img src=\"https://www.eulerstream.com/_static/captchas/puzzle.png\" alt=\"Puzzle Piece Example\"
    width=\"480\" />

    ## Usage

    The solution to the puzzle captcha is the distance to move the slider to fit the puzzle piece into
    the background.

    The `backgroundImage` is the full background image with the missing piece.
    The `pieceImage` is the small puzzle piece that needs to be fit into the background.

    The captcha image selectors are:
    - Background: `.captcha-verify-image`
    - Piece: `#captcha-verify-image ~ div.cap-absolute > img`

    The solution is the `x` proportion (0-1) of the width of the background image where the piece fits.
    It is 1:1 with the slider distance proportion.

    Args:
        body (CompletePuzzleCaptchaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompletePuzzleCaptchaResponse429 | CompletePuzzleCaptchaResponse500 | PuzzleCaptchaResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CompletePuzzleCaptchaBody,
) -> CompletePuzzleCaptchaResponse429 | CompletePuzzleCaptchaResponse500 | PuzzleCaptchaResponse | None:
    r"""The puzzle captcha requires two images

    ## Example Image
    <img src=\"https://www.eulerstream.com/_static/captchas/puzzle.png\" alt=\"Puzzle Piece Example\"
    width=\"480\" />

    ## Usage

    The solution to the puzzle captcha is the distance to move the slider to fit the puzzle piece into
    the background.

    The `backgroundImage` is the full background image with the missing piece.
    The `pieceImage` is the small puzzle piece that needs to be fit into the background.

    The captcha image selectors are:
    - Background: `.captcha-verify-image`
    - Piece: `#captcha-verify-image ~ div.cap-absolute > img`

    The solution is the `x` proportion (0-1) of the width of the background image where the piece fits.
    It is 1:1 with the slider distance proportion.

    Args:
        body (CompletePuzzleCaptchaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompletePuzzleCaptchaResponse429 | CompletePuzzleCaptchaResponse500 | PuzzleCaptchaResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

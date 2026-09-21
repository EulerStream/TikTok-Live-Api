from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_sensitive_word_response_429 import AddSensitiveWordResponse429
from ...models.add_sensitive_word_response_500 import AddSensitiveWordResponse500
from ...models.add_sensitive_word_response_503 import AddSensitiveWordResponse503
from ...models.room_add_sensitive_word_api_response import RoomAddSensitiveWordAPIResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    room_id: str,
    *,
    word: str,
    sec_anchor_id: str,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_oauth_token, Unset):
        headers["x-oauth-token"] = x_oauth_token

    if not isinstance(x_cookie_header, Unset):
        headers["x-cookie-header"] = x_cookie_header

    params: dict[str, Any] = {}

    params["word"] = word

    params["sec_anchor_id"] = sec_anchor_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webcast/rooms/{room_id}/moderation/sensitive-words".format(
            room_id=quote(str(room_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AddSensitiveWordResponse429
    | AddSensitiveWordResponse500
    | AddSensitiveWordResponse503
    | RoomAddSensitiveWordAPIResponse
    | None
):
    if response.status_code == 200:
        response_200 = RoomAddSensitiveWordAPIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = AddSensitiveWordResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = AddSensitiveWordResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = AddSensitiveWordResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AddSensitiveWordResponse429
    | AddSensitiveWordResponse500
    | AddSensitiveWordResponse503
    | RoomAddSensitiveWordAPIResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    room_id: str,
    *,
    client: AuthenticatedClient,
    word: str,
    sec_anchor_id: str,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Response[
    AddSensitiveWordResponse429
    | AddSensitiveWordResponse500
    | AddSensitiveWordResponse503
    | RoomAddSensitiveWordAPIResponse
]:
    """Add a sensitive word to a TikTok LIVE room's filter list.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        word (str):
        sec_anchor_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddSensitiveWordResponse429 | AddSensitiveWordResponse500 | AddSensitiveWordResponse503 | RoomAddSensitiveWordAPIResponse]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        word=word,
        sec_anchor_id=sec_anchor_id,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    room_id: str,
    *,
    client: AuthenticatedClient,
    word: str,
    sec_anchor_id: str,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> (
    AddSensitiveWordResponse429
    | AddSensitiveWordResponse500
    | AddSensitiveWordResponse503
    | RoomAddSensitiveWordAPIResponse
    | None
):
    """Add a sensitive word to a TikTok LIVE room's filter list.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        word (str):
        sec_anchor_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddSensitiveWordResponse429 | AddSensitiveWordResponse500 | AddSensitiveWordResponse503 | RoomAddSensitiveWordAPIResponse
    """

    return sync_detailed(
        room_id=room_id,
        client=client,
        word=word,
        sec_anchor_id=sec_anchor_id,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    ).parsed


async def asyncio_detailed(
    room_id: str,
    *,
    client: AuthenticatedClient,
    word: str,
    sec_anchor_id: str,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Response[
    AddSensitiveWordResponse429
    | AddSensitiveWordResponse500
    | AddSensitiveWordResponse503
    | RoomAddSensitiveWordAPIResponse
]:
    """Add a sensitive word to a TikTok LIVE room's filter list.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        word (str):
        sec_anchor_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddSensitiveWordResponse429 | AddSensitiveWordResponse500 | AddSensitiveWordResponse503 | RoomAddSensitiveWordAPIResponse]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        word=word,
        sec_anchor_id=sec_anchor_id,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    room_id: str,
    *,
    client: AuthenticatedClient,
    word: str,
    sec_anchor_id: str,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> (
    AddSensitiveWordResponse429
    | AddSensitiveWordResponse500
    | AddSensitiveWordResponse503
    | RoomAddSensitiveWordAPIResponse
    | None
):
    """Add a sensitive word to a TikTok LIVE room's filter list.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        word (str):
        sec_anchor_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddSensitiveWordResponse429 | AddSensitiveWordResponse500 | AddSensitiveWordResponse503 | RoomAddSensitiveWordAPIResponse
    """

    return (
        await asyncio_detailed(
            room_id=room_id,
            client=client,
            word=word,
            sec_anchor_id=sec_anchor_id,
            x_oauth_token=x_oauth_token,
            x_cookie_header=x_cookie_header,
        )
    ).parsed

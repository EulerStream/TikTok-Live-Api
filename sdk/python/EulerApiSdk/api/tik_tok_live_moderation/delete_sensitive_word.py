from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_sensitive_word_response_429 import DeleteSensitiveWordResponse429
from ...models.delete_sensitive_word_response_500 import DeleteSensitiveWordResponse500
from ...models.delete_sensitive_word_response_503 import DeleteSensitiveWordResponse503
from ...models.room_del_sensitive_word_api_response import RoomDelSensitiveWordAPIResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    room_id: str,
    *,
    word_id: str,
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

    params["word_id"] = word_id

    params["sec_anchor_id"] = sec_anchor_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
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
    DeleteSensitiveWordResponse429
    | DeleteSensitiveWordResponse500
    | DeleteSensitiveWordResponse503
    | RoomDelSensitiveWordAPIResponse
    | None
):
    if response.status_code == 200:
        response_200 = RoomDelSensitiveWordAPIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = DeleteSensitiveWordResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = DeleteSensitiveWordResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteSensitiveWordResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteSensitiveWordResponse429
    | DeleteSensitiveWordResponse500
    | DeleteSensitiveWordResponse503
    | RoomDelSensitiveWordAPIResponse
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
    word_id: str,
    sec_anchor_id: str,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Response[
    DeleteSensitiveWordResponse429
    | DeleteSensitiveWordResponse500
    | DeleteSensitiveWordResponse503
    | RoomDelSensitiveWordAPIResponse
]:
    """Delete a sensitive word from a TikTok LIVE room's filter list.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        word_id (str):
        sec_anchor_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSensitiveWordResponse429 | DeleteSensitiveWordResponse500 | DeleteSensitiveWordResponse503 | RoomDelSensitiveWordAPIResponse]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        word_id=word_id,
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
    word_id: str,
    sec_anchor_id: str,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> (
    DeleteSensitiveWordResponse429
    | DeleteSensitiveWordResponse500
    | DeleteSensitiveWordResponse503
    | RoomDelSensitiveWordAPIResponse
    | None
):
    """Delete a sensitive word from a TikTok LIVE room's filter list.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        word_id (str):
        sec_anchor_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSensitiveWordResponse429 | DeleteSensitiveWordResponse500 | DeleteSensitiveWordResponse503 | RoomDelSensitiveWordAPIResponse
    """

    return sync_detailed(
        room_id=room_id,
        client=client,
        word_id=word_id,
        sec_anchor_id=sec_anchor_id,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    ).parsed


async def asyncio_detailed(
    room_id: str,
    *,
    client: AuthenticatedClient,
    word_id: str,
    sec_anchor_id: str,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Response[
    DeleteSensitiveWordResponse429
    | DeleteSensitiveWordResponse500
    | DeleteSensitiveWordResponse503
    | RoomDelSensitiveWordAPIResponse
]:
    """Delete a sensitive word from a TikTok LIVE room's filter list.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        word_id (str):
        sec_anchor_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSensitiveWordResponse429 | DeleteSensitiveWordResponse500 | DeleteSensitiveWordResponse503 | RoomDelSensitiveWordAPIResponse]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        word_id=word_id,
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
    word_id: str,
    sec_anchor_id: str,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> (
    DeleteSensitiveWordResponse429
    | DeleteSensitiveWordResponse500
    | DeleteSensitiveWordResponse503
    | RoomDelSensitiveWordAPIResponse
    | None
):
    """Delete a sensitive word from a TikTok LIVE room's filter list.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        word_id (str):
        sec_anchor_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSensitiveWordResponse429 | DeleteSensitiveWordResponse500 | DeleteSensitiveWordResponse503 | RoomDelSensitiveWordAPIResponse
    """

    return (
        await asyncio_detailed(
            room_id=room_id,
            client=client,
            word_id=word_id,
            sec_anchor_id=sec_anchor_id,
            x_oauth_token=x_oauth_token,
            x_cookie_header=x_cookie_header,
        )
    ).parsed

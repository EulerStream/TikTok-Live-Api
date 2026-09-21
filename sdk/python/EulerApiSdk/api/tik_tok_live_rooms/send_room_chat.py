from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.send_room_chat_response_429 import SendRoomChatResponse429
from ...models.send_room_chat_response_500 import SendRoomChatResponse500
from ...models.send_room_chat_response_503 import SendRoomChatResponse503
from ...models.webcast_room_chat_payload import WebcastRoomChatPayload
from ...models.webcast_room_chat_payload_v1 import WebcastRoomChatPayloadV1
from ...models.webcast_room_chat_route_response import WebcastRoomChatRouteResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    room_id: str,
    *,
    body: WebcastRoomChatPayload | WebcastRoomChatPayloadV1,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_oauth_token, Unset):
        headers["x-oauth-token"] = x_oauth_token

    if not isinstance(x_cookie_header, Unset):
        headers["x-cookie-header"] = x_cookie_header

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webcast/rooms/{room_id}/chat".format(
            room_id=quote(str(room_id), safe=""),
        ),
    }

    if isinstance(body, WebcastRoomChatPayloadV1):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SendRoomChatResponse429 | SendRoomChatResponse500 | SendRoomChatResponse503 | WebcastRoomChatRouteResponse | None:
    if response.status_code == 200:
        response_200 = WebcastRoomChatRouteResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = SendRoomChatResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = SendRoomChatResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = SendRoomChatResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    SendRoomChatResponse429 | SendRoomChatResponse500 | SendRoomChatResponse503 | WebcastRoomChatRouteResponse
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
    body: WebcastRoomChatPayload | WebcastRoomChatPayloadV1,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Response[
    SendRoomChatResponse429 | SendRoomChatResponse500 | SendRoomChatResponse503 | WebcastRoomChatRouteResponse
]:
    """Send a chat to a TikTok LIVE room.

    Either `targetRoomId` or `targetUniqueId` must be provided to identify the room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        body (WebcastRoomChatPayload | WebcastRoomChatPayloadV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SendRoomChatResponse429 | SendRoomChatResponse500 | SendRoomChatResponse503 | WebcastRoomChatRouteResponse]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        body=body,
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
    body: WebcastRoomChatPayload | WebcastRoomChatPayloadV1,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> SendRoomChatResponse429 | SendRoomChatResponse500 | SendRoomChatResponse503 | WebcastRoomChatRouteResponse | None:
    """Send a chat to a TikTok LIVE room.

    Either `targetRoomId` or `targetUniqueId` must be provided to identify the room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        body (WebcastRoomChatPayload | WebcastRoomChatPayloadV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SendRoomChatResponse429 | SendRoomChatResponse500 | SendRoomChatResponse503 | WebcastRoomChatRouteResponse
    """

    return sync_detailed(
        room_id=room_id,
        client=client,
        body=body,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    ).parsed


async def asyncio_detailed(
    room_id: str,
    *,
    client: AuthenticatedClient,
    body: WebcastRoomChatPayload | WebcastRoomChatPayloadV1,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Response[
    SendRoomChatResponse429 | SendRoomChatResponse500 | SendRoomChatResponse503 | WebcastRoomChatRouteResponse
]:
    """Send a chat to a TikTok LIVE room.

    Either `targetRoomId` or `targetUniqueId` must be provided to identify the room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        body (WebcastRoomChatPayload | WebcastRoomChatPayloadV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SendRoomChatResponse429 | SendRoomChatResponse500 | SendRoomChatResponse503 | WebcastRoomChatRouteResponse]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        body=body,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    room_id: str,
    *,
    client: AuthenticatedClient,
    body: WebcastRoomChatPayload | WebcastRoomChatPayloadV1,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> SendRoomChatResponse429 | SendRoomChatResponse500 | SendRoomChatResponse503 | WebcastRoomChatRouteResponse | None:
    """Send a chat to a TikTok LIVE room.

    Either `targetRoomId` or `targetUniqueId` must be provided to identify the room.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        room_id (str):
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        body (WebcastRoomChatPayload | WebcastRoomChatPayloadV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SendRoomChatResponse429 | SendRoomChatResponse500 | SendRoomChatResponse503 | WebcastRoomChatRouteResponse
    """

    return (
        await asyncio_detailed(
            room_id=room_id,
            client=client,
            body=body,
            x_oauth_token=x_oauth_token,
            x_cookie_header=x_cookie_header,
        )
    ).parsed

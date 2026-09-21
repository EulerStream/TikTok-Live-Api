from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_bulk_live_check_payload import RetrieveBulkLiveCheckPayload
from ...models.retrieve_bulk_live_check_payload_v1 import RetrieveBulkLiveCheckPayloadV1
from ...models.retrieve_bulk_live_check_response import RetrieveBulkLiveCheckResponse
from ...models.retrieve_bulk_live_check_response_429 import RetrieveBulkLiveCheckResponse429
from ...models.retrieve_bulk_live_check_response_500 import RetrieveBulkLiveCheckResponse500
from ...models.retrieve_bulk_live_check_response_503 import RetrieveBulkLiveCheckResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RetrieveBulkLiveCheckPayload | RetrieveBulkLiveCheckPayloadV1,
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
        "url": "/webcast/bulk_live_check",
    }

    if isinstance(body, RetrieveBulkLiveCheckPayloadV1):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RetrieveBulkLiveCheckResponse
    | RetrieveBulkLiveCheckResponse429
    | RetrieveBulkLiveCheckResponse500
    | RetrieveBulkLiveCheckResponse503
    | None
):
    if response.status_code == 200:
        response_200 = RetrieveBulkLiveCheckResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveBulkLiveCheckResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveBulkLiveCheckResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RetrieveBulkLiveCheckResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RetrieveBulkLiveCheckResponse
    | RetrieveBulkLiveCheckResponse429
    | RetrieveBulkLiveCheckResponse500
    | RetrieveBulkLiveCheckResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RetrieveBulkLiveCheckPayload | RetrieveBulkLiveCheckPayloadV1,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Response[
    RetrieveBulkLiveCheckResponse
    | RetrieveBulkLiveCheckResponse429
    | RetrieveBulkLiveCheckResponse500
    | RetrieveBulkLiveCheckResponse503
]:
    """A bulk-check endpoint to determine if a group of TikTok users (up to 50 at once) are live.
    It uses a highly optimized job-based system for checking large numbers of users quickly.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        body (RetrieveBulkLiveCheckPayload | RetrieveBulkLiveCheckPayloadV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveBulkLiveCheckResponse | RetrieveBulkLiveCheckResponse429 | RetrieveBulkLiveCheckResponse500 | RetrieveBulkLiveCheckResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RetrieveBulkLiveCheckPayload | RetrieveBulkLiveCheckPayloadV1,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> (
    RetrieveBulkLiveCheckResponse
    | RetrieveBulkLiveCheckResponse429
    | RetrieveBulkLiveCheckResponse500
    | RetrieveBulkLiveCheckResponse503
    | None
):
    """A bulk-check endpoint to determine if a group of TikTok users (up to 50 at once) are live.
    It uses a highly optimized job-based system for checking large numbers of users quickly.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        body (RetrieveBulkLiveCheckPayload | RetrieveBulkLiveCheckPayloadV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveBulkLiveCheckResponse | RetrieveBulkLiveCheckResponse429 | RetrieveBulkLiveCheckResponse500 | RetrieveBulkLiveCheckResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RetrieveBulkLiveCheckPayload | RetrieveBulkLiveCheckPayloadV1,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> Response[
    RetrieveBulkLiveCheckResponse
    | RetrieveBulkLiveCheckResponse429
    | RetrieveBulkLiveCheckResponse500
    | RetrieveBulkLiveCheckResponse503
]:
    """A bulk-check endpoint to determine if a group of TikTok users (up to 50 at once) are live.
    It uses a highly optimized job-based system for checking large numbers of users quickly.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        body (RetrieveBulkLiveCheckPayload | RetrieveBulkLiveCheckPayloadV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveBulkLiveCheckResponse | RetrieveBulkLiveCheckResponse429 | RetrieveBulkLiveCheckResponse500 | RetrieveBulkLiveCheckResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
        x_oauth_token=x_oauth_token,
        x_cookie_header=x_cookie_header,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RetrieveBulkLiveCheckPayload | RetrieveBulkLiveCheckPayloadV1,
    x_oauth_token: str | Unset = UNSET,
    x_cookie_header: str | Unset = UNSET,
) -> (
    RetrieveBulkLiveCheckResponse
    | RetrieveBulkLiveCheckResponse429
    | RetrieveBulkLiveCheckResponse500
    | RetrieveBulkLiveCheckResponse503
    | None
):
    """A bulk-check endpoint to determine if a group of TikTok users (up to 50 at once) are live.
    It uses a highly optimized job-based system for checking large numbers of users quickly.

    **Authentication:** Provide exactly one of the following headers:
    - `x-oauth-token`: An OAuth access token. The sessionId and ttTargetIdc are resolved from the stored
    OAuth session. [Read More](https://www.eulerstream.com/docs/oauth)
    - `x-cookie-header`: A cookie header string containing `sessionid` and `tt-target-idc` cookies from
    TikTok.

    Args:
        x_oauth_token (str | Unset):
        x_cookie_header (str | Unset):
        body (RetrieveBulkLiveCheckPayload | RetrieveBulkLiveCheckPayloadV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveBulkLiveCheckResponse | RetrieveBulkLiveCheckResponse429 | RetrieveBulkLiveCheckResponse500 | RetrieveBulkLiveCheckResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_oauth_token=x_oauth_token,
            x_cookie_header=x_cookie_header,
        )
    ).parsed

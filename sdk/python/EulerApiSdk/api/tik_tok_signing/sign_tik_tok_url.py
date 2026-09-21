from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sign_tik_tok_url_body import SignTikTokUrlBody
from ...models.sign_tik_tok_url_response import SignTikTokUrlResponse
from ...models.sign_tik_tok_url_response_429 import SignTikTokUrlResponse429
from ...models.sign_tik_tok_url_response_500 import SignTikTokUrlResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SignTikTokUrlBody,
    client_query: str | Unset = "ttlive-other",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["client"] = client_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tiktok/signing/encrypt/sign_url",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SignTikTokUrlResponse | SignTikTokUrlResponse429 | SignTikTokUrlResponse500 | None:
    if response.status_code == 200:
        response_200 = SignTikTokUrlResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = SignTikTokUrlResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = SignTikTokUrlResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SignTikTokUrlResponse | SignTikTokUrlResponse429 | SignTikTokUrlResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SignTikTokUrlBody,
    client_query: str | Unset = "ttlive-other",
) -> Response[SignTikTokUrlResponse | SignTikTokUrlResponse429 | SignTikTokUrlResponse500]:
    """Sign a non-LIVE TikTok URL. This is NOT available to customers in any public package, and access is
    approved on a case-by-case basis.

    Args:
        client_query (str | Unset):  Default: 'ttlive-other'.
        body (SignTikTokUrlBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SignTikTokUrlResponse | SignTikTokUrlResponse429 | SignTikTokUrlResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
        client_query=client_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SignTikTokUrlBody,
    client_query: str | Unset = "ttlive-other",
) -> SignTikTokUrlResponse | SignTikTokUrlResponse429 | SignTikTokUrlResponse500 | None:
    """Sign a non-LIVE TikTok URL. This is NOT available to customers in any public package, and access is
    approved on a case-by-case basis.

    Args:
        client_query (str | Unset):  Default: 'ttlive-other'.
        body (SignTikTokUrlBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SignTikTokUrlResponse | SignTikTokUrlResponse429 | SignTikTokUrlResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
        client_query=client_query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SignTikTokUrlBody,
    client_query: str | Unset = "ttlive-other",
) -> Response[SignTikTokUrlResponse | SignTikTokUrlResponse429 | SignTikTokUrlResponse500]:
    """Sign a non-LIVE TikTok URL. This is NOT available to customers in any public package, and access is
    approved on a case-by-case basis.

    Args:
        client_query (str | Unset):  Default: 'ttlive-other'.
        body (SignTikTokUrlBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SignTikTokUrlResponse | SignTikTokUrlResponse429 | SignTikTokUrlResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
        client_query=client_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SignTikTokUrlBody,
    client_query: str | Unset = "ttlive-other",
) -> SignTikTokUrlResponse | SignTikTokUrlResponse429 | SignTikTokUrlResponse500 | None:
    """Sign a non-LIVE TikTok URL. This is NOT available to customers in any public package, and access is
    approved on a case-by-case basis.

    Args:
        client_query (str | Unset):  Default: 'ttlive-other'.
        body (SignTikTokUrlBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SignTikTokUrlResponse | SignTikTokUrlResponse429 | SignTikTokUrlResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            client_query=client_query,
        )
    ).parsed

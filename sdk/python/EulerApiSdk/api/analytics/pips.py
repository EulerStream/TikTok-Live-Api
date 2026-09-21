from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pip_response import PipResponse
from ...models.pips_response_429 import PipsResponse429
from ...models.pips_response_500 import PipsResponse500
from ...models.tik_tok_sign_live_client import TikTokSignLiveClient
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    label_colour: str | Unset = "#555",
    value_colour: str | Unset = "#007ec6",
    hours: float | Unset = 1.0,
    client_query: TikTokSignLiveClient | Unset = UNSET,
    json: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["labelColour"] = label_colour

    params["valueColour"] = value_colour

    params["hours"] = hours

    json_client_query: str | Unset = UNSET
    if not isinstance(client_query, Unset):
        json_client_query = client_query.value

    params["client"] = json_client_query

    params["json"] = json

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/pips",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PipResponse | str | PipsResponse429 | PipsResponse500 | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> PipResponse | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = PipResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(PipResponse | str, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = PipsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PipsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PipResponse | str | PipsResponse429 | PipsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    label_colour: str | Unset = "#555",
    value_colour: str | Unset = "#007ec6",
    hours: float | Unset = 1.0,
    client_query: TikTokSignLiveClient | Unset = UNSET,
    json: bool | Unset = False,
) -> Response[PipResponse | str | PipsResponse429 | PipsResponse500]:
    """Retrieve stats as an SVG

    Args:
        label_colour (str | Unset):  Default: '#555'.
        value_colour (str | Unset):  Default: '#007ec6'.
        hours (float | Unset):  Default: 1.0.
        client_query (TikTokSignLiveClient | Unset): Logical "client name" recorded against each
            request — supplied by the caller via the `metadata.client_name` RPC field. Free-form on
            the wire, but conventionally one of the values below.
        json (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PipResponse | str | PipsResponse429 | PipsResponse500]
    """

    kwargs = _get_kwargs(
        label_colour=label_colour,
        value_colour=value_colour,
        hours=hours,
        client_query=client_query,
        json=json,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    label_colour: str | Unset = "#555",
    value_colour: str | Unset = "#007ec6",
    hours: float | Unset = 1.0,
    client_query: TikTokSignLiveClient | Unset = UNSET,
    json: bool | Unset = False,
) -> PipResponse | str | PipsResponse429 | PipsResponse500 | None:
    """Retrieve stats as an SVG

    Args:
        label_colour (str | Unset):  Default: '#555'.
        value_colour (str | Unset):  Default: '#007ec6'.
        hours (float | Unset):  Default: 1.0.
        client_query (TikTokSignLiveClient | Unset): Logical "client name" recorded against each
            request — supplied by the caller via the `metadata.client_name` RPC field. Free-form on
            the wire, but conventionally one of the values below.
        json (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PipResponse | str | PipsResponse429 | PipsResponse500
    """

    return sync_detailed(
        client=client,
        label_colour=label_colour,
        value_colour=value_colour,
        hours=hours,
        client_query=client_query,
        json=json,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    label_colour: str | Unset = "#555",
    value_colour: str | Unset = "#007ec6",
    hours: float | Unset = 1.0,
    client_query: TikTokSignLiveClient | Unset = UNSET,
    json: bool | Unset = False,
) -> Response[PipResponse | str | PipsResponse429 | PipsResponse500]:
    """Retrieve stats as an SVG

    Args:
        label_colour (str | Unset):  Default: '#555'.
        value_colour (str | Unset):  Default: '#007ec6'.
        hours (float | Unset):  Default: 1.0.
        client_query (TikTokSignLiveClient | Unset): Logical "client name" recorded against each
            request — supplied by the caller via the `metadata.client_name` RPC field. Free-form on
            the wire, but conventionally one of the values below.
        json (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PipResponse | str | PipsResponse429 | PipsResponse500]
    """

    kwargs = _get_kwargs(
        label_colour=label_colour,
        value_colour=value_colour,
        hours=hours,
        client_query=client_query,
        json=json,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    label_colour: str | Unset = "#555",
    value_colour: str | Unset = "#007ec6",
    hours: float | Unset = 1.0,
    client_query: TikTokSignLiveClient | Unset = UNSET,
    json: bool | Unset = False,
) -> PipResponse | str | PipsResponse429 | PipsResponse500 | None:
    """Retrieve stats as an SVG

    Args:
        label_colour (str | Unset):  Default: '#555'.
        value_colour (str | Unset):  Default: '#007ec6'.
        hours (float | Unset):  Default: 1.0.
        client_query (TikTokSignLiveClient | Unset): Logical "client name" recorded against each
            request — supplied by the caller via the `metadata.client_name` RPC field. Free-form on
            the wire, but conventionally one of the values below.
        json (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PipResponse | str | PipsResponse429 | PipsResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            label_colour=label_colour,
            value_colour=value_colour,
            hours=hours,
            client_query=client_query,
            json=json,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agency_apply_url_response import AgencyApplyUrlResponse
from ...models.retrieve_agency_apply_url_response_429 import RetrieveAgencyApplyUrlResponse429
from ...models.retrieve_agency_apply_url_response_500 import RetrieveAgencyApplyUrlResponse500
from ...models.retrieve_agency_apply_url_response_503 import RetrieveAgencyApplyUrlResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agency_id: float,
    *,
    redirect: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["redirect"] = redirect

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/agencies/catalog/{agency_id}/apply_url".format(
            agency_id=quote(str(agency_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AgencyApplyUrlResponse
    | Any
    | RetrieveAgencyApplyUrlResponse429
    | RetrieveAgencyApplyUrlResponse500
    | RetrieveAgencyApplyUrlResponse503
    | None
):
    if response.status_code == 200:

        def _parse_response_200(data: object) -> AgencyApplyUrlResponse | Any:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = AgencyApplyUrlResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgencyApplyUrlResponse | Any, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = RetrieveAgencyApplyUrlResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RetrieveAgencyApplyUrlResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RetrieveAgencyApplyUrlResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AgencyApplyUrlResponse
    | Any
    | RetrieveAgencyApplyUrlResponse429
    | RetrieveAgencyApplyUrlResponse500
    | RetrieveAgencyApplyUrlResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agency_id: float,
    *,
    client: AuthenticatedClient,
    redirect: bool | Unset = False,
) -> Response[
    AgencyApplyUrlResponse
    | Any
    | RetrieveAgencyApplyUrlResponse429
    | RetrieveAgencyApplyUrlResponse500
    | RetrieveAgencyApplyUrlResponse503
]:
    """Retrieve the application (recruitment) URL for a TikTok LIVE agency. This is the URL an agency's QR
    code points prospective creators at.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        agency_id (float):
        redirect (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgencyApplyUrlResponse | Any | RetrieveAgencyApplyUrlResponse429 | RetrieveAgencyApplyUrlResponse500 | RetrieveAgencyApplyUrlResponse503]
    """

    kwargs = _get_kwargs(
        agency_id=agency_id,
        redirect=redirect,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agency_id: float,
    *,
    client: AuthenticatedClient,
    redirect: bool | Unset = False,
) -> (
    AgencyApplyUrlResponse
    | Any
    | RetrieveAgencyApplyUrlResponse429
    | RetrieveAgencyApplyUrlResponse500
    | RetrieveAgencyApplyUrlResponse503
    | None
):
    """Retrieve the application (recruitment) URL for a TikTok LIVE agency. This is the URL an agency's QR
    code points prospective creators at.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        agency_id (float):
        redirect (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgencyApplyUrlResponse | Any | RetrieveAgencyApplyUrlResponse429 | RetrieveAgencyApplyUrlResponse500 | RetrieveAgencyApplyUrlResponse503
    """

    return sync_detailed(
        agency_id=agency_id,
        client=client,
        redirect=redirect,
    ).parsed


async def asyncio_detailed(
    agency_id: float,
    *,
    client: AuthenticatedClient,
    redirect: bool | Unset = False,
) -> Response[
    AgencyApplyUrlResponse
    | Any
    | RetrieveAgencyApplyUrlResponse429
    | RetrieveAgencyApplyUrlResponse500
    | RetrieveAgencyApplyUrlResponse503
]:
    """Retrieve the application (recruitment) URL for a TikTok LIVE agency. This is the URL an agency's QR
    code points prospective creators at.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        agency_id (float):
        redirect (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgencyApplyUrlResponse | Any | RetrieveAgencyApplyUrlResponse429 | RetrieveAgencyApplyUrlResponse500 | RetrieveAgencyApplyUrlResponse503]
    """

    kwargs = _get_kwargs(
        agency_id=agency_id,
        redirect=redirect,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agency_id: float,
    *,
    client: AuthenticatedClient,
    redirect: bool | Unset = False,
) -> (
    AgencyApplyUrlResponse
    | Any
    | RetrieveAgencyApplyUrlResponse429
    | RetrieveAgencyApplyUrlResponse500
    | RetrieveAgencyApplyUrlResponse503
    | None
):
    """Retrieve the application (recruitment) URL for a TikTok LIVE agency. This is the URL an agency's QR
    code points prospective creators at.

    Requests to catalogue endpoints do NOT count towards normal API limits.

    Args:
        agency_id (float):
        redirect (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgencyApplyUrlResponse | Any | RetrieveAgencyApplyUrlResponse429 | RetrieveAgencyApplyUrlResponse500 | RetrieveAgencyApplyUrlResponse503
    """

    return (
        await asyncio_detailed(
            agency_id=agency_id,
            client=client,
            redirect=redirect,
        )
    ).parsed

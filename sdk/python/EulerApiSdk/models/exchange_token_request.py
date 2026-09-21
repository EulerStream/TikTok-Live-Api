from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.exchange_token_request_grant_type import ExchangeTokenRequestGrantType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExchangeTokenRequest")


@_attrs_define
class ExchangeTokenRequest:
    """
    Attributes:
        client_id (str):
        client_secret (str):
        grant_type (ExchangeTokenRequestGrantType):
        code (str | Unset): Required for authorization_code grant
        redirect_uri (str | Unset): Required for authorization_code grant
        refresh_token (str | Unset): Required for refresh_token grant
    """

    client_id: str
    client_secret: str
    grant_type: ExchangeTokenRequestGrantType
    code: str | Unset = UNSET
    redirect_uri: str | Unset = UNSET
    refresh_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        client_secret = self.client_secret

        grant_type = self.grant_type.value

        code = self.code

        redirect_uri = self.redirect_uri

        refresh_token = self.refresh_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client_id": client_id,
                "client_secret": client_secret,
                "grant_type": grant_type,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if redirect_uri is not UNSET:
            field_dict["redirect_uri"] = redirect_uri
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("client_id")

        client_secret = d.pop("client_secret")

        grant_type = ExchangeTokenRequestGrantType(d.pop("grant_type"))

        code = d.pop("code", UNSET)

        redirect_uri = d.pop("redirect_uri", UNSET)

        refresh_token = d.pop("refresh_token", UNSET)

        exchange_token_request = cls(
            client_id=client_id,
            client_secret=client_secret,
            grant_type=grant_type,
            code=code,
            redirect_uri=redirect_uri,
            refresh_token=refresh_token,
        )

        exchange_token_request.additional_properties = d
        return exchange_token_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

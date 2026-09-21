from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.o_auth_scope import OAuthScope
from ..models.token_response_token_type import TokenResponseTokenType

T = TypeVar("T", bound="TokenResponse")


@_attrs_define
class TokenResponse:
    """
    Attributes:
        access_token (str):
        refresh_token (str):
        token_type (TokenResponseTokenType):
        expires_in (float): Access token lifetime in seconds
        refresh_expires_in (float): Refresh token lifetime in seconds
        scopes (list[OAuthScope]):
    """

    access_token: str
    refresh_token: str
    token_type: TokenResponseTokenType
    expires_in: float
    refresh_expires_in: float
    scopes: list[OAuthScope]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        refresh_token = self.refresh_token

        token_type = self.token_type.value

        expires_in = self.expires_in

        refresh_expires_in = self.refresh_expires_in

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.value
            scopes.append(scopes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": token_type,
                "expires_in": expires_in,
                "refresh_expires_in": refresh_expires_in,
                "scopes": scopes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("access_token")

        refresh_token = d.pop("refresh_token")

        token_type = TokenResponseTokenType(d.pop("token_type"))

        expires_in = d.pop("expires_in")

        refresh_expires_in = d.pop("refresh_expires_in")

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = OAuthScope(scopes_item_data)

            scopes.append(scopes_item)

        token_response = cls(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type=token_type,
            expires_in=expires_in,
            refresh_expires_in=refresh_expires_in,
            scopes=scopes,
        )

        token_response.additional_properties = d
        return token_response

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

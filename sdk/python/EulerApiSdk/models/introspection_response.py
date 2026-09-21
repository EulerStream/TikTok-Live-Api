from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.introspection_response_token_type import IntrospectionResponseTokenType
from ..types import UNSET, Unset

T = TypeVar("T", bound="IntrospectionResponse")


@_attrs_define
class IntrospectionResponse:
    """RFC 7662 Token Introspection response

    Attributes:
        active (bool):
        scope (str | Unset):
        client_id (str | Unset):
        token_type (IntrospectionResponseTokenType | Unset):
        exp (float | Unset):
        iat (float | Unset):
        sub (str | Unset):
    """

    active: bool
    scope: str | Unset = UNSET
    client_id: str | Unset = UNSET
    token_type: IntrospectionResponseTokenType | Unset = UNSET
    exp: float | Unset = UNSET
    iat: float | Unset = UNSET
    sub: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        scope = self.scope

        client_id = self.client_id

        token_type: str | Unset = UNSET
        if not isinstance(self.token_type, Unset):
            token_type = self.token_type.value

        exp = self.exp

        iat = self.iat

        sub = self.sub

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
            }
        )
        if scope is not UNSET:
            field_dict["scope"] = scope
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if token_type is not UNSET:
            field_dict["token_type"] = token_type
        if exp is not UNSET:
            field_dict["exp"] = exp
        if iat is not UNSET:
            field_dict["iat"] = iat
        if sub is not UNSET:
            field_dict["sub"] = sub

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active")

        scope = d.pop("scope", UNSET)

        client_id = d.pop("client_id", UNSET)

        _token_type = d.pop("token_type", UNSET)
        token_type: IntrospectionResponseTokenType | Unset
        if isinstance(_token_type, Unset):
            token_type = UNSET
        else:
            token_type = IntrospectionResponseTokenType(_token_type)

        exp = d.pop("exp", UNSET)

        iat = d.pop("iat", UNSET)

        sub = d.pop("sub", UNSET)

        introspection_response = cls(
            active=active,
            scope=scope,
            client_id=client_id,
            token_type=token_type,
            exp=exp,
            iat=iat,
            sub=sub,
        )

        introspection_response.additional_properties = d
        return introspection_response

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

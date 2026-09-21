from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.introspect_request_body_token_type_hint import IntrospectRequestBodyTokenTypeHint
from ..types import UNSET, Unset

T = TypeVar("T", bound="IntrospectRequestBody")


@_attrs_define
class IntrospectRequestBody:
    """
    Attributes:
        token (str):
        client_id (str):
        client_secret (str):
        token_type_hint (IntrospectRequestBodyTokenTypeHint | Unset):
    """

    token: str
    client_id: str
    client_secret: str
    token_type_hint: IntrospectRequestBodyTokenTypeHint | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        client_id = self.client_id

        client_secret = self.client_secret

        token_type_hint: str | Unset = UNSET
        if not isinstance(self.token_type_hint, Unset):
            token_type_hint = self.token_type_hint.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "client_id": client_id,
                "client_secret": client_secret,
            }
        )
        if token_type_hint is not UNSET:
            field_dict["token_type_hint"] = token_type_hint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token")

        client_id = d.pop("client_id")

        client_secret = d.pop("client_secret")

        _token_type_hint = d.pop("token_type_hint", UNSET)
        token_type_hint: IntrospectRequestBodyTokenTypeHint | Unset
        if isinstance(_token_type_hint, Unset):
            token_type_hint = UNSET
        else:
            token_type_hint = IntrospectRequestBodyTokenTypeHint(_token_type_hint)

        introspect_request_body = cls(
            token=token,
            client_id=client_id,
            client_secret=client_secret,
            token_type_hint=token_type_hint,
        )

        introspect_request_body.additional_properties = d
        return introspect_request_body

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

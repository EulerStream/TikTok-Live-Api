from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_key import ApiKey


T = TypeVar("T", bound="RetrieveKeyResponse")


@_attrs_define
class RetrieveKeyResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        key (ApiKey | Unset):
    """

    code: float
    message: str | Unset = UNSET
    key: ApiKey | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        key: dict[str, Any] | Unset = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key import ApiKey  # noqa: PLC0415

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _key = d.pop("key", UNSET)
        key: ApiKey | Unset
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = ApiKey.from_dict(_key)

        retrieve_key_response = cls(
            code=code,
            message=message,
            key=key,
        )

        retrieve_key_response.additional_properties = d
        return retrieve_key_response

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

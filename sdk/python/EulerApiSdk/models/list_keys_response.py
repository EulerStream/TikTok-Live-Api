from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_key import ApiKey


T = TypeVar("T", bound="ListKeysResponse")


@_attrs_define
class ListKeysResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        keys (list[ApiKey] | Unset):
    """

    code: float
    message: str | Unset = UNSET
    keys: list[ApiKey] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        keys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.keys, Unset):
            keys = []
            for keys_item_data in self.keys:
                keys_item = keys_item_data.to_dict()
                keys.append(keys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if keys is not UNSET:
            field_dict["keys"] = keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key import ApiKey

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _keys = d.pop("keys", UNSET)
        keys: list[ApiKey] | Unset = UNSET
        if _keys is not UNSET:
            keys = []
            for keys_item_data in _keys:
                keys_item = ApiKey.from_dict(keys_item_data)

                keys.append(keys_item)

        list_keys_response = cls(
            code=code,
            message=message,
            keys=keys,
        )

        list_keys_response.additional_properties = d
        return list_keys_response

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

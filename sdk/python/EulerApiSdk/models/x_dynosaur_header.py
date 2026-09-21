from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="XDynosaurHeader")


@_attrs_define
class XDynosaurHeader:
    """
    Attributes:
        prefix (str): The raw header byte, as `0x..`.
        sign_type (float):
        has_flag_8 (bool):
        mode (float):
    """

    prefix: str
    sign_type: float
    has_flag_8: bool
    mode: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prefix = self.prefix

        sign_type = self.sign_type

        has_flag_8 = self.has_flag_8

        mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prefix": prefix,
                "signType": sign_type,
                "hasFlag8": has_flag_8,
                "mode": mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prefix = d.pop("prefix")

        sign_type = d.pop("signType")

        has_flag_8 = d.pop("hasFlag8")

        mode = d.pop("mode")

        x_dynosaur_header = cls(
            prefix=prefix,
            sign_type=sign_type,
            has_flag_8=has_flag_8,
            mode=mode,
        )

        x_dynosaur_header.additional_properties = d
        return x_dynosaur_header

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

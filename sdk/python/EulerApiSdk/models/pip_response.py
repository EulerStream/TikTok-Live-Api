from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PipResponse")


@_attrs_define
class PipResponse:
    """
    Attributes:
        code (float):
        image_url (str):
        label (str):
        value (float):
        unit (str):
        message (str | Unset):
    """

    code: float
    image_url: str
    label: str
    value: float
    unit: str
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        image_url = self.image_url

        label = self.label

        value = self.value

        unit = self.unit

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "image_url": image_url,
                "label": label,
                "value": value,
                "unit": unit,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        image_url = d.pop("image_url")

        label = d.pop("label")

        value = d.pop("value")

        unit = d.pop("unit")

        message = d.pop("message", UNSET)

        pip_response = cls(
            code=code,
            image_url=image_url,
            label=label,
            value=value,
            unit=unit,
            message=message,
        )

        pip_response.additional_properties = d
        return pip_response

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

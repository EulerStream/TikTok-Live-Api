from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RateLimitInfo")


@_attrs_define
class RateLimitInfo:
    """
    Attributes:
        max_ (float):
        remaining (float):
        reset_at (None | str):
    """

    max_: float
    remaining: float
    reset_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_ = self.max_

        remaining = self.remaining

        reset_at: None | str
        reset_at = self.reset_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "max": max_,
                "remaining": remaining,
                "reset_at": reset_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_ = d.pop("max")

        remaining = d.pop("remaining")

        def _parse_reset_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reset_at = _parse_reset_at(d.pop("reset_at"))

        rate_limit_info = cls(
            max_=max_,
            remaining=remaining,
            reset_at=reset_at,
        )

        rate_limit_info.additional_properties = d
        return rate_limit_info

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

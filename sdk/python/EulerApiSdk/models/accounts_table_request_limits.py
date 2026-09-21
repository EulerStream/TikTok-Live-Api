from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AccountsTableRequestLimits")


@_attrs_define
class AccountsTableRequestLimits:
    """
    Attributes:
        day (float):
        hour (float):
        minute (float):
    """

    day: float
    hour: float
    minute: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day = self.day

        hour = self.hour

        minute = self.minute

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "day": day,
                "hour": hour,
                "minute": minute,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        day = d.pop("day")

        hour = d.pop("hour")

        minute = d.pop("minute")

        accounts_table_request_limits = cls(
            day=day,
            hour=hour,
            minute=minute,
        )

        accounts_table_request_limits.additional_properties = d
        return accounts_table_request_limits

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

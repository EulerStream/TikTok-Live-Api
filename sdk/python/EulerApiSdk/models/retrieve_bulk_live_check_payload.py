from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RetrieveBulkLiveCheckPayload")


@_attrs_define
class RetrieveBulkLiveCheckPayload:
    """
    Attributes:
        user_numeric_ids (list[str]):
    """

    user_numeric_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_numeric_ids = self.user_numeric_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_numeric_ids": user_numeric_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_numeric_ids = cast(list[str], d.pop("user_numeric_ids"))

        retrieve_bulk_live_check_payload = cls(
            user_numeric_ids=user_numeric_ids,
        )

        retrieve_bulk_live_check_payload.additional_properties = d
        return retrieve_bulk_live_check_payload

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

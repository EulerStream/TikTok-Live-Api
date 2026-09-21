from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GiftOverrideGiftSponsorInfo")


@_attrs_define
class GiftOverrideGiftSponsorInfo:
    """
    Attributes:
        current_count (float):
        can_sponsor (bool):
        left_count_to_sponsor (float):
        sponsor_count (float):
        sponsor_id (float):
    """

    current_count: float
    can_sponsor: bool
    left_count_to_sponsor: float
    sponsor_count: float
    sponsor_id: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_count = self.current_count

        can_sponsor = self.can_sponsor

        left_count_to_sponsor = self.left_count_to_sponsor

        sponsor_count = self.sponsor_count

        sponsor_id = self.sponsor_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_count": current_count,
                "can_sponsor": can_sponsor,
                "left_count_to_sponsor": left_count_to_sponsor,
                "sponsor_count": sponsor_count,
                "sponsor_id": sponsor_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_count = d.pop("current_count")

        can_sponsor = d.pop("can_sponsor")

        left_count_to_sponsor = d.pop("left_count_to_sponsor")

        sponsor_count = d.pop("sponsor_count")

        sponsor_id = d.pop("sponsor_id")

        gift_override_gift_sponsor_info = cls(
            current_count=current_count,
            can_sponsor=can_sponsor,
            left_count_to_sponsor=left_count_to_sponsor,
            sponsor_count=sponsor_count,
            sponsor_id=sponsor_id,
        )

        gift_override_gift_sponsor_info.additional_properties = d
        return gift_override_gift_sponsor_info

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

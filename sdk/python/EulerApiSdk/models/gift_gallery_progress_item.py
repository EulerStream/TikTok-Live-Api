from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GiftGalleryProgressItem")


@_attrs_define
class GiftGalleryProgressItem:
    """Per-gift sponsorship progress entry (`data.current_user_progress[giftId]`).

    Attributes:
        sponsor_id (float):
        sponsor_count (float):
        left_count_to_sponsor (float):
        current_count (float):
        can_sponsor (bool):
    """

    sponsor_id: float
    sponsor_count: float
    left_count_to_sponsor: float
    current_count: float
    can_sponsor: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sponsor_id = self.sponsor_id

        sponsor_count = self.sponsor_count

        left_count_to_sponsor = self.left_count_to_sponsor

        current_count = self.current_count

        can_sponsor = self.can_sponsor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sponsor_id": sponsor_id,
                "sponsor_count": sponsor_count,
                "left_count_to_sponsor": left_count_to_sponsor,
                "current_count": current_count,
                "can_sponsor": can_sponsor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sponsor_id = d.pop("sponsor_id")

        sponsor_count = d.pop("sponsor_count")

        left_count_to_sponsor = d.pop("left_count_to_sponsor")

        current_count = d.pop("current_count")

        can_sponsor = d.pop("can_sponsor")

        gift_gallery_progress_item = cls(
            sponsor_id=sponsor_id,
            sponsor_count=sponsor_count,
            left_count_to_sponsor=left_count_to_sponsor,
            current_count=current_count,
            can_sponsor=can_sponsor,
        )

        gift_gallery_progress_item.additional_properties = d
        return gift_gallery_progress_item

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

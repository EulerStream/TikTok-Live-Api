from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gift_override_gift_sponsor_info import GiftOverrideGiftSponsorInfo


T = TypeVar("T", bound="GiftOverride")


@_attrs_define
class GiftOverride:
    """
    Attributes:
        is_displayed_on_panel (bool | Unset):
        is_gallery_gift (bool | Unset):
        gift_sponsor_info (GiftOverrideGiftSponsorInfo | Unset):
    """

    is_displayed_on_panel: bool | Unset = UNSET
    is_gallery_gift: bool | Unset = UNSET
    gift_sponsor_info: GiftOverrideGiftSponsorInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_displayed_on_panel = self.is_displayed_on_panel

        is_gallery_gift = self.is_gallery_gift

        gift_sponsor_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gift_sponsor_info, Unset):
            gift_sponsor_info = self.gift_sponsor_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_displayed_on_panel is not UNSET:
            field_dict["is_displayed_on_panel"] = is_displayed_on_panel
        if is_gallery_gift is not UNSET:
            field_dict["is_gallery_gift"] = is_gallery_gift
        if gift_sponsor_info is not UNSET:
            field_dict["gift_sponsor_info"] = gift_sponsor_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gift_override_gift_sponsor_info import GiftOverrideGiftSponsorInfo

        d = dict(src_dict)
        is_displayed_on_panel = d.pop("is_displayed_on_panel", UNSET)

        is_gallery_gift = d.pop("is_gallery_gift", UNSET)

        _gift_sponsor_info = d.pop("gift_sponsor_info", UNSET)
        gift_sponsor_info: GiftOverrideGiftSponsorInfo | Unset
        if isinstance(_gift_sponsor_info, Unset):
            gift_sponsor_info = UNSET
        else:
            gift_sponsor_info = GiftOverrideGiftSponsorInfo.from_dict(_gift_sponsor_info)

        gift_override = cls(
            is_displayed_on_panel=is_displayed_on_panel,
            is_gallery_gift=is_gallery_gift,
            gift_sponsor_info=gift_sponsor_info,
        )

        gift_override.additional_properties = d
        return gift_override

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

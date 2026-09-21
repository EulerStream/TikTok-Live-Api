from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebcastFeedResponseRoomDataTaxonomyTagInfo")


@_attrs_define
class WebcastFeedResponseRoomDataTaxonomyTagInfo:
    """
    Attributes:
        level2_tag (str):
        level1_tag (list[str] | Unset):
    """

    level2_tag: str
    level1_tag: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        level2_tag = self.level2_tag

        level1_tag: list[str] | Unset = UNSET
        if not isinstance(self.level1_tag, Unset):
            level1_tag = self.level1_tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "level2_tag": level2_tag,
            }
        )
        if level1_tag is not UNSET:
            field_dict["level1_tag"] = level1_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        level2_tag = d.pop("level2_tag")

        level1_tag = cast(list[str], d.pop("level1_tag", UNSET))

        webcast_feed_response_room_data_taxonomy_tag_info = cls(
            level2_tag=level2_tag,
            level1_tag=level1_tag,
        )

        webcast_feed_response_room_data_taxonomy_tag_info.additional_properties = d
        return webcast_feed_response_room_data_taxonomy_tag_info

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

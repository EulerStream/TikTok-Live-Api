from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TikTokGiftsServerGift")


@_attrs_define
class TikTokGiftsServerGift:
    """One gift row from the ClickHouse `tiktok_gifts` ReplacingMergeTree. Mirrors the searchable columns + the JSON `raw`
    blob (shipped as a UTF-8 JSON string here so consumers can decode lazily without re-encoding through protobuf any-
    types).

        Attributes:
            gift_id (float):
            gift_name (str):
            gift_type (float):
            diamond_count (float):
            combo (bool):
            for_link_mic (bool):
            describe (str):
            duration (str):
            image_uri (str):
            updated_at (str):
    """

    gift_id: float
    gift_name: str
    gift_type: float
    diamond_count: float
    combo: bool
    for_link_mic: bool
    describe: str
    duration: str
    image_uri: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gift_id = self.gift_id

        gift_name = self.gift_name

        gift_type = self.gift_type

        diamond_count = self.diamond_count

        combo = self.combo

        for_link_mic = self.for_link_mic

        describe = self.describe

        duration = self.duration

        image_uri = self.image_uri

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "giftId": gift_id,
                "giftName": gift_name,
                "giftType": gift_type,
                "diamondCount": diamond_count,
                "combo": combo,
                "forLinkMic": for_link_mic,
                "describe": describe,
                "duration": duration,
                "imageUri": image_uri,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gift_id = d.pop("giftId")

        gift_name = d.pop("giftName")

        gift_type = d.pop("giftType")

        diamond_count = d.pop("diamondCount")

        combo = d.pop("combo")

        for_link_mic = d.pop("forLinkMic")

        describe = d.pop("describe")

        duration = d.pop("duration")

        image_uri = d.pop("imageUri")

        updated_at = d.pop("updatedAt")

        tik_tok_gifts_server_gift = cls(
            gift_id=gift_id,
            gift_name=gift_name,
            gift_type=gift_type,
            diamond_count=diamond_count,
            combo=combo,
            for_link_mic=for_link_mic,
            describe=describe,
            duration=duration,
            image_uri=image_uri,
            updated_at=updated_at,
        )

        tik_tok_gifts_server_gift.additional_properties = d
        return tik_tok_gifts_server_gift

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

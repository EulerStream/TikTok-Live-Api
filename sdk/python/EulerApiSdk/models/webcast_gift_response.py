from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tik_tok_gifts_server_gift import TikTokGiftsServerGift


T = TypeVar("T", bound="WebcastGiftResponse")


@_attrs_define
class WebcastGiftResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        gift (TikTokGiftsServerGift | Unset): One gift row from the ClickHouse `tiktok_gifts` ReplacingMergeTree.
            Mirrors the searchable columns + the JSON `raw` blob (shipped as a UTF-8 JSON string here so consumers can
            decode lazily without re-encoding through protobuf any-types).
    """

    code: float
    message: str | Unset = UNSET
    gift: TikTokGiftsServerGift | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        gift: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gift, Unset):
            gift = self.gift.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if gift is not UNSET:
            field_dict["gift"] = gift

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tik_tok_gifts_server_gift import TikTokGiftsServerGift  # noqa: PLC0415

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _gift = d.pop("gift", UNSET)
        gift: TikTokGiftsServerGift | Unset
        if isinstance(_gift, Unset):
            gift = UNSET
        else:
            gift = TikTokGiftsServerGift.from_dict(_gift)

        webcast_gift_response = cls(
            code=code,
            message=message,
            gift=gift,
        )

        webcast_gift_response.additional_properties = d
        return webcast_gift_response

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tik_tok_gifts_server_gift import TikTokGiftsServerGift


T = TypeVar("T", bound="WebcastGiftSearchResponse")


@_attrs_define
class WebcastGiftSearchResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        gifts (list[TikTokGiftsServerGift] | Unset):
    """

    code: float
    message: str | Unset = UNSET
    gifts: list[TikTokGiftsServerGift] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        gifts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gifts, Unset):
            gifts = []
            for gifts_item_data in self.gifts:
                gifts_item = gifts_item_data.to_dict()
                gifts.append(gifts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if gifts is not UNSET:
            field_dict["gifts"] = gifts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tik_tok_gifts_server_gift import TikTokGiftsServerGift

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _gifts = d.pop("gifts", UNSET)
        gifts: list[TikTokGiftsServerGift] | Unset = UNSET
        if _gifts is not UNSET:
            gifts = []
            for gifts_item_data in _gifts:
                gifts_item = TikTokGiftsServerGift.from_dict(gifts_item_data)

                gifts.append(gifts_item)

        webcast_gift_search_response = cls(
            code=code,
            message=message,
            gifts=gifts,
        )

        webcast_gift_search_response.additional_properties = d
        return webcast_gift_search_response

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

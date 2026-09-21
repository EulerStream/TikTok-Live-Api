from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tik_tok_gifts_server_gift import TikTokGiftsServerGift


T = TypeVar("T", bound="WebcastGiftcatalogResponse")


@_attrs_define
class WebcastGiftcatalogResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        gifts (list[TikTokGiftsServerGift] | Unset):
        total (float | Unset):
        page_size (float | Unset):
        page_number (float | Unset):
        total_pages (float | Unset):
    """

    code: float
    message: str | Unset = UNSET
    gifts: list[TikTokGiftsServerGift] | Unset = UNSET
    total: float | Unset = UNSET
    page_size: float | Unset = UNSET
    page_number: float | Unset = UNSET
    total_pages: float | Unset = UNSET
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

        total = self.total

        page_size = self.page_size

        page_number = self.page_number

        total_pages = self.total_pages

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
        if total is not UNSET:
            field_dict["total"] = total
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages

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

        total = d.pop("total", UNSET)

        page_size = d.pop("pageSize", UNSET)

        page_number = d.pop("pageNumber", UNSET)

        total_pages = d.pop("totalPages", UNSET)

        webcast_giftcatalog_response = cls(
            code=code,
            message=message,
            gifts=gifts,
            total=total,
            page_size=page_size,
            page_number=page_number,
            total_pages=total_pages,
        )

        webcast_giftcatalog_response.additional_properties = d
        return webcast_giftcatalog_response

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

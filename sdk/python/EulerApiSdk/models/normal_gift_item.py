from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.gift_gallery_sponsor_info import GiftGallerySponsorInfo
    from ..models.normal_gift_item_biz_extra import NormalGiftItemBizExtra


T = TypeVar("T", bound="NormalGiftItem")


@_attrs_define
class NormalGiftItem:
    """An entry of `data.normal_gifts` — a sponsorable gallery gift.

    Attributes:
        unlighted_image_url (str):
        swapped (bool):
        sponsorship_require_count (float):
        sponsored (bool):
        sponsor_rank (list[Any]):
        sponsor_info (GiftGallerySponsorInfo): Current sponsor of a gallery gift (`normal_gifts[].sponsor_info`).
        name (str):
        is_sponsor (bool):
        image_url (str):
        goal_count (float):
        gift_id (str):
        gallery_gift_tag_url (str):
        gallery_gift_tag_type (float):
        current_sent_count (float):
        coin_price (float):
        can_sponsor (bool):
        biz_extra (NormalGiftItemBizExtra):
    """

    unlighted_image_url: str
    swapped: bool
    sponsorship_require_count: float
    sponsored: bool
    sponsor_rank: list[Any]
    sponsor_info: GiftGallerySponsorInfo
    name: str
    is_sponsor: bool
    image_url: str
    goal_count: float
    gift_id: str
    gallery_gift_tag_url: str
    gallery_gift_tag_type: float
    current_sent_count: float
    coin_price: float
    can_sponsor: bool
    biz_extra: NormalGiftItemBizExtra
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unlighted_image_url = self.unlighted_image_url

        swapped = self.swapped

        sponsorship_require_count = self.sponsorship_require_count

        sponsored = self.sponsored

        sponsor_rank = self.sponsor_rank

        sponsor_info = self.sponsor_info.to_dict()

        name = self.name

        is_sponsor = self.is_sponsor

        image_url = self.image_url

        goal_count = self.goal_count

        gift_id = self.gift_id

        gallery_gift_tag_url = self.gallery_gift_tag_url

        gallery_gift_tag_type = self.gallery_gift_tag_type

        current_sent_count = self.current_sent_count

        coin_price = self.coin_price

        can_sponsor = self.can_sponsor

        biz_extra = self.biz_extra.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unlighted_image_url": unlighted_image_url,
                "swapped": swapped,
                "sponsorship_require_count": sponsorship_require_count,
                "sponsored": sponsored,
                "sponsor_rank": sponsor_rank,
                "sponsor_info": sponsor_info,
                "name": name,
                "is_sponsor": is_sponsor,
                "image_url": image_url,
                "goal_count": goal_count,
                "gift_id": gift_id,
                "gallery_gift_tag_url": gallery_gift_tag_url,
                "gallery_gift_tag_type": gallery_gift_tag_type,
                "current_sent_count": current_sent_count,
                "coin_price": coin_price,
                "can_sponsor": can_sponsor,
                "biz_extra": biz_extra,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gift_gallery_sponsor_info import GiftGallerySponsorInfo
        from ..models.normal_gift_item_biz_extra import NormalGiftItemBizExtra

        d = dict(src_dict)
        unlighted_image_url = d.pop("unlighted_image_url")

        swapped = d.pop("swapped")

        sponsorship_require_count = d.pop("sponsorship_require_count")

        sponsored = d.pop("sponsored")

        sponsor_rank = cast(list[Any], d.pop("sponsor_rank"))

        sponsor_info = GiftGallerySponsorInfo.from_dict(d.pop("sponsor_info"))

        name = d.pop("name")

        is_sponsor = d.pop("is_sponsor")

        image_url = d.pop("image_url")

        goal_count = d.pop("goal_count")

        gift_id = d.pop("gift_id")

        gallery_gift_tag_url = d.pop("gallery_gift_tag_url")

        gallery_gift_tag_type = d.pop("gallery_gift_tag_type")

        current_sent_count = d.pop("current_sent_count")

        coin_price = d.pop("coin_price")

        can_sponsor = d.pop("can_sponsor")

        biz_extra = NormalGiftItemBizExtra.from_dict(d.pop("biz_extra"))

        normal_gift_item = cls(
            unlighted_image_url=unlighted_image_url,
            swapped=swapped,
            sponsorship_require_count=sponsorship_require_count,
            sponsored=sponsored,
            sponsor_rank=sponsor_rank,
            sponsor_info=sponsor_info,
            name=name,
            is_sponsor=is_sponsor,
            image_url=image_url,
            goal_count=goal_count,
            gift_id=gift_id,
            gallery_gift_tag_url=gallery_gift_tag_url,
            gallery_gift_tag_type=gallery_gift_tag_type,
            current_sent_count=current_sent_count,
            coin_price=coin_price,
            can_sponsor=can_sponsor,
            biz_extra=biz_extra,
        )

        normal_gift_item.additional_properties = d
        return normal_gift_item

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

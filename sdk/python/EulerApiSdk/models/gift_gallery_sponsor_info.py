from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GiftGallerySponsorInfo")


@_attrs_define
class GiftGallerySponsorInfo:
    """Current sponsor of a gallery gift (`normal_gifts[].sponsor_info`).

    Attributes:
        user_has_optout (bool):
        sponsor_id (str):
        sent_count (float):
        nickname (str):
        last_send_time_sec (float):
        became_sponsor_times (float):
        avatar_image (str):
        anchor_has_followed (bool):
    """

    user_has_optout: bool
    sponsor_id: str
    sent_count: float
    nickname: str
    last_send_time_sec: float
    became_sponsor_times: float
    avatar_image: str
    anchor_has_followed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_has_optout = self.user_has_optout

        sponsor_id = self.sponsor_id

        sent_count = self.sent_count

        nickname = self.nickname

        last_send_time_sec = self.last_send_time_sec

        became_sponsor_times = self.became_sponsor_times

        avatar_image = self.avatar_image

        anchor_has_followed = self.anchor_has_followed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_has_optout": user_has_optout,
                "sponsor_id": sponsor_id,
                "sent_count": sent_count,
                "nickname": nickname,
                "last_send_time_sec": last_send_time_sec,
                "became_sponsor_times": became_sponsor_times,
                "avatar_image": avatar_image,
                "anchor_has_followed": anchor_has_followed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_has_optout = d.pop("user_has_optout")

        sponsor_id = d.pop("sponsor_id")

        sent_count = d.pop("sent_count")

        nickname = d.pop("nickname")

        last_send_time_sec = d.pop("last_send_time_sec")

        became_sponsor_times = d.pop("became_sponsor_times")

        avatar_image = d.pop("avatar_image")

        anchor_has_followed = d.pop("anchor_has_followed")

        gift_gallery_sponsor_info = cls(
            user_has_optout=user_has_optout,
            sponsor_id=sponsor_id,
            sent_count=sent_count,
            nickname=nickname,
            last_send_time_sec=last_send_time_sec,
            became_sponsor_times=became_sponsor_times,
            avatar_image=avatar_image,
            anchor_has_followed=anchor_has_followed,
        )

        gift_gallery_sponsor_info.additional_properties = d
        return gift_gallery_sponsor_info

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

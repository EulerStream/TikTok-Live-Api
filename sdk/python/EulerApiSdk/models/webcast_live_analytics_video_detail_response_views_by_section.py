from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseViewsBySection")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseViewsBySection:
    """
    Attributes:
        following (float):
        live_recomm (float):
        others (float):
        share (float):
        video_recomm (float):
    """

    following: float
    live_recomm: float
    others: float
    share: float
    video_recomm: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        following = self.following

        live_recomm = self.live_recomm

        others = self.others

        share = self.share

        video_recomm = self.video_recomm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "following": following,
                "live_recomm": live_recomm,
                "others": others,
                "share": share,
                "video_recomm": video_recomm,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        following = d.pop("following")

        live_recomm = d.pop("live_recomm")

        others = d.pop("others")

        share = d.pop("share")

        video_recomm = d.pop("video_recomm")

        webcast_live_analytics_video_detail_response_views_by_section = cls(
            following=following,
            live_recomm=live_recomm,
            others=others,
            share=share,
            video_recomm=video_recomm,
        )

        webcast_live_analytics_video_detail_response_views_by_section.additional_properties = d
        return webcast_live_analytics_video_detail_response_views_by_section

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_video_detail_response_video_recomm_info import (
        WebcastLiveAnalyticsVideoDetailResponseVideoRecommInfo,
    )


T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseTrafficTotal")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseTrafficTotal:
    """
    Attributes:
        following (float):
        live_recomm (float):
        others (float):
        share (float):
        video_recomm (float):
        video_recomm_info (WebcastLiveAnalyticsVideoDetailResponseVideoRecommInfo):
    """

    following: float
    live_recomm: float
    others: float
    share: float
    video_recomm: float
    video_recomm_info: WebcastLiveAnalyticsVideoDetailResponseVideoRecommInfo
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        following = self.following

        live_recomm = self.live_recomm

        others = self.others

        share = self.share

        video_recomm = self.video_recomm

        video_recomm_info = self.video_recomm_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "following": following,
                "live_recomm": live_recomm,
                "others": others,
                "share": share,
                "video_recomm": video_recomm,
                "video_recomm_info": video_recomm_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_live_analytics_video_detail_response_video_recomm_info import (
            WebcastLiveAnalyticsVideoDetailResponseVideoRecommInfo,  # noqa: PLC0415
        )

        d = dict(src_dict)
        following = d.pop("following")

        live_recomm = d.pop("live_recomm")

        others = d.pop("others")

        share = d.pop("share")

        video_recomm = d.pop("video_recomm")

        video_recomm_info = WebcastLiveAnalyticsVideoDetailResponseVideoRecommInfo.from_dict(d.pop("video_recomm_info"))

        webcast_live_analytics_video_detail_response_traffic_total = cls(
            following=following,
            live_recomm=live_recomm,
            others=others,
            share=share,
            video_recomm=video_recomm,
            video_recomm_info=video_recomm_info,
        )

        webcast_live_analytics_video_detail_response_traffic_total.additional_properties = d
        return webcast_live_analytics_video_detail_response_traffic_total

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

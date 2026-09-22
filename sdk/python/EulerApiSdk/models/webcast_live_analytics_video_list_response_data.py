from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_video_list_response_video import WebcastLiveAnalyticsVideoListResponseVideo


T = TypeVar("T", bound="WebcastLiveAnalyticsVideoListResponseData")


@_attrs_define
class WebcastLiveAnalyticsVideoListResponseData:
    """
    Attributes:
        total (float):
        video_list (list[WebcastLiveAnalyticsVideoListResponseVideo]):
    """

    total: float
    video_list: list[WebcastLiveAnalyticsVideoListResponseVideo]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        video_list = []
        for video_list_item_data in self.video_list:
            video_list_item = video_list_item_data.to_dict()
            video_list.append(video_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "video_list": video_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_live_analytics_video_list_response_video import (
            WebcastLiveAnalyticsVideoListResponseVideo,  # noqa: PLC0415
        )

        d = dict(src_dict)
        total = d.pop("total")

        video_list = []
        _video_list = d.pop("video_list")
        for video_list_item_data in _video_list:
            video_list_item = WebcastLiveAnalyticsVideoListResponseVideo.from_dict(video_list_item_data)

            video_list.append(video_list_item)

        webcast_live_analytics_video_list_response_data = cls(
            total=total,
            video_list=video_list,
        )

        webcast_live_analytics_video_list_response_data.additional_properties = d
        return webcast_live_analytics_video_list_response_data

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

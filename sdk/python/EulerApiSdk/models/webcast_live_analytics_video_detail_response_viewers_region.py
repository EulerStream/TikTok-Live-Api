from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_video_detail_response_region_entry import (
        WebcastLiveAnalyticsVideoDetailResponseRegionEntry,
    )


T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseViewersRegion")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseViewersRegion:
    """
    Attributes:
        others (float):
        top_viewers_region_list (list[WebcastLiveAnalyticsVideoDetailResponseRegionEntry]):
    """

    others: float
    top_viewers_region_list: list[WebcastLiveAnalyticsVideoDetailResponseRegionEntry]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        others = self.others

        top_viewers_region_list = []
        for top_viewers_region_list_item_data in self.top_viewers_region_list:
            top_viewers_region_list_item = top_viewers_region_list_item_data.to_dict()
            top_viewers_region_list.append(top_viewers_region_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "others": others,
                "top_viewers_region_list": top_viewers_region_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_live_analytics_video_detail_response_region_entry import (
            WebcastLiveAnalyticsVideoDetailResponseRegionEntry,
        )

        d = dict(src_dict)
        others = d.pop("others")

        top_viewers_region_list = []
        _top_viewers_region_list = d.pop("top_viewers_region_list")
        for top_viewers_region_list_item_data in _top_viewers_region_list:
            top_viewers_region_list_item = WebcastLiveAnalyticsVideoDetailResponseRegionEntry.from_dict(
                top_viewers_region_list_item_data
            )

            top_viewers_region_list.append(top_viewers_region_list_item)

        webcast_live_analytics_video_detail_response_viewers_region = cls(
            others=others,
            top_viewers_region_list=top_viewers_region_list,
        )

        webcast_live_analytics_video_detail_response_viewers_region.additional_properties = d
        return webcast_live_analytics_video_detail_response_viewers_region

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

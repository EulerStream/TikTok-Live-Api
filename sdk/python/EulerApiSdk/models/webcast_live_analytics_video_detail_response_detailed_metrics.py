from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_video_detail_response_follower_metric import (
        WebcastLiveAnalyticsVideoDetailResponseFollowerMetric,
    )


T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseDetailedMetrics")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseDetailedMetrics:
    """
    Attributes:
        commenter (WebcastLiveAnalyticsVideoDetailResponseFollowerMetric):
        gifters (WebcastLiveAnalyticsVideoDetailResponseFollowerMetric):
        viewers (WebcastLiveAnalyticsVideoDetailResponseFollowerMetric):
    """

    commenter: WebcastLiveAnalyticsVideoDetailResponseFollowerMetric
    gifters: WebcastLiveAnalyticsVideoDetailResponseFollowerMetric
    viewers: WebcastLiveAnalyticsVideoDetailResponseFollowerMetric
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commenter = self.commenter.to_dict()

        gifters = self.gifters.to_dict()

        viewers = self.viewers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commenter": commenter,
                "gifters": gifters,
                "viewers": viewers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_live_analytics_video_detail_response_follower_metric import (
            WebcastLiveAnalyticsVideoDetailResponseFollowerMetric,
        )

        d = dict(src_dict)
        commenter = WebcastLiveAnalyticsVideoDetailResponseFollowerMetric.from_dict(d.pop("commenter"))

        gifters = WebcastLiveAnalyticsVideoDetailResponseFollowerMetric.from_dict(d.pop("gifters"))

        viewers = WebcastLiveAnalyticsVideoDetailResponseFollowerMetric.from_dict(d.pop("viewers"))

        webcast_live_analytics_video_detail_response_detailed_metrics = cls(
            commenter=commenter,
            gifters=gifters,
            viewers=viewers,
        )

        webcast_live_analytics_video_detail_response_detailed_metrics.additional_properties = d
        return webcast_live_analytics_video_detail_response_detailed_metrics

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

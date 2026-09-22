from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_video_detail_response_analytics import (
        WebcastLiveAnalyticsVideoDetailResponseAnalytics,
    )
    from ..models.webcast_live_analytics_video_detail_response_average_watch_time import (
        WebcastLiveAnalyticsVideoDetailResponseAverageWatchTime,
    )
    from ..models.webcast_live_analytics_video_detail_response_behavior_summary import (
        WebcastLiveAnalyticsVideoDetailResponseBehaviorSummary,
    )
    from ..models.webcast_live_analytics_video_detail_response_comments_info import (
        WebcastLiveAnalyticsVideoDetailResponseCommentsInfo,
    )
    from ..models.webcast_live_analytics_video_detail_response_detailed_metrics import (
        WebcastLiveAnalyticsVideoDetailResponseDetailedMetrics,
    )
    from ..models.webcast_live_analytics_video_detail_response_new_analytics import (
        WebcastLiveAnalyticsVideoDetailResponseNewAnalytics,
    )
    from ..models.webcast_live_analytics_video_detail_response_traffic_info import (
        WebcastLiveAnalyticsVideoDetailResponseTrafficInfo,
    )
    from ..models.webcast_live_analytics_video_detail_response_viewer_info import (
        WebcastLiveAnalyticsVideoDetailResponseViewerInfo,
    )
    from ..models.webcast_live_analytics_video_detail_response_views_by_section import (
        WebcastLiveAnalyticsVideoDetailResponseViewsBySection,
    )


T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseData")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseData:
    """
    Attributes:
        analytics (WebcastLiveAnalyticsVideoDetailResponseAnalytics):
        average_watch_time (WebcastLiveAnalyticsVideoDetailResponseAverageWatchTime):
        behavior_summary (WebcastLiveAnalyticsVideoDetailResponseBehaviorSummary):
        comments_info (WebcastLiveAnalyticsVideoDetailResponseCommentsInfo):
        cover_image_url (str):
        detailed_metrics (WebcastLiveAnalyticsVideoDetailResponseDetailedMetrics):
        duration (float):
        end_time (float):
        is_first_live (bool):
        new_analytics (WebcastLiveAnalyticsVideoDetailResponseNewAnalytics):
        pause_duration (float):
        start_time (float):
        title (str):
        traffic_info (WebcastLiveAnalyticsVideoDetailResponseTrafficInfo):
        viewer_info (WebcastLiveAnalyticsVideoDetailResponseViewerInfo):
        views_by_setion (WebcastLiveAnalyticsVideoDetailResponseViewsBySection):
    """

    analytics: WebcastLiveAnalyticsVideoDetailResponseAnalytics
    average_watch_time: WebcastLiveAnalyticsVideoDetailResponseAverageWatchTime
    behavior_summary: WebcastLiveAnalyticsVideoDetailResponseBehaviorSummary
    comments_info: WebcastLiveAnalyticsVideoDetailResponseCommentsInfo
    cover_image_url: str
    detailed_metrics: WebcastLiveAnalyticsVideoDetailResponseDetailedMetrics
    duration: float
    end_time: float
    is_first_live: bool
    new_analytics: WebcastLiveAnalyticsVideoDetailResponseNewAnalytics
    pause_duration: float
    start_time: float
    title: str
    traffic_info: WebcastLiveAnalyticsVideoDetailResponseTrafficInfo
    viewer_info: WebcastLiveAnalyticsVideoDetailResponseViewerInfo
    views_by_setion: WebcastLiveAnalyticsVideoDetailResponseViewsBySection
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        analytics = self.analytics.to_dict()

        average_watch_time = self.average_watch_time.to_dict()

        behavior_summary = self.behavior_summary.to_dict()

        comments_info = self.comments_info.to_dict()

        cover_image_url = self.cover_image_url

        detailed_metrics = self.detailed_metrics.to_dict()

        duration = self.duration

        end_time = self.end_time

        is_first_live = self.is_first_live

        new_analytics = self.new_analytics.to_dict()

        pause_duration = self.pause_duration

        start_time = self.start_time

        title = self.title

        traffic_info = self.traffic_info.to_dict()

        viewer_info = self.viewer_info.to_dict()

        views_by_setion = self.views_by_setion.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "analytics": analytics,
                "average_watch_time": average_watch_time,
                "behavior_summary": behavior_summary,
                "comments_info": comments_info,
                "cover_image_url": cover_image_url,
                "detailed_metrics": detailed_metrics,
                "duration": duration,
                "end_time": end_time,
                "is_first_live": is_first_live,
                "new_analytics": new_analytics,
                "pause_duration": pause_duration,
                "start_time": start_time,
                "title": title,
                "traffic_info": traffic_info,
                "viewer_info": viewer_info,
                "views_by_setion": views_by_setion,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_live_analytics_video_detail_response_analytics import (
            WebcastLiveAnalyticsVideoDetailResponseAnalytics,  # noqa: PLC0415
        )
        from ..models.webcast_live_analytics_video_detail_response_average_watch_time import (
            WebcastLiveAnalyticsVideoDetailResponseAverageWatchTime,  # noqa: PLC0415
        )
        from ..models.webcast_live_analytics_video_detail_response_behavior_summary import (
            WebcastLiveAnalyticsVideoDetailResponseBehaviorSummary,  # noqa: PLC0415
        )
        from ..models.webcast_live_analytics_video_detail_response_comments_info import (
            WebcastLiveAnalyticsVideoDetailResponseCommentsInfo,  # noqa: PLC0415
        )
        from ..models.webcast_live_analytics_video_detail_response_detailed_metrics import (
            WebcastLiveAnalyticsVideoDetailResponseDetailedMetrics,  # noqa: PLC0415
        )
        from ..models.webcast_live_analytics_video_detail_response_new_analytics import (
            WebcastLiveAnalyticsVideoDetailResponseNewAnalytics,  # noqa: PLC0415
        )
        from ..models.webcast_live_analytics_video_detail_response_traffic_info import (
            WebcastLiveAnalyticsVideoDetailResponseTrafficInfo,  # noqa: PLC0415
        )
        from ..models.webcast_live_analytics_video_detail_response_viewer_info import (
            WebcastLiveAnalyticsVideoDetailResponseViewerInfo,  # noqa: PLC0415
        )
        from ..models.webcast_live_analytics_video_detail_response_views_by_section import (
            WebcastLiveAnalyticsVideoDetailResponseViewsBySection,  # noqa: PLC0415
        )

        d = dict(src_dict)
        analytics = WebcastLiveAnalyticsVideoDetailResponseAnalytics.from_dict(d.pop("analytics"))

        average_watch_time = WebcastLiveAnalyticsVideoDetailResponseAverageWatchTime.from_dict(
            d.pop("average_watch_time")
        )

        behavior_summary = WebcastLiveAnalyticsVideoDetailResponseBehaviorSummary.from_dict(d.pop("behavior_summary"))

        comments_info = WebcastLiveAnalyticsVideoDetailResponseCommentsInfo.from_dict(d.pop("comments_info"))

        cover_image_url = d.pop("cover_image_url")

        detailed_metrics = WebcastLiveAnalyticsVideoDetailResponseDetailedMetrics.from_dict(d.pop("detailed_metrics"))

        duration = d.pop("duration")

        end_time = d.pop("end_time")

        is_first_live = d.pop("is_first_live")

        new_analytics = WebcastLiveAnalyticsVideoDetailResponseNewAnalytics.from_dict(d.pop("new_analytics"))

        pause_duration = d.pop("pause_duration")

        start_time = d.pop("start_time")

        title = d.pop("title")

        traffic_info = WebcastLiveAnalyticsVideoDetailResponseTrafficInfo.from_dict(d.pop("traffic_info"))

        viewer_info = WebcastLiveAnalyticsVideoDetailResponseViewerInfo.from_dict(d.pop("viewer_info"))

        views_by_setion = WebcastLiveAnalyticsVideoDetailResponseViewsBySection.from_dict(d.pop("views_by_setion"))

        webcast_live_analytics_video_detail_response_data = cls(
            analytics=analytics,
            average_watch_time=average_watch_time,
            behavior_summary=behavior_summary,
            comments_info=comments_info,
            cover_image_url=cover_image_url,
            detailed_metrics=detailed_metrics,
            duration=duration,
            end_time=end_time,
            is_first_live=is_first_live,
            new_analytics=new_analytics,
            pause_duration=pause_duration,
            start_time=start_time,
            title=title,
            traffic_info=traffic_info,
            viewer_info=viewer_info,
            views_by_setion=views_by_setion,
        )

        webcast_live_analytics_video_detail_response_data.additional_properties = d
        return webcast_live_analytics_video_detail_response_data

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_video_detail_response_earnings import (
        WebcastLiveAnalyticsVideoDetailResponseEarnings,
    )
    from ..models.webcast_live_analytics_video_detail_response_interaction import (
        WebcastLiveAnalyticsVideoDetailResponseInteraction,
    )
    from ..models.webcast_live_analytics_video_detail_response_views import WebcastLiveAnalyticsVideoDetailResponseViews


T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseAnalytics")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseAnalytics:
    """
    Attributes:
        earnings (WebcastLiveAnalyticsVideoDetailResponseEarnings):
        interaction (WebcastLiveAnalyticsVideoDetailResponseInteraction):
        views (WebcastLiveAnalyticsVideoDetailResponseViews):
    """

    earnings: WebcastLiveAnalyticsVideoDetailResponseEarnings
    interaction: WebcastLiveAnalyticsVideoDetailResponseInteraction
    views: WebcastLiveAnalyticsVideoDetailResponseViews
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        earnings = self.earnings.to_dict()

        interaction = self.interaction.to_dict()

        views = self.views.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "earnings": earnings,
                "interaction": interaction,
                "views": views,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_live_analytics_video_detail_response_earnings import (
            WebcastLiveAnalyticsVideoDetailResponseEarnings,  # noqa: PLC0415
        )
        from ..models.webcast_live_analytics_video_detail_response_interaction import (
            WebcastLiveAnalyticsVideoDetailResponseInteraction,  # noqa: PLC0415
        )
        from ..models.webcast_live_analytics_video_detail_response_views import (
            WebcastLiveAnalyticsVideoDetailResponseViews,  # noqa: PLC0415
        )

        d = dict(src_dict)
        earnings = WebcastLiveAnalyticsVideoDetailResponseEarnings.from_dict(d.pop("earnings"))

        interaction = WebcastLiveAnalyticsVideoDetailResponseInteraction.from_dict(d.pop("interaction"))

        views = WebcastLiveAnalyticsVideoDetailResponseViews.from_dict(d.pop("views"))

        webcast_live_analytics_video_detail_response_analytics = cls(
            earnings=earnings,
            interaction=interaction,
            views=views,
        )

        webcast_live_analytics_video_detail_response_analytics.additional_properties = d
        return webcast_live_analytics_video_detail_response_analytics

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

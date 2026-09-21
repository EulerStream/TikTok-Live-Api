from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_video_detail_response_new_earnings import (
        WebcastLiveAnalyticsVideoDetailResponseNewEarnings,
    )
    from ..models.webcast_live_analytics_video_detail_response_new_interaction import (
        WebcastLiveAnalyticsVideoDetailResponseNewInteraction,
    )
    from ..models.webcast_live_analytics_video_detail_response_new_views import (
        WebcastLiveAnalyticsVideoDetailResponseNewViews,
    )


T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseNewAnalytics")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseNewAnalytics:
    """
    Attributes:
        earnings (WebcastLiveAnalyticsVideoDetailResponseNewEarnings):
        interaction (WebcastLiveAnalyticsVideoDetailResponseNewInteraction):
        views (WebcastLiveAnalyticsVideoDetailResponseNewViews):
    """

    earnings: WebcastLiveAnalyticsVideoDetailResponseNewEarnings
    interaction: WebcastLiveAnalyticsVideoDetailResponseNewInteraction
    views: WebcastLiveAnalyticsVideoDetailResponseNewViews
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
        from ..models.webcast_live_analytics_video_detail_response_new_earnings import (
            WebcastLiveAnalyticsVideoDetailResponseNewEarnings,
        )
        from ..models.webcast_live_analytics_video_detail_response_new_interaction import (
            WebcastLiveAnalyticsVideoDetailResponseNewInteraction,
        )
        from ..models.webcast_live_analytics_video_detail_response_new_views import (
            WebcastLiveAnalyticsVideoDetailResponseNewViews,
        )

        d = dict(src_dict)
        earnings = WebcastLiveAnalyticsVideoDetailResponseNewEarnings.from_dict(d.pop("earnings"))

        interaction = WebcastLiveAnalyticsVideoDetailResponseNewInteraction.from_dict(d.pop("interaction"))

        views = WebcastLiveAnalyticsVideoDetailResponseNewViews.from_dict(d.pop("views"))

        webcast_live_analytics_video_detail_response_new_analytics = cls(
            earnings=earnings,
            interaction=interaction,
            views=views,
        )

        webcast_live_analytics_video_detail_response_new_analytics.additional_properties = d
        return webcast_live_analytics_video_detail_response_new_analytics

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_video_detail_response_viewer_portrait import (
        WebcastLiveAnalyticsVideoDetailResponseViewerPortrait,
    )
    from ..models.webcast_live_analytics_video_detail_response_watcher_rank import (
        WebcastLiveAnalyticsVideoDetailResponseWatcherRank,
    )


T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseViewerInfo")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseViewerInfo:
    """
    Attributes:
        gift_rank (list[Any]):
        viewer_portrait (WebcastLiveAnalyticsVideoDetailResponseViewerPortrait):
        watcher_rank (list[WebcastLiveAnalyticsVideoDetailResponseWatcherRank]):
    """

    gift_rank: list[Any]
    viewer_portrait: WebcastLiveAnalyticsVideoDetailResponseViewerPortrait
    watcher_rank: list[WebcastLiveAnalyticsVideoDetailResponseWatcherRank]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gift_rank = self.gift_rank

        viewer_portrait = self.viewer_portrait.to_dict()

        watcher_rank = []
        for watcher_rank_item_data in self.watcher_rank:
            watcher_rank_item = watcher_rank_item_data.to_dict()
            watcher_rank.append(watcher_rank_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gift_rank": gift_rank,
                "viewer_portrait": viewer_portrait,
                "watcher_rank": watcher_rank,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_live_analytics_video_detail_response_viewer_portrait import (
            WebcastLiveAnalyticsVideoDetailResponseViewerPortrait,  # noqa: PLC0415
        )
        from ..models.webcast_live_analytics_video_detail_response_watcher_rank import (
            WebcastLiveAnalyticsVideoDetailResponseWatcherRank,  # noqa: PLC0415
        )

        d = dict(src_dict)
        gift_rank = cast(list[Any], d.pop("gift_rank"))

        viewer_portrait = WebcastLiveAnalyticsVideoDetailResponseViewerPortrait.from_dict(d.pop("viewer_portrait"))

        watcher_rank = []
        _watcher_rank = d.pop("watcher_rank")
        for watcher_rank_item_data in _watcher_rank:
            watcher_rank_item = WebcastLiveAnalyticsVideoDetailResponseWatcherRank.from_dict(watcher_rank_item_data)

            watcher_rank.append(watcher_rank_item)

        webcast_live_analytics_video_detail_response_viewer_info = cls(
            gift_rank=gift_rank,
            viewer_portrait=viewer_portrait,
            watcher_rank=watcher_rank,
        )

        webcast_live_analytics_video_detail_response_viewer_info.additional_properties = d
        return webcast_live_analytics_video_detail_response_viewer_info

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

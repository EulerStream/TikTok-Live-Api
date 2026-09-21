from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_user_interactions_response_comment import (
        WebcastLiveAnalyticsUserInteractionsResponseComment,
    )
    from ..models.webcast_live_analytics_user_interactions_response_user import (
        WebcastLiveAnalyticsUserInteractionsResponseUser,
    )


T = TypeVar("T", bound="WebcastLiveAnalyticsUserInteractionsResponseData")


@_attrs_define
class WebcastLiveAnalyticsUserInteractionsResponseData:
    """
    Attributes:
        anchor (WebcastLiveAnalyticsUserInteractionsResponseUser):
        comment_count (float):
        comment_list (list[WebcastLiveAnalyticsUserInteractionsResponseComment]):
        follow_time (float):
        like_count (float):
        share_count (float):
        summary (str):
        summary_type (float):
        user (WebcastLiveAnalyticsUserInteractionsResponseUser):
        watch_duration (float):
    """

    anchor: WebcastLiveAnalyticsUserInteractionsResponseUser
    comment_count: float
    comment_list: list[WebcastLiveAnalyticsUserInteractionsResponseComment]
    follow_time: float
    like_count: float
    share_count: float
    summary: str
    summary_type: float
    user: WebcastLiveAnalyticsUserInteractionsResponseUser
    watch_duration: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anchor = self.anchor.to_dict()

        comment_count = self.comment_count

        comment_list = []
        for comment_list_item_data in self.comment_list:
            comment_list_item = comment_list_item_data.to_dict()
            comment_list.append(comment_list_item)

        follow_time = self.follow_time

        like_count = self.like_count

        share_count = self.share_count

        summary = self.summary

        summary_type = self.summary_type

        user = self.user.to_dict()

        watch_duration = self.watch_duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "anchor": anchor,
                "comment_count": comment_count,
                "comment_list": comment_list,
                "follow_time": follow_time,
                "like_count": like_count,
                "share_count": share_count,
                "summary": summary,
                "summary_type": summary_type,
                "user": user,
                "watch_duration": watch_duration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_live_analytics_user_interactions_response_comment import (
            WebcastLiveAnalyticsUserInteractionsResponseComment,
        )
        from ..models.webcast_live_analytics_user_interactions_response_user import (
            WebcastLiveAnalyticsUserInteractionsResponseUser,
        )

        d = dict(src_dict)
        anchor = WebcastLiveAnalyticsUserInteractionsResponseUser.from_dict(d.pop("anchor"))

        comment_count = d.pop("comment_count")

        comment_list = []
        _comment_list = d.pop("comment_list")
        for comment_list_item_data in _comment_list:
            comment_list_item = WebcastLiveAnalyticsUserInteractionsResponseComment.from_dict(comment_list_item_data)

            comment_list.append(comment_list_item)

        follow_time = d.pop("follow_time")

        like_count = d.pop("like_count")

        share_count = d.pop("share_count")

        summary = d.pop("summary")

        summary_type = d.pop("summary_type")

        user = WebcastLiveAnalyticsUserInteractionsResponseUser.from_dict(d.pop("user"))

        watch_duration = d.pop("watch_duration")

        webcast_live_analytics_user_interactions_response_data = cls(
            anchor=anchor,
            comment_count=comment_count,
            comment_list=comment_list,
            follow_time=follow_time,
            like_count=like_count,
            share_count=share_count,
            summary=summary,
            summary_type=summary_type,
            user=user,
            watch_duration=watch_duration,
        )

        webcast_live_analytics_user_interactions_response_data.additional_properties = d
        return webcast_live_analytics_user_interactions_response_data

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

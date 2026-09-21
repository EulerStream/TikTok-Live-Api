from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseCommentsInfo")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseCommentsInfo:
    """
    Attributes:
        comment_cnt (float):
        entry_location (str):
        show_entry (bool):
        sub_title (str):
        top_users (list[Any]):
    """

    comment_cnt: float
    entry_location: str
    show_entry: bool
    sub_title: str
    top_users: list[Any]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_cnt = self.comment_cnt

        entry_location = self.entry_location

        show_entry = self.show_entry

        sub_title = self.sub_title

        top_users = self.top_users

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment_cnt": comment_cnt,
                "entry_location": entry_location,
                "show_entry": show_entry,
                "sub_title": sub_title,
                "top_users": top_users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment_cnt = d.pop("comment_cnt")

        entry_location = d.pop("entry_location")

        show_entry = d.pop("show_entry")

        sub_title = d.pop("sub_title")

        top_users = cast(list[Any], d.pop("top_users"))

        webcast_live_analytics_video_detail_response_comments_info = cls(
            comment_cnt=comment_cnt,
            entry_location=entry_location,
            show_entry=show_entry,
            sub_title=sub_title,
            top_users=top_users,
        )

        webcast_live_analytics_video_detail_response_comments_info.additional_properties = d
        return webcast_live_analytics_video_detail_response_comments_info

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseInteraction")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseInteraction:
    """
    Attributes:
        comment (float):
        likes (float):
        new_followers (float):
        shares (float):
    """

    comment: float
    likes: float
    new_followers: float
    shares: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        likes = self.likes

        new_followers = self.new_followers

        shares = self.shares

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment": comment,
                "likes": likes,
                "new_followers": new_followers,
                "shares": shares,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment = d.pop("comment")

        likes = d.pop("likes")

        new_followers = d.pop("new_followers")

        shares = d.pop("shares")

        webcast_live_analytics_video_detail_response_interaction = cls(
            comment=comment,
            likes=likes,
            new_followers=new_followers,
            shares=shares,
        )

        webcast_live_analytics_video_detail_response_interaction.additional_properties = d
        return webcast_live_analytics_video_detail_response_interaction

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

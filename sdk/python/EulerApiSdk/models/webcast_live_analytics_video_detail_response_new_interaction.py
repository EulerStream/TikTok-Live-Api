from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseNewInteraction")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseNewInteraction:
    """
    Attributes:
        comment (float):
        gifters (float):
        last_comment (float):
        last_gifters (float):
        last_likes (float):
        last_new_followers (float):
        last_shares (float):
        likes (float):
        new_followers (float):
        shares (float):
        top_interaction (float):
    """

    comment: float
    gifters: float
    last_comment: float
    last_gifters: float
    last_likes: float
    last_new_followers: float
    last_shares: float
    likes: float
    new_followers: float
    shares: float
    top_interaction: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        gifters = self.gifters

        last_comment = self.last_comment

        last_gifters = self.last_gifters

        last_likes = self.last_likes

        last_new_followers = self.last_new_followers

        last_shares = self.last_shares

        likes = self.likes

        new_followers = self.new_followers

        shares = self.shares

        top_interaction = self.top_interaction

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment": comment,
                "gifters": gifters,
                "last_comment": last_comment,
                "last_gifters": last_gifters,
                "last_likes": last_likes,
                "last_new_followers": last_new_followers,
                "last_shares": last_shares,
                "likes": likes,
                "new_followers": new_followers,
                "shares": shares,
                "top_interaction": top_interaction,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment = d.pop("comment")

        gifters = d.pop("gifters")

        last_comment = d.pop("last_comment")

        last_gifters = d.pop("last_gifters")

        last_likes = d.pop("last_likes")

        last_new_followers = d.pop("last_new_followers")

        last_shares = d.pop("last_shares")

        likes = d.pop("likes")

        new_followers = d.pop("new_followers")

        shares = d.pop("shares")

        top_interaction = d.pop("top_interaction")

        webcast_live_analytics_video_detail_response_new_interaction = cls(
            comment=comment,
            gifters=gifters,
            last_comment=last_comment,
            last_gifters=last_gifters,
            last_likes=last_likes,
            last_new_followers=last_new_followers,
            last_shares=last_shares,
            likes=likes,
            new_followers=new_followers,
            shares=shares,
            top_interaction=top_interaction,
        )

        webcast_live_analytics_video_detail_response_new_interaction.additional_properties = d
        return webcast_live_analytics_video_detail_response_new_interaction

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

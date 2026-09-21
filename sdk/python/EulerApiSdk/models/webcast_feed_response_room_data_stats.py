from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webcast_feed_response_room_data_stats_user_count_composition import (
        WebcastFeedResponseRoomDataStatsUserCountComposition,
    )


T = TypeVar("T", bound="WebcastFeedResponseRoomDataStats")


@_attrs_define
class WebcastFeedResponseRoomDataStats:
    """
    Attributes:
        comment_count (float):
        enter_count (float):
        total_user (float):
        share_count (float | Unset):
        user_count_composition (WebcastFeedResponseRoomDataStatsUserCountComposition | Unset):
    """

    comment_count: float
    enter_count: float
    total_user: float
    share_count: float | Unset = UNSET
    user_count_composition: WebcastFeedResponseRoomDataStatsUserCountComposition | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_count = self.comment_count

        enter_count = self.enter_count

        total_user = self.total_user

        share_count = self.share_count

        user_count_composition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_count_composition, Unset):
            user_count_composition = self.user_count_composition.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment_count": comment_count,
                "enter_count": enter_count,
                "total_user": total_user,
            }
        )
        if share_count is not UNSET:
            field_dict["share_count"] = share_count
        if user_count_composition is not UNSET:
            field_dict["user_count_composition"] = user_count_composition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_feed_response_room_data_stats_user_count_composition import (
            WebcastFeedResponseRoomDataStatsUserCountComposition,
        )

        d = dict(src_dict)
        comment_count = d.pop("comment_count")

        enter_count = d.pop("enter_count")

        total_user = d.pop("total_user")

        share_count = d.pop("share_count", UNSET)

        _user_count_composition = d.pop("user_count_composition", UNSET)
        user_count_composition: WebcastFeedResponseRoomDataStatsUserCountComposition | Unset
        if isinstance(_user_count_composition, Unset):
            user_count_composition = UNSET
        else:
            user_count_composition = WebcastFeedResponseRoomDataStatsUserCountComposition.from_dict(
                _user_count_composition
            )

        webcast_feed_response_room_data_stats = cls(
            comment_count=comment_count,
            enter_count=enter_count,
            total_user=total_user,
            share_count=share_count,
            user_count_composition=user_count_composition,
        )

        webcast_feed_response_room_data_stats.additional_properties = d
        return webcast_feed_response_room_data_stats

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

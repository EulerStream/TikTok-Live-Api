from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseMultiGuestSummary")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseMultiGuestSummary:
    """
    Attributes:
        multi_guest_rank (list[Any]):
        multi_guest_show_type (float):
        total_diamonds (float):
        total_duration (float):
        total_guest (float):
        total_points (float):
    """

    multi_guest_rank: list[Any]
    multi_guest_show_type: float
    total_diamonds: float
    total_duration: float
    total_guest: float
    total_points: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        multi_guest_rank = self.multi_guest_rank

        multi_guest_show_type = self.multi_guest_show_type

        total_diamonds = self.total_diamonds

        total_duration = self.total_duration

        total_guest = self.total_guest

        total_points = self.total_points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "multi_guest_rank": multi_guest_rank,
                "multi_guest_show_type": multi_guest_show_type,
                "total_diamonds": total_diamonds,
                "total_duration": total_duration,
                "total_guest": total_guest,
                "total_points": total_points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        multi_guest_rank = cast(list[Any], d.pop("multi_guest_rank"))

        multi_guest_show_type = d.pop("multi_guest_show_type")

        total_diamonds = d.pop("total_diamonds")

        total_duration = d.pop("total_duration")

        total_guest = d.pop("total_guest")

        total_points = d.pop("total_points")

        webcast_live_analytics_video_detail_response_multi_guest_summary = cls(
            multi_guest_rank=multi_guest_rank,
            multi_guest_show_type=multi_guest_show_type,
            total_diamonds=total_diamonds,
            total_duration=total_duration,
            total_guest=total_guest,
            total_points=total_points,
        )

        webcast_live_analytics_video_detail_response_multi_guest_summary.additional_properties = d
        return webcast_live_analytics_video_detail_response_multi_guest_summary

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

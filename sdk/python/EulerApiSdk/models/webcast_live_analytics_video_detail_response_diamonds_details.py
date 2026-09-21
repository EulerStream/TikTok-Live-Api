from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseDiamondsDetails")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseDiamondsDetails:
    """
    Attributes:
        gift_fan_tickets_percentage (float):
        multi_guest_fan_tickets_percentage (float):
        star_comment_fan_tickets_percentage (float):
        star_comment_qualification (bool):
    """

    gift_fan_tickets_percentage: float
    multi_guest_fan_tickets_percentage: float
    star_comment_fan_tickets_percentage: float
    star_comment_qualification: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gift_fan_tickets_percentage = self.gift_fan_tickets_percentage

        multi_guest_fan_tickets_percentage = self.multi_guest_fan_tickets_percentage

        star_comment_fan_tickets_percentage = self.star_comment_fan_tickets_percentage

        star_comment_qualification = self.star_comment_qualification

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gift_fan_tickets_percentage": gift_fan_tickets_percentage,
                "multi_guest_fan_tickets_percentage": multi_guest_fan_tickets_percentage,
                "star_comment_fan_tickets_percentage": star_comment_fan_tickets_percentage,
                "star_comment_qualification": star_comment_qualification,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gift_fan_tickets_percentage = d.pop("gift_fan_tickets_percentage")

        multi_guest_fan_tickets_percentage = d.pop("multi_guest_fan_tickets_percentage")

        star_comment_fan_tickets_percentage = d.pop("star_comment_fan_tickets_percentage")

        star_comment_qualification = d.pop("star_comment_qualification")

        webcast_live_analytics_video_detail_response_diamonds_details = cls(
            gift_fan_tickets_percentage=gift_fan_tickets_percentage,
            multi_guest_fan_tickets_percentage=multi_guest_fan_tickets_percentage,
            star_comment_fan_tickets_percentage=star_comment_fan_tickets_percentage,
            star_comment_qualification=star_comment_qualification,
        )

        webcast_live_analytics_video_detail_response_diamonds_details.additional_properties = d
        return webcast_live_analytics_video_detail_response_diamonds_details

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

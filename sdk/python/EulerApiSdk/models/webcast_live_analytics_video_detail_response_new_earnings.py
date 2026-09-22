from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_video_detail_response_diamonds_details import (
        WebcastLiveAnalyticsVideoDetailResponseDiamondsDetails,
    )


T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseNewEarnings")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseNewEarnings:
    """
    Attributes:
        diamonds (float):
        diamonds_details (WebcastLiveAnalyticsVideoDetailResponseDiamondsDetails):
        last_diamonds (float):
    """

    diamonds: float
    diamonds_details: WebcastLiveAnalyticsVideoDetailResponseDiamondsDetails
    last_diamonds: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        diamonds = self.diamonds

        diamonds_details = self.diamonds_details.to_dict()

        last_diamonds = self.last_diamonds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "diamonds": diamonds,
                "diamonds_details": diamonds_details,
                "last_diamonds": last_diamonds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_live_analytics_video_detail_response_diamonds_details import (
            WebcastLiveAnalyticsVideoDetailResponseDiamondsDetails,  # noqa: PLC0415
        )

        d = dict(src_dict)
        diamonds = d.pop("diamonds")

        diamonds_details = WebcastLiveAnalyticsVideoDetailResponseDiamondsDetails.from_dict(d.pop("diamonds_details"))

        last_diamonds = d.pop("last_diamonds")

        webcast_live_analytics_video_detail_response_new_earnings = cls(
            diamonds=diamonds,
            diamonds_details=diamonds_details,
            last_diamonds=last_diamonds,
        )

        webcast_live_analytics_video_detail_response_new_earnings.additional_properties = d
        return webcast_live_analytics_video_detail_response_new_earnings

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

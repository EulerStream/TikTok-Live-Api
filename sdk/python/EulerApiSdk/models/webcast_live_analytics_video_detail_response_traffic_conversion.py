from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseTrafficConversion")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseTrafficConversion:
    """
    Attributes:
        gifters (float):
        impression_viewers (float):
        unique_viewers (float):
    """

    gifters: float
    impression_viewers: float
    unique_viewers: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gifters = self.gifters

        impression_viewers = self.impression_viewers

        unique_viewers = self.unique_viewers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gifters": gifters,
                "impression_viewers": impression_viewers,
                "unique_viewers": unique_viewers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gifters = d.pop("gifters")

        impression_viewers = d.pop("impression_viewers")

        unique_viewers = d.pop("unique_viewers")

        webcast_live_analytics_video_detail_response_traffic_conversion = cls(
            gifters=gifters,
            impression_viewers=impression_viewers,
            unique_viewers=unique_viewers,
        )

        webcast_live_analytics_video_detail_response_traffic_conversion.additional_properties = d
        return webcast_live_analytics_video_detail_response_traffic_conversion

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

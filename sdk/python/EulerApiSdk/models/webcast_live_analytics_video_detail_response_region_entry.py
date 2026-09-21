from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseRegionEntry")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseRegionEntry:
    """
    Attributes:
        percent (float):
        region_name (str):
    """

    percent: float
    region_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        percent = self.percent

        region_name = self.region_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "percent": percent,
                "region_name": region_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        percent = d.pop("percent")

        region_name = d.pop("region_name")

        webcast_live_analytics_video_detail_response_region_entry = cls(
            percent=percent,
            region_name=region_name,
        )

        webcast_live_analytics_video_detail_response_region_entry.additional_properties = d
        return webcast_live_analytics_video_detail_response_region_entry

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

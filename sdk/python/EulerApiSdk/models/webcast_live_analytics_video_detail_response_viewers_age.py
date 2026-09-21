from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseViewersAge")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseViewersAge:
    """
    Attributes:
        age_section (str):
        percent (float):
    """

    age_section: str
    percent: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        age_section = self.age_section

        percent = self.percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "age_section": age_section,
                "percent": percent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        age_section = d.pop("age_section")

        percent = d.pop("percent")

        webcast_live_analytics_video_detail_response_viewers_age = cls(
            age_section=age_section,
            percent=percent,
        )

        webcast_live_analytics_video_detail_response_viewers_age.additional_properties = d
        return webcast_live_analytics_video_detail_response_viewers_age

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

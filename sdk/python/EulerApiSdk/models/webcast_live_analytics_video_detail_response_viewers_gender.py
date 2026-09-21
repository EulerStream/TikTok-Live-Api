from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastLiveAnalyticsVideoDetailResponseViewersGender")


@_attrs_define
class WebcastLiveAnalyticsVideoDetailResponseViewersGender:
    """
    Attributes:
        female_percent (float):
        male_percent (float):
    """

    female_percent: float
    male_percent: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        female_percent = self.female_percent

        male_percent = self.male_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "female_percent": female_percent,
                "male_percent": male_percent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        female_percent = d.pop("female_percent")

        male_percent = d.pop("male_percent")

        webcast_live_analytics_video_detail_response_viewers_gender = cls(
            female_percent=female_percent,
            male_percent=male_percent,
        )

        webcast_live_analytics_video_detail_response_viewers_gender.additional_properties = d
        return webcast_live_analytics_video_detail_response_viewers_gender

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_video_list_response import WebcastLiveAnalyticsVideoListResponse


T = TypeVar("T", bound="WebcastLiveAnalyticsVideoListRouteOutput")


@_attrs_define
class WebcastLiveAnalyticsVideoListRouteOutput:
    """
    Attributes:
        data (WebcastLiveAnalyticsVideoListResponse):
    """

    data: WebcastLiveAnalyticsVideoListResponse
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_live_analytics_video_list_response import (
            WebcastLiveAnalyticsVideoListResponse,  # noqa: PLC0415
        )

        d = dict(src_dict)
        data = WebcastLiveAnalyticsVideoListResponse.from_dict(d.pop("data"))

        webcast_live_analytics_video_list_route_output = cls(
            data=data,
        )

        webcast_live_analytics_video_list_route_output.additional_properties = d
        return webcast_live_analytics_video_list_route_output

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

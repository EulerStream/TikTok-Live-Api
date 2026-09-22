from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_feed_response_stream_url_live_core_sdk_data_pull_data_options_default_quality import (
        WebcastFeedResponseStreamUrlLiveCoreSdkDataPullDataOptionsDefaultQuality,
    )


T = TypeVar("T", bound="WebcastFeedResponseStreamUrlLiveCoreSdkDataPullDataOptions")


@_attrs_define
class WebcastFeedResponseStreamUrlLiveCoreSdkDataPullDataOptions:
    """
    Attributes:
        default_quality (WebcastFeedResponseStreamUrlLiveCoreSdkDataPullDataOptionsDefaultQuality):
    """

    default_quality: WebcastFeedResponseStreamUrlLiveCoreSdkDataPullDataOptionsDefaultQuality
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_quality = self.default_quality.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "default_quality": default_quality,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_feed_response_stream_url_live_core_sdk_data_pull_data_options_default_quality import (
            WebcastFeedResponseStreamUrlLiveCoreSdkDataPullDataOptionsDefaultQuality,  # noqa: PLC0415
        )

        d = dict(src_dict)
        default_quality = WebcastFeedResponseStreamUrlLiveCoreSdkDataPullDataOptionsDefaultQuality.from_dict(
            d.pop("default_quality")
        )

        webcast_feed_response_stream_url_live_core_sdk_data_pull_data_options = cls(
            default_quality=default_quality,
        )

        webcast_feed_response_stream_url_live_core_sdk_data_pull_data_options.additional_properties = d
        return webcast_feed_response_stream_url_live_core_sdk_data_pull_data_options

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

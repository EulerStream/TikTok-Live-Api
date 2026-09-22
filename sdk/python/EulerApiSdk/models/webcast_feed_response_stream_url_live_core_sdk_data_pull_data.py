from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_feed_response_stream_url_live_core_sdk_data_pull_data_options import (
        WebcastFeedResponseStreamUrlLiveCoreSdkDataPullDataOptions,
    )


T = TypeVar("T", bound="WebcastFeedResponseStreamUrlLiveCoreSdkDataPullData")


@_attrs_define
class WebcastFeedResponseStreamUrlLiveCoreSdkDataPullData:
    """
    Attributes:
        options (WebcastFeedResponseStreamUrlLiveCoreSdkDataPullDataOptions):
        stream_data (str):
    """

    options: WebcastFeedResponseStreamUrlLiveCoreSdkDataPullDataOptions
    stream_data: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        options = self.options.to_dict()

        stream_data = self.stream_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "options": options,
                "stream_data": stream_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_feed_response_stream_url_live_core_sdk_data_pull_data_options import (
            WebcastFeedResponseStreamUrlLiveCoreSdkDataPullDataOptions,  # noqa: PLC0415
        )

        d = dict(src_dict)
        options = WebcastFeedResponseStreamUrlLiveCoreSdkDataPullDataOptions.from_dict(d.pop("options"))

        stream_data = d.pop("stream_data")

        webcast_feed_response_stream_url_live_core_sdk_data_pull_data = cls(
            options=options,
            stream_data=stream_data,
        )

        webcast_feed_response_stream_url_live_core_sdk_data_pull_data.additional_properties = d
        return webcast_feed_response_stream_url_live_core_sdk_data_pull_data

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

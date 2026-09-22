from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_feed_response_stream_url_live_core_sdk_data_pull_data import (
        WebcastFeedResponseStreamUrlLiveCoreSdkDataPullData,
    )


T = TypeVar("T", bound="WebcastFeedResponseStreamUrlLiveCoreSdkData")


@_attrs_define
class WebcastFeedResponseStreamUrlLiveCoreSdkData:
    """
    Attributes:
        pull_data (WebcastFeedResponseStreamUrlLiveCoreSdkDataPullData):
    """

    pull_data: WebcastFeedResponseStreamUrlLiveCoreSdkDataPullData
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pull_data = self.pull_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pull_data": pull_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_feed_response_stream_url_live_core_sdk_data_pull_data import (
            WebcastFeedResponseStreamUrlLiveCoreSdkDataPullData,  # noqa: PLC0415
        )

        d = dict(src_dict)
        pull_data = WebcastFeedResponseStreamUrlLiveCoreSdkDataPullData.from_dict(d.pop("pull_data"))

        webcast_feed_response_stream_url_live_core_sdk_data = cls(
            pull_data=pull_data,
        )

        webcast_feed_response_stream_url_live_core_sdk_data.additional_properties = d
        return webcast_feed_response_stream_url_live_core_sdk_data

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

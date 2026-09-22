from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webcast_feed_response_stream_url_flv_pull_url import WebcastFeedResponseStreamUrlFlvPullUrl
    from ..models.webcast_feed_response_stream_url_flv_pull_url_params import (
        WebcastFeedResponseStreamUrlFlvPullUrlParams,
    )
    from ..models.webcast_feed_response_stream_url_live_core_sdk_data import WebcastFeedResponseStreamUrlLiveCoreSdkData


T = TypeVar("T", bound="WebcastFeedResponseStreamUrl")


@_attrs_define
class WebcastFeedResponseStreamUrl:
    """
    Attributes:
        rtmp_pull_url (str):
        flv_pull_url (WebcastFeedResponseStreamUrlFlvPullUrl):
        stream_size_width (float):
        stream_size_height (float):
        flv_pull_url_params (WebcastFeedResponseStreamUrlFlvPullUrlParams | Unset):
        live_core_sdk_data (WebcastFeedResponseStreamUrlLiveCoreSdkData | Unset):
    """

    rtmp_pull_url: str
    flv_pull_url: WebcastFeedResponseStreamUrlFlvPullUrl
    stream_size_width: float
    stream_size_height: float
    flv_pull_url_params: WebcastFeedResponseStreamUrlFlvPullUrlParams | Unset = UNSET
    live_core_sdk_data: WebcastFeedResponseStreamUrlLiveCoreSdkData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rtmp_pull_url = self.rtmp_pull_url

        flv_pull_url = self.flv_pull_url.to_dict()

        stream_size_width = self.stream_size_width

        stream_size_height = self.stream_size_height

        flv_pull_url_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.flv_pull_url_params, Unset):
            flv_pull_url_params = self.flv_pull_url_params.to_dict()

        live_core_sdk_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live_core_sdk_data, Unset):
            live_core_sdk_data = self.live_core_sdk_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rtmp_pull_url": rtmp_pull_url,
                "flv_pull_url": flv_pull_url,
                "stream_size_width": stream_size_width,
                "stream_size_height": stream_size_height,
            }
        )
        if flv_pull_url_params is not UNSET:
            field_dict["flv_pull_url_params"] = flv_pull_url_params
        if live_core_sdk_data is not UNSET:
            field_dict["live_core_sdk_data"] = live_core_sdk_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_feed_response_stream_url_flv_pull_url import (
            WebcastFeedResponseStreamUrlFlvPullUrl,  # noqa: PLC0415
        )
        from ..models.webcast_feed_response_stream_url_flv_pull_url_params import (
            WebcastFeedResponseStreamUrlFlvPullUrlParams,  # noqa: PLC0415
        )
        from ..models.webcast_feed_response_stream_url_live_core_sdk_data import (
            WebcastFeedResponseStreamUrlLiveCoreSdkData,  # noqa: PLC0415
        )

        d = dict(src_dict)
        rtmp_pull_url = d.pop("rtmp_pull_url")

        flv_pull_url = WebcastFeedResponseStreamUrlFlvPullUrl.from_dict(d.pop("flv_pull_url"))

        stream_size_width = d.pop("stream_size_width")

        stream_size_height = d.pop("stream_size_height")

        _flv_pull_url_params = d.pop("flv_pull_url_params", UNSET)
        flv_pull_url_params: WebcastFeedResponseStreamUrlFlvPullUrlParams | Unset
        if isinstance(_flv_pull_url_params, Unset):
            flv_pull_url_params = UNSET
        else:
            flv_pull_url_params = WebcastFeedResponseStreamUrlFlvPullUrlParams.from_dict(_flv_pull_url_params)

        _live_core_sdk_data = d.pop("live_core_sdk_data", UNSET)
        live_core_sdk_data: WebcastFeedResponseStreamUrlLiveCoreSdkData | Unset
        if isinstance(_live_core_sdk_data, Unset):
            live_core_sdk_data = UNSET
        else:
            live_core_sdk_data = WebcastFeedResponseStreamUrlLiveCoreSdkData.from_dict(_live_core_sdk_data)

        webcast_feed_response_stream_url = cls(
            rtmp_pull_url=rtmp_pull_url,
            flv_pull_url=flv_pull_url,
            stream_size_width=stream_size_width,
            stream_size_height=stream_size_height,
            flv_pull_url_params=flv_pull_url_params,
            live_core_sdk_data=live_core_sdk_data,
        )

        webcast_feed_response_stream_url.additional_properties = d
        return webcast_feed_response_stream_url

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

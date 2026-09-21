from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastEventImage")


@_attrs_define
class WebcastEventImage:
    """Look up a single TikTok LIVE event (a scheduled/subscription stream) by its `event_id` via the unsigned
    `/tiktok/event/get/v1` endpoint on `webcast.tiktok.com`. No cookies and no signature are required; every query param
    is a baked-in constant except `event_id` and a generated `device_id`. The request is routed through the caller-
    provided proxy (the route does not self-select one). Success is signalled by a top-level `status_code === 0` with an
    `event` payload.

        Attributes:
            uri (str):
            url_list (list[str]):
            width (float):
            height (float):
            url_prefix (None | str):
    """

    uri: str
    url_list: list[str]
    width: float
    height: float
    url_prefix: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uri = self.uri

        url_list = self.url_list

        width = self.width

        height = self.height

        url_prefix: None | str
        url_prefix = self.url_prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uri": uri,
                "url_list": url_list,
                "width": width,
                "height": height,
                "url_prefix": url_prefix,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uri = d.pop("uri")

        url_list = cast(list[str], d.pop("url_list"))

        width = d.pop("width")

        height = d.pop("height")

        def _parse_url_prefix(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        url_prefix = _parse_url_prefix(d.pop("url_prefix"))

        webcast_event_image = cls(
            uri=uri,
            url_list=url_list,
            width=width,
            height=height,
            url_prefix=url_prefix,
        )

        webcast_event_image.additional_properties = d
        return webcast_event_image

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

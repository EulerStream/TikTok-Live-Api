from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stable_stream_quality import StableStreamQuality
from ..models.stable_stream_type import StableStreamType

T = TypeVar("T", bound="StableStreamUrl")


@_attrs_define
class StableStreamUrl:
    """
    Attributes:
        url (str): Direct playback URL.
        quality (StableStreamQuality): Mirrors of the SDK's `StreamQuality` / `StreamType` enums as literal unions.

            Declared here rather than re-exported so the published spec is decoupled from SDK churn — the same reason the
            rest of this file exists. Same precedent as `RoomInfoForceSourceHeader`.
        type_ (StableStreamType):
    """

    url: str
    quality: StableStreamQuality
    type_: StableStreamType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        quality = self.quality.value

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "quality": quality,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        quality = StableStreamQuality(d.pop("quality"))

        type_ = StableStreamType(d.pop("type"))

        stable_stream_url = cls(
            url=url,
            quality=quality,
            type_=type_,
        )

        stable_stream_url.additional_properties = d
        return stable_stream_url

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

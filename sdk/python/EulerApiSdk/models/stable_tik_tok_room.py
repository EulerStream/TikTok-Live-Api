from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stable_stream_url import StableStreamUrl


T = TypeVar("T", bound="StableTikTokRoom")


@_attrs_define
class StableTikTokRoom:
    """
    Attributes:
        stream_urls (list[StableStreamUrl]): Every playback URL the room published. Always present, but empty for
            offline rooms and for live rooms TikTok served without stream metadata.
        status (float | Unset):
        is_live (bool | Unset):
        id (str | Unset):
        cover_url (str | Unset):
        title (str | Unset):
        start_time (float | Unset):
    """

    stream_urls: list[StableStreamUrl]
    status: float | Unset = UNSET
    is_live: bool | Unset = UNSET
    id: str | Unset = UNSET
    cover_url: str | Unset = UNSET
    title: str | Unset = UNSET
    start_time: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stream_urls = []
        for stream_urls_item_data in self.stream_urls:
            stream_urls_item = stream_urls_item_data.to_dict()
            stream_urls.append(stream_urls_item)

        status = self.status

        is_live = self.is_live

        id = self.id

        cover_url = self.cover_url

        title = self.title

        start_time = self.start_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stream_urls": stream_urls,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if is_live is not UNSET:
            field_dict["is_live"] = is_live
        if id is not UNSET:
            field_dict["id"] = id
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url
        if title is not UNSET:
            field_dict["title"] = title
        if start_time is not UNSET:
            field_dict["start_time"] = start_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stable_stream_url import StableStreamUrl

        d = dict(src_dict)
        stream_urls = []
        _stream_urls = d.pop("stream_urls")
        for stream_urls_item_data in _stream_urls:
            stream_urls_item = StableStreamUrl.from_dict(stream_urls_item_data)

            stream_urls.append(stream_urls_item)

        status = d.pop("status", UNSET)

        is_live = d.pop("is_live", UNSET)

        id = d.pop("id", UNSET)

        cover_url = d.pop("cover_url", UNSET)

        title = d.pop("title", UNSET)

        start_time = d.pop("start_time", UNSET)

        stable_tik_tok_room = cls(
            stream_urls=stream_urls,
            status=status,
            is_live=is_live,
            id=id,
            cover_url=cover_url,
            title=title,
            start_time=start_time,
        )

        stable_tik_tok_room.additional_properties = d
        return stable_tik_tok_room

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

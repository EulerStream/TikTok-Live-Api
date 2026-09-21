from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TikTokUserDetailedVideo")


@_attrs_define
class TikTokUserDetailedVideo:
    """
    Attributes:
        id (str):
        thumbnail (str):
        animated_thumbnail (str): The video's dynamic cover; the still again when the video has no animated one.
        description (str):
        views (float):
        video_url (str):
    """

    id: str
    thumbnail: str
    animated_thumbnail: str
    description: str
    views: float
    video_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        thumbnail = self.thumbnail

        animated_thumbnail = self.animated_thumbnail

        description = self.description

        views = self.views

        video_url = self.video_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "thumbnail": thumbnail,
                "animated_thumbnail": animated_thumbnail,
                "description": description,
                "views": views,
                "video_url": video_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        thumbnail = d.pop("thumbnail")

        animated_thumbnail = d.pop("animated_thumbnail")

        description = d.pop("description")

        views = d.pop("views")

        video_url = d.pop("video_url")

        tik_tok_user_detailed_video = cls(
            id=id,
            thumbnail=thumbnail,
            animated_thumbnail=animated_thumbnail,
            description=description,
            views=views,
            video_url=video_url,
        )

        tik_tok_user_detailed_video.additional_properties = d
        return tik_tok_user_detailed_video

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tik_tok_video_basic_music import TikTokVideoBasicMusic


T = TypeVar("T", bound="TikTokVideoBasicVideo")


@_attrs_define
class TikTokVideoBasicVideo:
    """
    Attributes:
        id (str):
        thumbnail (str):
        description (str):
        hashtags (list[str]):
        music (TikTokVideoBasicMusic):
    """

    id: str
    thumbnail: str
    description: str
    hashtags: list[str]
    music: TikTokVideoBasicMusic
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        thumbnail = self.thumbnail

        description = self.description

        hashtags = self.hashtags

        music = self.music.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "thumbnail": thumbnail,
                "description": description,
                "hashtags": hashtags,
                "music": music,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tik_tok_video_basic_music import TikTokVideoBasicMusic

        d = dict(src_dict)
        id = d.pop("id")

        thumbnail = d.pop("thumbnail")

        description = d.pop("description")

        hashtags = cast(list[str], d.pop("hashtags"))

        music = TikTokVideoBasicMusic.from_dict(d.pop("music"))

        tik_tok_video_basic_video = cls(
            id=id,
            thumbnail=thumbnail,
            description=description,
            hashtags=hashtags,
            music=music,
        )

        tik_tok_video_basic_video.additional_properties = d
        return tik_tok_video_basic_video

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

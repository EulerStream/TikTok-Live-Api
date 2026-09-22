from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tik_tok_video_basic_author import TikTokVideoBasicAuthor
    from ..models.tik_tok_video_basic_video import TikTokVideoBasicVideo


T = TypeVar("T", bound="RetrieveTikTokVideoBasicResponse")


@_attrs_define
class RetrieveTikTokVideoBasicResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        video (TikTokVideoBasicVideo | Unset):
        author (TikTokVideoBasicAuthor | Unset):
    """

    code: float
    message: str | Unset = UNSET
    video: TikTokVideoBasicVideo | Unset = UNSET
    author: TikTokVideoBasicAuthor | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        video: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video, Unset):
            video = self.video.to_dict()

        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if video is not UNSET:
            field_dict["video"] = video
        if author is not UNSET:
            field_dict["author"] = author

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tik_tok_video_basic_author import TikTokVideoBasicAuthor  # noqa: PLC0415
        from ..models.tik_tok_video_basic_video import TikTokVideoBasicVideo  # noqa: PLC0415

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _video = d.pop("video", UNSET)
        video: TikTokVideoBasicVideo | Unset
        if isinstance(_video, Unset):
            video = UNSET
        else:
            video = TikTokVideoBasicVideo.from_dict(_video)

        _author = d.pop("author", UNSET)
        author: TikTokVideoBasicAuthor | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = TikTokVideoBasicAuthor.from_dict(_author)

        retrieve_tik_tok_video_basic_response = cls(
            code=code,
            message=message,
            video=video,
            author=author,
        )

        retrieve_tik_tok_video_basic_response.additional_properties = d
        return retrieve_tik_tok_video_basic_response

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tik_tok_user_detailed_user import TikTokUserDetailedUser
    from ..models.tik_tok_user_detailed_video import TikTokUserDetailedVideo


T = TypeVar("T", bound="RetrieveTikTokUserDetailedResponse")


@_attrs_define
class RetrieveTikTokUserDetailedResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        user (TikTokUserDetailedUser | Unset):
        videos (list[TikTokUserDetailedVideo] | Unset): The user's latest videos, newest first.
    """

    code: float
    message: str | Unset = UNSET
    user: TikTokUserDetailedUser | Unset = UNSET
    videos: list[TikTokUserDetailedVideo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        videos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.videos, Unset):
            videos = []
            for videos_item_data in self.videos:
                videos_item = videos_item_data.to_dict()
                videos.append(videos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if user is not UNSET:
            field_dict["user"] = user
        if videos is not UNSET:
            field_dict["videos"] = videos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tik_tok_user_detailed_user import TikTokUserDetailedUser
        from ..models.tik_tok_user_detailed_video import TikTokUserDetailedVideo

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _user = d.pop("user", UNSET)
        user: TikTokUserDetailedUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = TikTokUserDetailedUser.from_dict(_user)

        _videos = d.pop("videos", UNSET)
        videos: list[TikTokUserDetailedVideo] | Unset = UNSET
        if _videos is not UNSET:
            videos = []
            for videos_item_data in _videos:
                videos_item = TikTokUserDetailedVideo.from_dict(videos_item_data)

                videos.append(videos_item)

        retrieve_tik_tok_user_detailed_response = cls(
            code=code,
            message=message,
            user=user,
            videos=videos,
        )

        retrieve_tik_tok_user_detailed_response.additional_properties = d
        return retrieve_tik_tok_user_detailed_response

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TikTokUserDetailedUser")


@_attrs_define
class TikTokUserDetailedUser:
    """
    Attributes:
        unique_id (str):
        avatar_url (str):
        nickname (str):
        numeric_uid (str):
        signature (str):
        is_verified (bool):
        following (float):
        followers (float):
        likes (float):
        is_private (bool):
    """

    unique_id: str
    avatar_url: str
    nickname: str
    numeric_uid: str
    signature: str
    is_verified: bool
    following: float
    followers: float
    likes: float
    is_private: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unique_id = self.unique_id

        avatar_url = self.avatar_url

        nickname = self.nickname

        numeric_uid = self.numeric_uid

        signature = self.signature

        is_verified = self.is_verified

        following = self.following

        followers = self.followers

        likes = self.likes

        is_private = self.is_private

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unique_id": unique_id,
                "avatar_url": avatar_url,
                "nickname": nickname,
                "numeric_uid": numeric_uid,
                "signature": signature,
                "is_verified": is_verified,
                "following": following,
                "followers": followers,
                "likes": likes,
                "is_private": is_private,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unique_id = d.pop("unique_id")

        avatar_url = d.pop("avatar_url")

        nickname = d.pop("nickname")

        numeric_uid = d.pop("numeric_uid")

        signature = d.pop("signature")

        is_verified = d.pop("is_verified")

        following = d.pop("following")

        followers = d.pop("followers")

        likes = d.pop("likes")

        is_private = d.pop("is_private")

        tik_tok_user_detailed_user = cls(
            unique_id=unique_id,
            avatar_url=avatar_url,
            nickname=nickname,
            numeric_uid=numeric_uid,
            signature=signature,
            is_verified=is_verified,
            following=following,
            followers=followers,
            likes=likes,
            is_private=is_private,
        )

        tik_tok_user_detailed_user.additional_properties = d
        return tik_tok_user_detailed_user

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

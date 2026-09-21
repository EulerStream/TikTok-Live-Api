from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StableTikTokRoomUser")


@_attrs_define
class StableTikTokRoomUser:
    """
    Attributes:
        unique_id (str):
        avatar_url (str | Unset):
        nickname (str | Unset):
        sec_uid (str | Unset):
        numeric_uid (str | Unset):
        signature (str | Unset):
        is_verified (bool | Unset):
        following (float | Unset):
        followers (float | Unset):
    """

    unique_id: str
    avatar_url: str | Unset = UNSET
    nickname: str | Unset = UNSET
    sec_uid: str | Unset = UNSET
    numeric_uid: str | Unset = UNSET
    signature: str | Unset = UNSET
    is_verified: bool | Unset = UNSET
    following: float | Unset = UNSET
    followers: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unique_id = self.unique_id

        avatar_url = self.avatar_url

        nickname = self.nickname

        sec_uid = self.sec_uid

        numeric_uid = self.numeric_uid

        signature = self.signature

        is_verified = self.is_verified

        following = self.following

        followers = self.followers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unique_id": unique_id,
            }
        )
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if sec_uid is not UNSET:
            field_dict["sec_uid"] = sec_uid
        if numeric_uid is not UNSET:
            field_dict["numeric_uid"] = numeric_uid
        if signature is not UNSET:
            field_dict["signature"] = signature
        if is_verified is not UNSET:
            field_dict["is_verified"] = is_verified
        if following is not UNSET:
            field_dict["following"] = following
        if followers is not UNSET:
            field_dict["followers"] = followers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unique_id = d.pop("unique_id")

        avatar_url = d.pop("avatar_url", UNSET)

        nickname = d.pop("nickname", UNSET)

        sec_uid = d.pop("sec_uid", UNSET)

        numeric_uid = d.pop("numeric_uid", UNSET)

        signature = d.pop("signature", UNSET)

        is_verified = d.pop("is_verified", UNSET)

        following = d.pop("following", UNSET)

        followers = d.pop("followers", UNSET)

        stable_tik_tok_room_user = cls(
            unique_id=unique_id,
            avatar_url=avatar_url,
            nickname=nickname,
            sec_uid=sec_uid,
            numeric_uid=numeric_uid,
            signature=signature,
            is_verified=is_verified,
            following=following,
            followers=followers,
        )

        stable_tik_tok_room_user.additional_properties = d
        return stable_tik_tok_room_user

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

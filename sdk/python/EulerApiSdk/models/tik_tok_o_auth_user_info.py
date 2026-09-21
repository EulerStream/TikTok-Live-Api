from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TikTokOAuthUserInfo")


@_attrs_define
class TikTokOAuthUserInfo:
    """
    Attributes:
        uid (str | Unset):
        sec_uid (str | Unset):
        nick_name (str | Unset):
        unique_id (str | Unset):
        region (str | Unset):
        avatar_url (str | Unset):
        room_id (str | Unset):
        has_live_permission (bool | Unset):
        is_private_account (bool | Unset):
    """

    uid: str | Unset = UNSET
    sec_uid: str | Unset = UNSET
    nick_name: str | Unset = UNSET
    unique_id: str | Unset = UNSET
    region: str | Unset = UNSET
    avatar_url: str | Unset = UNSET
    room_id: str | Unset = UNSET
    has_live_permission: bool | Unset = UNSET
    is_private_account: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uid = self.uid

        sec_uid = self.sec_uid

        nick_name = self.nick_name

        unique_id = self.unique_id

        region = self.region

        avatar_url = self.avatar_url

        room_id = self.room_id

        has_live_permission = self.has_live_permission

        is_private_account = self.is_private_account

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uid is not UNSET:
            field_dict["uid"] = uid
        if sec_uid is not UNSET:
            field_dict["secUid"] = sec_uid
        if nick_name is not UNSET:
            field_dict["nickName"] = nick_name
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if region is not UNSET:
            field_dict["region"] = region
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if has_live_permission is not UNSET:
            field_dict["hasLivePermission"] = has_live_permission
        if is_private_account is not UNSET:
            field_dict["isPrivateAccount"] = is_private_account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uid = d.pop("uid", UNSET)

        sec_uid = d.pop("secUid", UNSET)

        nick_name = d.pop("nickName", UNSET)

        unique_id = d.pop("uniqueId", UNSET)

        region = d.pop("region", UNSET)

        avatar_url = d.pop("avatarUrl", UNSET)

        room_id = d.pop("roomId", UNSET)

        has_live_permission = d.pop("hasLivePermission", UNSET)

        is_private_account = d.pop("isPrivateAccount", UNSET)

        tik_tok_o_auth_user_info = cls(
            uid=uid,
            sec_uid=sec_uid,
            nick_name=nick_name,
            unique_id=unique_id,
            region=region,
            avatar_url=avatar_url,
            room_id=room_id,
            has_live_permission=has_live_permission,
            is_private_account=is_private_account,
        )

        tik_tok_o_auth_user_info.additional_properties = d
        return tik_tok_o_auth_user_info

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

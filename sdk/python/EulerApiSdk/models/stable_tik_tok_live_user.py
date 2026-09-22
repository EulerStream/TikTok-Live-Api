from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stable_tik_tok_live_user_raw import StableTikTokLiveUserRaw
    from ..models.stable_tik_tok_room import StableTikTokRoom
    from ..models.stable_tik_tok_room_user import StableTikTokRoomUser


T = TypeVar("T", bound="StableTikTokLiveUser")


@_attrs_define
class StableTikTokLiveUser:
    """
    Attributes:
        unique_id (str):
        raw (StableTikTokLiveUserRaw):
        user (StableTikTokRoomUser | Unset):
        room_info (StableTikTokRoom | Unset):
    """

    unique_id: str
    raw: StableTikTokLiveUserRaw
    user: StableTikTokRoomUser | Unset = UNSET
    room_info: StableTikTokRoom | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unique_id = self.unique_id

        raw = self.raw.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        room_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.room_info, Unset):
            room_info = self.room_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unique_id": unique_id,
                "raw": raw,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user
        if room_info is not UNSET:
            field_dict["room_info"] = room_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stable_tik_tok_live_user_raw import StableTikTokLiveUserRaw  # noqa: PLC0415
        from ..models.stable_tik_tok_room import StableTikTokRoom  # noqa: PLC0415
        from ..models.stable_tik_tok_room_user import StableTikTokRoomUser  # noqa: PLC0415

        d = dict(src_dict)
        unique_id = d.pop("unique_id")

        raw = StableTikTokLiveUserRaw.from_dict(d.pop("raw"))

        _user = d.pop("user", UNSET)
        user: StableTikTokRoomUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = StableTikTokRoomUser.from_dict(_user)

        _room_info = d.pop("room_info", UNSET)
        room_info: StableTikTokRoom | Unset
        if isinstance(_room_info, Unset):
            room_info = UNSET
        else:
            room_info = StableTikTokRoom.from_dict(_room_info)

        stable_tik_tok_live_user = cls(
            unique_id=unique_id,
            raw=raw,
            user=user,
            room_info=room_info,
        )

        stable_tik_tok_live_user.additional_properties = d
        return stable_tik_tok_live_user

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebcastRoomChatPayloadV1")


@_attrs_define
class WebcastRoomChatPayloadV1:
    """
    Attributes:
        content (str): The chat message content to send
        target_room_id (str | Unset):
        target_unique_id (str | Unset): The username of the room to send the chat to (either this or targetRoomId is
            required).
            Pass room_id = 0 to parameter for this to work.
        session_id (str | Unset):
        tt_target_idc (str | Unset):
        room_id (str | Unset):
    """

    content: str
    target_room_id: str | Unset = UNSET
    target_unique_id: str | Unset = UNSET
    session_id: str | Unset = UNSET
    tt_target_idc: str | Unset = UNSET
    room_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        target_room_id = self.target_room_id

        target_unique_id = self.target_unique_id

        session_id = self.session_id

        tt_target_idc = self.tt_target_idc

        room_id = self.room_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if target_room_id is not UNSET:
            field_dict["targetRoomId"] = target_room_id
        if target_unique_id is not UNSET:
            field_dict["targetUniqueId"] = target_unique_id
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if tt_target_idc is not UNSET:
            field_dict["ttTargetIdc"] = tt_target_idc
        if room_id is not UNSET:
            field_dict["roomId"] = room_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        target_room_id = d.pop("targetRoomId", UNSET)

        target_unique_id = d.pop("targetUniqueId", UNSET)

        session_id = d.pop("sessionId", UNSET)

        tt_target_idc = d.pop("ttTargetIdc", UNSET)

        room_id = d.pop("roomId", UNSET)

        webcast_room_chat_payload_v1 = cls(
            content=content,
            target_room_id=target_room_id,
            target_unique_id=target_unique_id,
            session_id=session_id,
            tt_target_idc=tt_target_idc,
            room_id=room_id,
        )

        webcast_room_chat_payload_v1.additional_properties = d
        return webcast_room_chat_payload_v1

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

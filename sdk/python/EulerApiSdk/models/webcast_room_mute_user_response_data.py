from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastRoomMuteUserResponseData")


@_attrs_define
class WebcastRoomMuteUserResponseData:
    """
    Attributes:
        actual_duration (float):
        max_count (float):
        room_id (float):
        total (float):
        user_id (float):
    """

    actual_duration: float
    max_count: float
    room_id: float
    total: float
    user_id: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actual_duration = self.actual_duration

        max_count = self.max_count

        room_id = self.room_id

        total = self.total

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actual_duration": actual_duration,
                "max_count": max_count,
                "room_id": room_id,
                "total": total,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        actual_duration = d.pop("actual_duration")

        max_count = d.pop("max_count")

        room_id = d.pop("room_id")

        total = d.pop("total")

        user_id = d.pop("user_id")

        webcast_room_mute_user_response_data = cls(
            actual_duration=actual_duration,
            max_count=max_count,
            room_id=room_id,
            total=total,
            user_id=user_id,
        )

        webcast_room_mute_user_response_data.additional_properties = d
        return webcast_room_mute_user_response_data

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

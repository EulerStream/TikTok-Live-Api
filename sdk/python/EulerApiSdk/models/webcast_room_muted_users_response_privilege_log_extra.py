from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastRoomMutedUsersResponsePrivilegeLogExtra")


@_attrs_define
class WebcastRoomMutedUsersResponsePrivilegeLogExtra:
    """
    Attributes:
        data_version (str):
        end_time (float):
        level (str):
        privilege_id (str):
        privilege_order_id (str):
        privilege_version (str):
        start_time (float):
    """

    data_version: str
    end_time: float
    level: str
    privilege_id: str
    privilege_order_id: str
    privilege_version: str
    start_time: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_version = self.data_version

        end_time = self.end_time

        level = self.level

        privilege_id = self.privilege_id

        privilege_order_id = self.privilege_order_id

        privilege_version = self.privilege_version

        start_time = self.start_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_version": data_version,
                "end_time": end_time,
                "level": level,
                "privilege_id": privilege_id,
                "privilege_order_id": privilege_order_id,
                "privilege_version": privilege_version,
                "start_time": start_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_version = d.pop("data_version")

        end_time = d.pop("end_time")

        level = d.pop("level")

        privilege_id = d.pop("privilege_id")

        privilege_order_id = d.pop("privilege_order_id")

        privilege_version = d.pop("privilege_version")

        start_time = d.pop("start_time")

        webcast_room_muted_users_response_privilege_log_extra = cls(
            data_version=data_version,
            end_time=end_time,
            level=level,
            privilege_id=privilege_id,
            privilege_order_id=privilege_order_id,
            privilege_version=privilege_version,
            start_time=start_time,
        )

        webcast_room_muted_users_response_privilege_log_extra.additional_properties = d
        return webcast_room_muted_users_response_privilege_log_extra

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

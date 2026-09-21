from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastRoomKickedUsersResponseExtra")


@_attrs_define
class WebcastRoomKickedUsersResponseExtra:
    """
    Attributes:
        has_more (bool):
        next_cursor (float):
        now (float):
        total (float):
    """

    has_more: bool
    next_cursor: float
    now: float
    total: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_more = self.has_more

        next_cursor = self.next_cursor

        now = self.now

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "has_more": has_more,
                "next_cursor": next_cursor,
                "now": now,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_more = d.pop("has_more")

        next_cursor = d.pop("next_cursor")

        now = d.pop("now")

        total = d.pop("total")

        webcast_room_kicked_users_response_extra = cls(
            has_more=has_more,
            next_cursor=next_cursor,
            now=now,
            total=total,
        )

        webcast_room_kicked_users_response_extra.additional_properties = d
        return webcast_room_kicked_users_response_extra

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

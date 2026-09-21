from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebcastRoomMutedUsersResponseBadgeText")


@_attrs_define
class WebcastRoomMutedUsersResponseBadgeText:
    """
    Attributes:
        default_pattern (str):
        key (str):
        pieces (list[Any]):
        display_type (float | Unset):
    """

    default_pattern: str
    key: str
    pieces: list[Any]
    display_type: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_pattern = self.default_pattern

        key = self.key

        pieces = self.pieces

        display_type = self.display_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "default_pattern": default_pattern,
                "key": key,
                "pieces": pieces,
            }
        )
        if display_type is not UNSET:
            field_dict["display_type"] = display_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_pattern = d.pop("default_pattern")

        key = d.pop("key")

        pieces = cast(list[Any], d.pop("pieces"))

        display_type = d.pop("display_type", UNSET)

        webcast_room_muted_users_response_badge_text = cls(
            default_pattern=default_pattern,
            key=key,
            pieces=pieces,
            display_type=display_type,
        )

        webcast_room_muted_users_response_badge_text.additional_properties = d
        return webcast_room_muted_users_response_badge_text

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

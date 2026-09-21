from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastIsLiveOutputDataAdditionalProperty")


@_attrs_define
class WebcastIsLiveOutputDataAdditionalProperty:
    """
    Attributes:
        is_live (bool):
        room_id (None | str):
    """

    is_live: bool
    room_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_live = self.is_live

        room_id: None | str
        room_id = self.room_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "is_live": is_live,
                "room_id": room_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_live = d.pop("is_live")

        def _parse_room_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        room_id = _parse_room_id(d.pop("room_id"))

        webcast_is_live_output_data_additional_property = cls(
            is_live=is_live,
            room_id=room_id,
        )

        webcast_is_live_output_data_additional_property.additional_properties = d
        return webcast_is_live_output_data_additional_property

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

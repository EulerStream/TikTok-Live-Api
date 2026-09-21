from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebcastRoomIdRouteResponse")


@_attrs_define
class WebcastRoomIdRouteResponse:
    """
    Attributes:
        code (float):
        ok (bool):
        routes_attempted (list[str]):
        message (str | Unset):
        is_live (bool | Unset):
        room_id (str | Unset):
        room_status (float | Unset):
        source (str | Unset):
    """

    code: float
    ok: bool
    routes_attempted: list[str]
    message: str | Unset = UNSET
    is_live: bool | Unset = UNSET
    room_id: str | Unset = UNSET
    room_status: float | Unset = UNSET
    source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        ok = self.ok

        routes_attempted = self.routes_attempted

        message = self.message

        is_live = self.is_live

        room_id = self.room_id

        room_status = self.room_status

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "ok": ok,
                "routes_attempted": routes_attempted,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if is_live is not UNSET:
            field_dict["is_live"] = is_live
        if room_id is not UNSET:
            field_dict["room_id"] = room_id
        if room_status is not UNSET:
            field_dict["room_status"] = room_status
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        ok = d.pop("ok")

        routes_attempted = cast(list[str], d.pop("routes_attempted"))

        message = d.pop("message", UNSET)

        is_live = d.pop("is_live", UNSET)

        room_id = d.pop("room_id", UNSET)

        room_status = d.pop("room_status", UNSET)

        source = d.pop("source", UNSET)

        webcast_room_id_route_response = cls(
            code=code,
            ok=ok,
            routes_attempted=routes_attempted,
            message=message,
            is_live=is_live,
            room_id=room_id,
            room_status=room_status,
            source=source,
        )

        webcast_room_id_route_response.additional_properties = d
        return webcast_room_id_route_response

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

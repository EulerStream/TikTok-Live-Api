from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stable_tik_tok_live_user import StableTikTokLiveUser


T = TypeVar("T", bound="WebcastRoomInfoByRoomIdRouteResponse")


@_attrs_define
class WebcastRoomInfoByRoomIdRouteResponse:
    """
    Attributes:
        code (float):
        ok (bool):
        routes_attempted (list[str]):
        source (None | str): Which source produced `data`. `CACHE` indicates an Euler cache hit. Typed `string` rather
            than `RoomInfoByRoomIdSource`: the pinned SDK (0.15.0) still types this route's `source` as a plain string.
            Tighten to the enum once the SDK carrying the room-info enum restructure is published.
        data (StableTikTokLiveUser):
        message (str | Unset):
    """

    code: float
    ok: bool
    routes_attempted: list[str]
    source: None | str
    data: StableTikTokLiveUser
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        ok = self.ok

        routes_attempted = self.routes_attempted

        source: None | str
        source = self.source

        data = self.data.to_dict()

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "ok": ok,
                "routes_attempted": routes_attempted,
                "source": source,
                "data": data,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stable_tik_tok_live_user import StableTikTokLiveUser  # noqa: PLC0415

        d = dict(src_dict)
        code = d.pop("code")

        ok = d.pop("ok")

        routes_attempted = cast(list[str], d.pop("routes_attempted"))

        def _parse_source(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source = _parse_source(d.pop("source"))

        data = StableTikTokLiveUser.from_dict(d.pop("data"))

        message = d.pop("message", UNSET)

        webcast_room_info_by_room_id_route_response = cls(
            code=code,
            ok=ok,
            routes_attempted=routes_attempted,
            source=source,
            data=data,
            message=message,
        )

        webcast_room_info_by_room_id_route_response.additional_properties = d
        return webcast_room_info_by_room_id_route_response

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

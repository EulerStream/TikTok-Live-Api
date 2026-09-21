from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.room_info_fetch_api_route import RoomInfoFetchApiRoute
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stable_tik_tok_live_user import StableTikTokLiveUser


T = TypeVar("T", bound="WebcastRoomInfoRouteResponse")


@_attrs_define
class WebcastRoomInfoRouteResponse:
    """
    Attributes:
        code (float):
        ok (bool):
        routes_attempted (list[str]):
        source (None | RoomInfoFetchApiRoute): Which source produced `data`. `CACHE` / `CACHE_UNVERIFIED` indicate the
            room info came out of Euler's cache — `CACHE` means its live state was revalidated, `CACHE_UNVERIFIED` means it
            could not be. Without this, `X-Cache-Hit` is a bare boolean and those two are indistinguishable.
        data (StableTikTokLiveUser):
        message (str | Unset):
    """

    code: float
    ok: bool
    routes_attempted: list[str]
    source: None | RoomInfoFetchApiRoute
    data: StableTikTokLiveUser
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        ok = self.ok

        routes_attempted = self.routes_attempted

        source: None | str
        if isinstance(self.source, RoomInfoFetchApiRoute):
            source = self.source.value
        else:
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
        from ..models.stable_tik_tok_live_user import StableTikTokLiveUser

        d = dict(src_dict)
        code = d.pop("code")

        ok = d.pop("ok")

        routes_attempted = cast(list[str], d.pop("routes_attempted"))

        def _parse_source(data: object) -> None | RoomInfoFetchApiRoute:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_type_1 = RoomInfoFetchApiRoute(data)

                return source_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RoomInfoFetchApiRoute, data)

        source = _parse_source(d.pop("source"))

        data = StableTikTokLiveUser.from_dict(d.pop("data"))

        message = d.pop("message", UNSET)

        webcast_room_info_route_response = cls(
            code=code,
            ok=ok,
            routes_attempted=routes_attempted,
            source=source,
            data=data,
            message=message,
        )

        webcast_room_info_route_response.additional_properties = d
        return webcast_room_info_route_response

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

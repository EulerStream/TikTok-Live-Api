from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_room_admin_update_response_data import WebcastRoomAdminUpdateResponseData
    from ..models.webcast_room_admin_update_response_extra import WebcastRoomAdminUpdateResponseExtra


T = TypeVar("T", bound="WebcastRoomAdminUpdateResponse")


@_attrs_define
class WebcastRoomAdminUpdateResponse:
    """
    Attributes:
        data (WebcastRoomAdminUpdateResponseData):
        extra (WebcastRoomAdminUpdateResponseExtra):
        status_code (float):
    """

    data: WebcastRoomAdminUpdateResponseData
    extra: WebcastRoomAdminUpdateResponseExtra
    status_code: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        extra = self.extra.to_dict()

        status_code = self.status_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "extra": extra,
                "status_code": status_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_room_admin_update_response_data import WebcastRoomAdminUpdateResponseData
        from ..models.webcast_room_admin_update_response_extra import WebcastRoomAdminUpdateResponseExtra

        d = dict(src_dict)
        data = WebcastRoomAdminUpdateResponseData.from_dict(d.pop("data"))

        extra = WebcastRoomAdminUpdateResponseExtra.from_dict(d.pop("extra"))

        status_code = d.pop("status_code")

        webcast_room_admin_update_response = cls(
            data=data,
            extra=extra,
            status_code=status_code,
        )

        webcast_room_admin_update_response.additional_properties = d
        return webcast_room_admin_update_response

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

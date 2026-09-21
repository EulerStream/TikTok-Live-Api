from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_room_admin_list_response_admin import WebcastRoomAdminListResponseAdmin
    from ..models.webcast_room_admin_list_response_extra import WebcastRoomAdminListResponseExtra


T = TypeVar("T", bound="WebcastRoomAdminListResponse")


@_attrs_define
class WebcastRoomAdminListResponse:
    """
    Attributes:
        data (list[WebcastRoomAdminListResponseAdmin]):
        extra (WebcastRoomAdminListResponseExtra):
        status_code (float):
    """

    data: list[WebcastRoomAdminListResponseAdmin]
    extra: WebcastRoomAdminListResponseExtra
    status_code: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

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
        from ..models.webcast_room_admin_list_response_admin import WebcastRoomAdminListResponseAdmin
        from ..models.webcast_room_admin_list_response_extra import WebcastRoomAdminListResponseExtra

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = WebcastRoomAdminListResponseAdmin.from_dict(data_item_data)

            data.append(data_item)

        extra = WebcastRoomAdminListResponseExtra.from_dict(d.pop("extra"))

        status_code = d.pop("status_code")

        webcast_room_admin_list_response = cls(
            data=data,
            extra=extra,
            status_code=status_code,
        )

        webcast_room_admin_list_response.additional_properties = d
        return webcast_room_admin_list_response

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

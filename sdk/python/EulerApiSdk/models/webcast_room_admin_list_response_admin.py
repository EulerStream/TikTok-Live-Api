from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_room_admin_list_response_admin_admin_permissions import (
        WebcastRoomAdminListResponseAdminAdminPermissions,
    )
    from ..models.webcast_room_admin_list_response_image import WebcastRoomAdminListResponseImage


T = TypeVar("T", bound="WebcastRoomAdminListResponseAdmin")


@_attrs_define
class WebcastRoomAdminListResponseAdmin:
    """
    Attributes:
        admin_permissions (WebcastRoomAdminListResponseAdminAdminPermissions):
        avatar_large (WebcastRoomAdminListResponseImage):
        avatar_thumb (WebcastRoomAdminListResponseImage):
        display_id (str):
        id (float):
        id_str (str):
        nickname (str):
        sec_uid (str):
    """

    admin_permissions: WebcastRoomAdminListResponseAdminAdminPermissions
    avatar_large: WebcastRoomAdminListResponseImage
    avatar_thumb: WebcastRoomAdminListResponseImage
    display_id: str
    id: float
    id_str: str
    nickname: str
    sec_uid: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin_permissions = self.admin_permissions.to_dict()

        avatar_large = self.avatar_large.to_dict()

        avatar_thumb = self.avatar_thumb.to_dict()

        display_id = self.display_id

        id = self.id

        id_str = self.id_str

        nickname = self.nickname

        sec_uid = self.sec_uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "admin_permissions": admin_permissions,
                "avatar_large": avatar_large,
                "avatar_thumb": avatar_thumb,
                "display_id": display_id,
                "id": id,
                "id_str": id_str,
                "nickname": nickname,
                "sec_uid": sec_uid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_room_admin_list_response_admin_admin_permissions import (
            WebcastRoomAdminListResponseAdminAdminPermissions,  # noqa: PLC0415
        )
        from ..models.webcast_room_admin_list_response_image import WebcastRoomAdminListResponseImage  # noqa: PLC0415

        d = dict(src_dict)
        admin_permissions = WebcastRoomAdminListResponseAdminAdminPermissions.from_dict(d.pop("admin_permissions"))

        avatar_large = WebcastRoomAdminListResponseImage.from_dict(d.pop("avatar_large"))

        avatar_thumb = WebcastRoomAdminListResponseImage.from_dict(d.pop("avatar_thumb"))

        display_id = d.pop("display_id")

        id = d.pop("id")

        id_str = d.pop("id_str")

        nickname = d.pop("nickname")

        sec_uid = d.pop("sec_uid")

        webcast_room_admin_list_response_admin = cls(
            admin_permissions=admin_permissions,
            avatar_large=avatar_large,
            avatar_thumb=avatar_thumb,
            display_id=display_id,
            id=id,
            id_str=id_str,
            nickname=nickname,
            sec_uid=sec_uid,
        )

        webcast_room_admin_list_response_admin.additional_properties = d
        return webcast_room_admin_list_response_admin

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

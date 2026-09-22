from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_room_muted_users_response_user_attr_admin_permissions import (
        WebcastRoomMutedUsersResponseUserAttrAdminPermissions,
    )


T = TypeVar("T", bound="WebcastRoomMutedUsersResponseUserAttr")


@_attrs_define
class WebcastRoomMutedUsersResponseUserAttr:
    """
    Attributes:
        admin_permissions (WebcastRoomMutedUsersResponseUserAttrAdminPermissions):
        has_voting_function (bool):
        is_admin (bool):
        is_channel_admin (bool):
        is_muted (bool):
        is_super_admin (bool):
        mute_duration (float):
    """

    admin_permissions: WebcastRoomMutedUsersResponseUserAttrAdminPermissions
    has_voting_function: bool
    is_admin: bool
    is_channel_admin: bool
    is_muted: bool
    is_super_admin: bool
    mute_duration: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin_permissions = self.admin_permissions.to_dict()

        has_voting_function = self.has_voting_function

        is_admin = self.is_admin

        is_channel_admin = self.is_channel_admin

        is_muted = self.is_muted

        is_super_admin = self.is_super_admin

        mute_duration = self.mute_duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "admin_permissions": admin_permissions,
                "has_voting_function": has_voting_function,
                "is_admin": is_admin,
                "is_channel_admin": is_channel_admin,
                "is_muted": is_muted,
                "is_super_admin": is_super_admin,
                "mute_duration": mute_duration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_room_muted_users_response_user_attr_admin_permissions import (
            WebcastRoomMutedUsersResponseUserAttrAdminPermissions,  # noqa: PLC0415
        )

        d = dict(src_dict)
        admin_permissions = WebcastRoomMutedUsersResponseUserAttrAdminPermissions.from_dict(d.pop("admin_permissions"))

        has_voting_function = d.pop("has_voting_function")

        is_admin = d.pop("is_admin")

        is_channel_admin = d.pop("is_channel_admin")

        is_muted = d.pop("is_muted")

        is_super_admin = d.pop("is_super_admin")

        mute_duration = d.pop("mute_duration")

        webcast_room_muted_users_response_user_attr = cls(
            admin_permissions=admin_permissions,
            has_voting_function=has_voting_function,
            is_admin=is_admin,
            is_channel_admin=is_channel_admin,
            is_muted=is_muted,
            is_super_admin=is_super_admin,
            mute_duration=mute_duration,
        )

        webcast_room_muted_users_response_user_attr.additional_properties = d
        return webcast_room_muted_users_response_user_attr

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

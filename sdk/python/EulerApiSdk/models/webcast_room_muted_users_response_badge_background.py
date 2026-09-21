from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_room_muted_users_response_image import WebcastRoomMutedUsersResponseImage


T = TypeVar("T", bound="WebcastRoomMutedUsersResponseBadgeBackground")


@_attrs_define
class WebcastRoomMutedUsersResponseBadgeBackground:
    """
    Attributes:
        background_color_code (str):
        border_color_code (str):
        image (WebcastRoomMutedUsersResponseImage):
        left_side_image (WebcastRoomMutedUsersResponseImage):
    """

    background_color_code: str
    border_color_code: str
    image: WebcastRoomMutedUsersResponseImage
    left_side_image: WebcastRoomMutedUsersResponseImage
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        background_color_code = self.background_color_code

        border_color_code = self.border_color_code

        image = self.image.to_dict()

        left_side_image = self.left_side_image.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "background_color_code": background_color_code,
                "border_color_code": border_color_code,
                "image": image,
                "left_side_image": left_side_image,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_room_muted_users_response_image import WebcastRoomMutedUsersResponseImage

        d = dict(src_dict)
        background_color_code = d.pop("background_color_code")

        border_color_code = d.pop("border_color_code")

        image = WebcastRoomMutedUsersResponseImage.from_dict(d.pop("image"))

        left_side_image = WebcastRoomMutedUsersResponseImage.from_dict(d.pop("left_side_image"))

        webcast_room_muted_users_response_badge_background = cls(
            background_color_code=background_color_code,
            border_color_code=border_color_code,
            image=image,
            left_side_image=left_side_image,
        )

        webcast_room_muted_users_response_badge_background.additional_properties = d
        return webcast_room_muted_users_response_badge_background

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

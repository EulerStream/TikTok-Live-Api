from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastRoomMutedUsersResponseImage")


@_attrs_define
class WebcastRoomMutedUsersResponseImage:
    """
    Attributes:
        avg_color (str):
        height (float):
        image_type (float):
        is_animated (bool):
        open_web_url (str):
        uri (str):
        url_list (list[str]):
        width (float):
    """

    avg_color: str
    height: float
    image_type: float
    is_animated: bool
    open_web_url: str
    uri: str
    url_list: list[str]
    width: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_color = self.avg_color

        height = self.height

        image_type = self.image_type

        is_animated = self.is_animated

        open_web_url = self.open_web_url

        uri = self.uri

        url_list = self.url_list

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avg_color": avg_color,
                "height": height,
                "image_type": image_type,
                "is_animated": is_animated,
                "open_web_url": open_web_url,
                "uri": uri,
                "url_list": url_list,
                "width": width,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg_color = d.pop("avg_color")

        height = d.pop("height")

        image_type = d.pop("image_type")

        is_animated = d.pop("is_animated")

        open_web_url = d.pop("open_web_url")

        uri = d.pop("uri")

        url_list = cast(list[str], d.pop("url_list"))

        width = d.pop("width")

        webcast_room_muted_users_response_image = cls(
            avg_color=avg_color,
            height=height,
            image_type=image_type,
            is_animated=is_animated,
            open_web_url=open_web_url,
            uri=uri,
            url_list=url_list,
            width=width,
        )

        webcast_room_muted_users_response_image.additional_properties = d
        return webcast_room_muted_users_response_image

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

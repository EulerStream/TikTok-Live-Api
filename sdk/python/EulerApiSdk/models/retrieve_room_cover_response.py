from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetrieveRoomCoverResponse")


@_attrs_define
class RetrieveRoomCoverResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        cover_url (str | Unset):
    """

    code: float
    message: str | Unset = UNSET
    cover_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        cover_url = self.cover_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        cover_url = d.pop("cover_url", UNSET)

        retrieve_room_cover_response = cls(
            code=code,
            message=message,
            cover_url=cover_url,
        )

        retrieve_room_cover_response.additional_properties = d
        return retrieve_room_cover_response

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserHistoryResponseUser")


@_attrs_define
class UserHistoryResponseUser:
    """
    Attributes:
        avatar_url (str):
        nickname (str):
        unique_id (str):
        numeric_id (str):
    """

    avatar_url: str
    nickname: str
    unique_id: str
    numeric_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar_url = self.avatar_url

        nickname = self.nickname

        unique_id = self.unique_id

        numeric_id = self.numeric_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avatar_url": avatar_url,
                "nickname": nickname,
                "unique_id": unique_id,
                "numeric_id": numeric_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar_url = d.pop("avatar_url")

        nickname = d.pop("nickname")

        unique_id = d.pop("unique_id")

        numeric_id = d.pop("numeric_id")

        user_history_response_user = cls(
            avatar_url=avatar_url,
            nickname=nickname,
            unique_id=unique_id,
            numeric_id=numeric_id,
        )

        user_history_response_user.additional_properties = d
        return user_history_response_user

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

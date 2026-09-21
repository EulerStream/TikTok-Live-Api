from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TikTokUserBasicUser")


@_attrs_define
class TikTokUserBasicUser:
    """
    Attributes:
        avatar_larger (list[str]):
        avatar_medium (list[str]):
        avatar_thumb (list[str]):
        nickname (str):
        region (str):
        unique_id (str):
    """

    avatar_larger: list[str]
    avatar_medium: list[str]
    avatar_thumb: list[str]
    nickname: str
    region: str
    unique_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar_larger = self.avatar_larger

        avatar_medium = self.avatar_medium

        avatar_thumb = self.avatar_thumb

        nickname = self.nickname

        region = self.region

        unique_id = self.unique_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avatar_larger": avatar_larger,
                "avatar_medium": avatar_medium,
                "avatar_thumb": avatar_thumb,
                "nickname": nickname,
                "region": region,
                "unique_id": unique_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar_larger = cast(list[str], d.pop("avatar_larger"))

        avatar_medium = cast(list[str], d.pop("avatar_medium"))

        avatar_thumb = cast(list[str], d.pop("avatar_thumb"))

        nickname = d.pop("nickname")

        region = d.pop("region")

        unique_id = d.pop("unique_id")

        tik_tok_user_basic_user = cls(
            avatar_larger=avatar_larger,
            avatar_medium=avatar_medium,
            avatar_thumb=avatar_thumb,
            nickname=nickname,
            region=region,
            unique_id=unique_id,
        )

        tik_tok_user_basic_user.additional_properties = d
        return tik_tok_user_basic_user

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TikTokUserInfoByIdFollowInfo")


@_attrs_define
class TikTokUserInfoByIdFollowInfo:
    """
    Attributes:
        follower_count (float):
        following_count (float):
        follow_status (float):
    """

    follower_count: float
    following_count: float
    follow_status: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        follower_count = self.follower_count

        following_count = self.following_count

        follow_status = self.follow_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "follower_count": follower_count,
                "following_count": following_count,
                "follow_status": follow_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        follower_count = d.pop("follower_count")

        following_count = d.pop("following_count")

        follow_status = d.pop("follow_status")

        tik_tok_user_info_by_id_follow_info = cls(
            follower_count=follower_count,
            following_count=following_count,
            follow_status=follow_status,
        )

        tik_tok_user_info_by_id_follow_info.additional_properties = d
        return tik_tok_user_info_by_id_follow_info

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

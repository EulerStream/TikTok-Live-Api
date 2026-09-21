from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LeaderboardRowUser")


@_attrs_define
class LeaderboardRowUser:
    """
    Attributes:
        numeric_id (str):
        unique_id (str):
        nickname (str):
        avatar_url (str):
        follower_count (float):
        following_count (float):
        region (str):
    """

    numeric_id: str
    unique_id: str
    nickname: str
    avatar_url: str
    follower_count: float
    following_count: float
    region: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        numeric_id = self.numeric_id

        unique_id = self.unique_id

        nickname = self.nickname

        avatar_url = self.avatar_url

        follower_count = self.follower_count

        following_count = self.following_count

        region = self.region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "numeric_id": numeric_id,
                "unique_id": unique_id,
                "nickname": nickname,
                "avatar_url": avatar_url,
                "follower_count": follower_count,
                "following_count": following_count,
                "region": region,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        numeric_id = d.pop("numeric_id")

        unique_id = d.pop("unique_id")

        nickname = d.pop("nickname")

        avatar_url = d.pop("avatar_url")

        follower_count = d.pop("follower_count")

        following_count = d.pop("following_count")

        region = d.pop("region")

        leaderboard_row_user = cls(
            numeric_id=numeric_id,
            unique_id=unique_id,
            nickname=nickname,
            avatar_url=avatar_url,
            follower_count=follower_count,
            following_count=following_count,
            region=region,
        )

        leaderboard_row_user.additional_properties = d
        return leaderboard_row_user

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

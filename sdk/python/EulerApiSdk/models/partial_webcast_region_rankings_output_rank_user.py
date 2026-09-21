from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PartialWebcastRegionRankingsOutputRankUser")


@_attrs_define
class PartialWebcastRegionRankingsOutputRankUser:
    """
    Attributes:
        following_count (float):
        follower_count (float):
        nickname (str):
        numeric_id (str):
        unique_id (str):
        avatar_thumb (list[str]):
    """

    following_count: float
    follower_count: float
    nickname: str
    numeric_id: str
    unique_id: str
    avatar_thumb: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        following_count = self.following_count

        follower_count = self.follower_count

        nickname = self.nickname

        numeric_id = self.numeric_id

        unique_id = self.unique_id

        avatar_thumb = self.avatar_thumb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "following_count": following_count,
                "follower_count": follower_count,
                "nickname": nickname,
                "numeric_id": numeric_id,
                "unique_id": unique_id,
                "avatar_thumb": avatar_thumb,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        following_count = d.pop("following_count")

        follower_count = d.pop("follower_count")

        nickname = d.pop("nickname")

        numeric_id = d.pop("numeric_id")

        unique_id = d.pop("unique_id")

        avatar_thumb = cast(list[str], d.pop("avatar_thumb"))

        partial_webcast_region_rankings_output_rank_user = cls(
            following_count=following_count,
            follower_count=follower_count,
            nickname=nickname,
            numeric_id=numeric_id,
            unique_id=unique_id,
            avatar_thumb=avatar_thumb,
        )

        partial_webcast_region_rankings_output_rank_user.additional_properties = d
        return partial_webcast_region_rankings_output_rank_user

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

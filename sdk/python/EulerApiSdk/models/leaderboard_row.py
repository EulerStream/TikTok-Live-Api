from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.leaderboard_row_user import LeaderboardRowUser


T = TypeVar("T", bound="LeaderboardRow")


@_attrs_define
class LeaderboardRow:
    """
    Attributes:
        rank (float):
        score (float):
        score_description (str):
        user (LeaderboardRowUser):
    """

    rank: float
    score: float
    score_description: str
    user: LeaderboardRowUser
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rank = self.rank

        score = self.score

        score_description = self.score_description

        user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rank": rank,
                "score": score,
                "score_description": score_description,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.leaderboard_row_user import LeaderboardRowUser

        d = dict(src_dict)
        rank = d.pop("rank")

        score = d.pop("score")

        score_description = d.pop("score_description")

        user = LeaderboardRowUser.from_dict(d.pop("user"))

        leaderboard_row = cls(
            rank=rank,
            score=score,
            score_description=score_description,
            user=user,
        )

        leaderboard_row.additional_properties = d
        return leaderboard_row

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

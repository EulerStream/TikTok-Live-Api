from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.leaderboard_row_user import LeaderboardRowUser


T = TypeVar("T", bound="SearchUserResult")


@_attrs_define
class SearchUserResult:
    """
    Attributes:
        user (LeaderboardRowUser):
        last_seen (str):
    """

    user: LeaderboardRowUser
    last_seen: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user.to_dict()

        last_seen = self.last_seen

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "last_seen": last_seen,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.leaderboard_row_user import LeaderboardRowUser  # noqa: PLC0415

        d = dict(src_dict)
        user = LeaderboardRowUser.from_dict(d.pop("user"))

        last_seen = d.pop("last_seen")

        search_user_result = cls(
            user=user,
            last_seen=last_seen,
        )

        search_user_result.additional_properties = d
        return search_user_result

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

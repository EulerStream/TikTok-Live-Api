from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_leaderboards_response_leaderboards import UserLeaderboardsResponseLeaderboards


T = TypeVar("T", bound="UserLeaderboardsResponse")


@_attrs_define
class UserLeaderboardsResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        user_numeric_id (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        leaderboards (UserLeaderboardsResponseLeaderboards | Unset): region -> rank_names the creator appeared on (e.g.
            "DAILY_RANK", "SALE_RANK").
    """

    code: float
    message: str | Unset = UNSET
    user_numeric_id: str | Unset = UNSET
    from_: str | Unset = UNSET
    to: str | Unset = UNSET
    leaderboards: UserLeaderboardsResponseLeaderboards | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        user_numeric_id = self.user_numeric_id

        from_ = self.from_

        to = self.to

        leaderboards: dict[str, Any] | Unset = UNSET
        if not isinstance(self.leaderboards, Unset):
            leaderboards = self.leaderboards.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if user_numeric_id is not UNSET:
            field_dict["user_numeric_id"] = user_numeric_id
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if leaderboards is not UNSET:
            field_dict["leaderboards"] = leaderboards

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_leaderboards_response_leaderboards import UserLeaderboardsResponseLeaderboards

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        user_numeric_id = d.pop("user_numeric_id", UNSET)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        _leaderboards = d.pop("leaderboards", UNSET)
        leaderboards: UserLeaderboardsResponseLeaderboards | Unset
        if isinstance(_leaderboards, Unset):
            leaderboards = UNSET
        else:
            leaderboards = UserLeaderboardsResponseLeaderboards.from_dict(_leaderboards)

        user_leaderboards_response = cls(
            code=code,
            message=message,
            user_numeric_id=user_numeric_id,
            from_=from_,
            to=to,
            leaderboards=leaderboards,
        )

        user_leaderboards_response.additional_properties = d
        return user_leaderboards_response

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.available_webcast_rank_name import AvailableWebcastRankName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_history_point import UserHistoryPoint
    from ..models.user_history_response_user import UserHistoryResponseUser


T = TypeVar("T", bound="UserHistoryResponse")


@_attrs_define
class UserHistoryResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        user (UserHistoryResponseUser | Unset):
        region (str | Unset):
        rank_name (AvailableWebcastRankName | Unset):
        history (list[UserHistoryPoint] | Unset):
    """

    code: float
    message: str | Unset = UNSET
    user: UserHistoryResponseUser | Unset = UNSET
    region: str | Unset = UNSET
    rank_name: AvailableWebcastRankName | Unset = UNSET
    history: list[UserHistoryPoint] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        region = self.region

        rank_name: str | Unset = UNSET
        if not isinstance(self.rank_name, Unset):
            rank_name = self.rank_name.value

        history: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.history, Unset):
            history = []
            for history_item_data in self.history:
                history_item = history_item_data.to_dict()
                history.append(history_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if user is not UNSET:
            field_dict["user"] = user
        if region is not UNSET:
            field_dict["region"] = region
        if rank_name is not UNSET:
            field_dict["rank_name"] = rank_name
        if history is not UNSET:
            field_dict["history"] = history

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_history_point import UserHistoryPoint
        from ..models.user_history_response_user import UserHistoryResponseUser

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _user = d.pop("user", UNSET)
        user: UserHistoryResponseUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserHistoryResponseUser.from_dict(_user)

        region = d.pop("region", UNSET)

        _rank_name = d.pop("rank_name", UNSET)
        rank_name: AvailableWebcastRankName | Unset
        if isinstance(_rank_name, Unset):
            rank_name = UNSET
        else:
            rank_name = AvailableWebcastRankName(_rank_name)

        _history = d.pop("history", UNSET)
        history: list[UserHistoryPoint] | Unset = UNSET
        if _history is not UNSET:
            history = []
            for history_item_data in _history:
                history_item = UserHistoryPoint.from_dict(history_item_data)

                history.append(history_item)

        user_history_response = cls(
            code=code,
            message=message,
            user=user,
            region=region,
            rank_name=rank_name,
            history=history,
        )

        user_history_response.additional_properties = d
        return user_history_response

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partial_webcast_region_rankings_output_rank_user import PartialWebcastRegionRankingsOutputRankUser


T = TypeVar("T", bound="PartialWebcastRegionRankingsOutputRank")


@_attrs_define
class PartialWebcastRegionRankingsOutputRank:
    """
    Attributes:
        rank (float | Unset):
        diamonds (float | Unset):
        diamonds_description (str | Unset):
        room_id (str | Unset):
        user (PartialWebcastRegionRankingsOutputRankUser | Unset):
    """

    rank: float | Unset = UNSET
    diamonds: float | Unset = UNSET
    diamonds_description: str | Unset = UNSET
    room_id: str | Unset = UNSET
    user: PartialWebcastRegionRankingsOutputRankUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rank = self.rank

        diamonds = self.diamonds

        diamonds_description = self.diamonds_description

        room_id = self.room_id

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rank is not UNSET:
            field_dict["rank"] = rank
        if diamonds is not UNSET:
            field_dict["diamonds"] = diamonds
        if diamonds_description is not UNSET:
            field_dict["diamonds_description"] = diamonds_description
        if room_id is not UNSET:
            field_dict["room_id"] = room_id
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partial_webcast_region_rankings_output_rank_user import PartialWebcastRegionRankingsOutputRankUser

        d = dict(src_dict)
        rank = d.pop("rank", UNSET)

        diamonds = d.pop("diamonds", UNSET)

        diamonds_description = d.pop("diamonds_description", UNSET)

        room_id = d.pop("room_id", UNSET)

        _user = d.pop("user", UNSET)
        user: PartialWebcastRegionRankingsOutputRankUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = PartialWebcastRegionRankingsOutputRankUser.from_dict(_user)

        partial_webcast_region_rankings_output_rank = cls(
            rank=rank,
            diamonds=diamonds,
            diamonds_description=diamonds_description,
            room_id=room_id,
            user=user,
        )

        partial_webcast_region_rankings_output_rank.additional_properties = d
        return partial_webcast_region_rankings_output_rank

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

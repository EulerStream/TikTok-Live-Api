from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.region_overview_leagues_item import RegionOverviewLeaguesItem
from ..models.region_overview_rankings_item import RegionOverviewRankingsItem

T = TypeVar("T", bound="RegionOverview")


@_attrs_define
class RegionOverview:
    """
    Attributes:
        rankings (list[RegionOverviewRankingsItem]):
        leagues (list[RegionOverviewLeaguesItem]):
    """

    rankings: list[RegionOverviewRankingsItem]
    leagues: list[RegionOverviewLeaguesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rankings = []
        for rankings_item_data in self.rankings:
            rankings_item = rankings_item_data.value
            rankings.append(rankings_item)

        leagues = []
        for leagues_item_data in self.leagues:
            leagues_item = leagues_item_data.value
            leagues.append(leagues_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rankings": rankings,
                "leagues": leagues,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rankings = []
        _rankings = d.pop("rankings")
        for rankings_item_data in _rankings:
            rankings_item = RegionOverviewRankingsItem(rankings_item_data)

            rankings.append(rankings_item)

        leagues = []
        _leagues = d.pop("leagues")
        for leagues_item_data in _leagues:
            leagues_item = RegionOverviewLeaguesItem(leagues_item_data)

            leagues.append(leagues_item)

        region_overview = cls(
            rankings=rankings,
            leagues=leagues,
        )

        region_overview.additional_properties = d
        return region_overview

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

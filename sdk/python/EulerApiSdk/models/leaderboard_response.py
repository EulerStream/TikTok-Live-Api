from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.available_webcast_rank_name import AvailableWebcastRankName
from ..models.ranking_league_name import RankingLeagueName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.leaderboard_row import LeaderboardRow


T = TypeVar("T", bound="LeaderboardResponse")


@_attrs_define
class LeaderboardResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        ts (str | Unset):
        date (str | Unset):
        region (str | Unset):
        rank_name (AvailableWebcastRankName | Unset):
        league (RankingLeagueName | Unset):
        resets_at (None | str | Unset):
        is_latest (bool | Unset):
        ranks (list[LeaderboardRow] | Unset):
    """

    code: float
    message: str | Unset = UNSET
    ts: str | Unset = UNSET
    date: str | Unset = UNSET
    region: str | Unset = UNSET
    rank_name: AvailableWebcastRankName | Unset = UNSET
    league: RankingLeagueName | Unset = UNSET
    resets_at: None | str | Unset = UNSET
    is_latest: bool | Unset = UNSET
    ranks: list[LeaderboardRow] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        ts = self.ts

        date = self.date

        region = self.region

        rank_name: str | Unset = UNSET
        if not isinstance(self.rank_name, Unset):
            rank_name = self.rank_name.value

        league: str | Unset = UNSET
        if not isinstance(self.league, Unset):
            league = self.league.value

        resets_at: None | str | Unset
        if isinstance(self.resets_at, Unset):
            resets_at = UNSET
        else:
            resets_at = self.resets_at

        is_latest = self.is_latest

        ranks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ranks, Unset):
            ranks = []
            for ranks_item_data in self.ranks:
                ranks_item = ranks_item_data.to_dict()
                ranks.append(ranks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if ts is not UNSET:
            field_dict["ts"] = ts
        if date is not UNSET:
            field_dict["date"] = date
        if region is not UNSET:
            field_dict["region"] = region
        if rank_name is not UNSET:
            field_dict["rank_name"] = rank_name
        if league is not UNSET:
            field_dict["league"] = league
        if resets_at is not UNSET:
            field_dict["resets_at"] = resets_at
        if is_latest is not UNSET:
            field_dict["is_latest"] = is_latest
        if ranks is not UNSET:
            field_dict["ranks"] = ranks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.leaderboard_row import LeaderboardRow

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        ts = d.pop("ts", UNSET)

        date = d.pop("date", UNSET)

        region = d.pop("region", UNSET)

        _rank_name = d.pop("rank_name", UNSET)
        rank_name: AvailableWebcastRankName | Unset
        if isinstance(_rank_name, Unset):
            rank_name = UNSET
        else:
            rank_name = AvailableWebcastRankName(_rank_name)

        _league = d.pop("league", UNSET)
        league: RankingLeagueName | Unset
        if isinstance(_league, Unset):
            league = UNSET
        else:
            league = RankingLeagueName(_league)

        def _parse_resets_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resets_at = _parse_resets_at(d.pop("resets_at", UNSET))

        is_latest = d.pop("is_latest", UNSET)

        _ranks = d.pop("ranks", UNSET)
        ranks: list[LeaderboardRow] | Unset = UNSET
        if _ranks is not UNSET:
            ranks = []
            for ranks_item_data in _ranks:
                ranks_item = LeaderboardRow.from_dict(ranks_item_data)

                ranks.append(ranks_item)

        leaderboard_response = cls(
            code=code,
            message=message,
            ts=ts,
            date=date,
            region=region,
            rank_name=rank_name,
            league=league,
            resets_at=resets_at,
            is_latest=is_latest,
            ranks=ranks,
        )

        leaderboard_response.additional_properties = d
        return leaderboard_response

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

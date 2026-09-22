from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.partial_webcast_region_rankings_output_rank import PartialWebcastRegionRankingsOutputRank


T = TypeVar("T", bound="WebcastRegionRankingsOutput")


@_attrs_define
class WebcastRegionRankingsOutput:
    """
    Attributes:
        attempts (float):
        ranks (list[PartialWebcastRegionRankingsOutputRank]):
        rank_title (None | str):
        rank_type (None | str):
        resets_at (datetime.datetime | None):
        resets_in (float | None):
    """

    attempts: float
    ranks: list[PartialWebcastRegionRankingsOutputRank]
    rank_title: None | str
    rank_type: None | str
    resets_at: datetime.datetime | None
    resets_in: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attempts = self.attempts

        ranks = []
        for ranks_item_data in self.ranks:
            ranks_item = ranks_item_data.to_dict()
            ranks.append(ranks_item)

        rank_title: None | str
        rank_title = self.rank_title

        rank_type: None | str
        rank_type = self.rank_type

        resets_at: None | str
        if isinstance(self.resets_at, datetime.datetime):
            resets_at = self.resets_at.isoformat()
        else:
            resets_at = self.resets_at

        resets_in: float | None
        resets_in = self.resets_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attempts": attempts,
                "ranks": ranks,
                "rank_title": rank_title,
                "rank_type": rank_type,
                "resets_at": resets_at,
                "resets_in": resets_in,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partial_webcast_region_rankings_output_rank import (
            PartialWebcastRegionRankingsOutputRank,  # noqa: PLC0415
        )

        d = dict(src_dict)
        attempts = d.pop("attempts")

        ranks = []
        _ranks = d.pop("ranks")
        for ranks_item_data in _ranks:
            ranks_item = PartialWebcastRegionRankingsOutputRank.from_dict(ranks_item_data)

            ranks.append(ranks_item)

        def _parse_rank_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rank_title = _parse_rank_title(d.pop("rank_title"))

        def _parse_rank_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rank_type = _parse_rank_type(d.pop("rank_type"))

        def _parse_resets_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resets_at_type_0 = datetime.datetime.fromisoformat(data)

                return resets_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        resets_at = _parse_resets_at(d.pop("resets_at"))

        def _parse_resets_in(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        resets_in = _parse_resets_in(d.pop("resets_in"))

        webcast_region_rankings_output = cls(
            attempts=attempts,
            ranks=ranks,
            rank_title=rank_title,
            rank_type=rank_type,
            resets_at=resets_at,
            resets_in=resets_in,
        )

        webcast_region_rankings_output.additional_properties = d
        return webcast_region_rankings_output

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

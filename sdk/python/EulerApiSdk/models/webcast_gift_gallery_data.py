from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ranking_league_level import RankingLeagueLevel
from ..models.webcast_gift_gallery_data_anchor_ranking_league import WebcastGiftGalleryDataAnchorRankingLeague
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.normal_gift_item import NormalGiftItem
    from ..models.webcast_gift_gallery_data_current_user_progress import WebcastGiftGalleryDataCurrentUserProgress


T = TypeVar("T", bound="WebcastGiftGalleryData")


@_attrs_define
class WebcastGiftGalleryData:
    """Gallery entrance payload. Only the fields we model are typed; the rest of the (large) TikTok response rides through
    as `any`.

        Attributes:
            normal_gifts (list[NormalGiftItem]):
            current_timestamp (float):
            current_period_starts_at (float):
            current_period_ends_at (float):
            class_type (RankingLeagueLevel):
            anchor_ranking_league (WebcastGiftGalleryDataAnchorRankingLeague):
            current_user_progress (WebcastGiftGalleryDataCurrentUserProgress | Unset):
    """

    normal_gifts: list[NormalGiftItem]
    current_timestamp: float
    current_period_starts_at: float
    current_period_ends_at: float
    class_type: RankingLeagueLevel
    anchor_ranking_league: WebcastGiftGalleryDataAnchorRankingLeague
    current_user_progress: WebcastGiftGalleryDataCurrentUserProgress | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        normal_gifts = []
        for normal_gifts_item_data in self.normal_gifts:
            normal_gifts_item = normal_gifts_item_data.to_dict()
            normal_gifts.append(normal_gifts_item)

        current_timestamp = self.current_timestamp

        current_period_starts_at = self.current_period_starts_at

        current_period_ends_at = self.current_period_ends_at

        class_type = self.class_type.value

        anchor_ranking_league = self.anchor_ranking_league.value

        current_user_progress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current_user_progress, Unset):
            current_user_progress = self.current_user_progress.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "normal_gifts": normal_gifts,
                "current_timestamp": current_timestamp,
                "current_period_starts_at": current_period_starts_at,
                "current_period_ends_at": current_period_ends_at,
                "class_type": class_type,
                "anchor_ranking_league": anchor_ranking_league,
            }
        )
        if current_user_progress is not UNSET:
            field_dict["current_user_progress"] = current_user_progress

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.normal_gift_item import NormalGiftItem
        from ..models.webcast_gift_gallery_data_current_user_progress import WebcastGiftGalleryDataCurrentUserProgress

        d = dict(src_dict)
        normal_gifts = []
        _normal_gifts = d.pop("normal_gifts")
        for normal_gifts_item_data in _normal_gifts:
            normal_gifts_item = NormalGiftItem.from_dict(normal_gifts_item_data)

            normal_gifts.append(normal_gifts_item)

        current_timestamp = d.pop("current_timestamp")

        current_period_starts_at = d.pop("current_period_starts_at")

        current_period_ends_at = d.pop("current_period_ends_at")

        class_type = RankingLeagueLevel(d.pop("class_type"))

        anchor_ranking_league = WebcastGiftGalleryDataAnchorRankingLeague(d.pop("anchor_ranking_league"))

        _current_user_progress = d.pop("current_user_progress", UNSET)
        current_user_progress: WebcastGiftGalleryDataCurrentUserProgress | Unset
        if isinstance(_current_user_progress, Unset):
            current_user_progress = UNSET
        else:
            current_user_progress = WebcastGiftGalleryDataCurrentUserProgress.from_dict(_current_user_progress)

        webcast_gift_gallery_data = cls(
            normal_gifts=normal_gifts,
            current_timestamp=current_timestamp,
            current_period_starts_at=current_period_starts_at,
            current_period_ends_at=current_period_ends_at,
            class_type=class_type,
            anchor_ranking_league=anchor_ranking_league,
            current_user_progress=current_user_progress,
        )

        webcast_gift_gallery_data.additional_properties = d
        return webcast_gift_gallery_data

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

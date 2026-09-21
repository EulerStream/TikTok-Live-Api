from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.room_gifts_result_gift_overrides import RoomGiftsResultGiftOverrides
    from ..models.room_gifts_result_panel_refresh_data import RoomGiftsResultPanelRefreshData


T = TypeVar("T", bound="RoomGiftsResult")


@_attrs_define
class RoomGiftsResult:
    """
    Attributes:
        room_id (str):
        page_gifts (list[float]):
        gift_overrides (RoomGiftsResultGiftOverrides):
        panel_refresh_data (RoomGiftsResultPanelRefreshData | Unset):
    """

    room_id: str
    page_gifts: list[float]
    gift_overrides: RoomGiftsResultGiftOverrides
    panel_refresh_data: RoomGiftsResultPanelRefreshData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        room_id = self.room_id

        page_gifts = self.page_gifts

        gift_overrides = self.gift_overrides.to_dict()

        panel_refresh_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.panel_refresh_data, Unset):
            panel_refresh_data = self.panel_refresh_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "room_id": room_id,
                "page_gifts": page_gifts,
                "gift_overrides": gift_overrides,
            }
        )
        if panel_refresh_data is not UNSET:
            field_dict["panel_refresh_data"] = panel_refresh_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.room_gifts_result_gift_overrides import RoomGiftsResultGiftOverrides
        from ..models.room_gifts_result_panel_refresh_data import RoomGiftsResultPanelRefreshData

        d = dict(src_dict)
        room_id = d.pop("room_id")

        page_gifts = cast(list[float], d.pop("page_gifts"))

        gift_overrides = RoomGiftsResultGiftOverrides.from_dict(d.pop("gift_overrides"))

        _panel_refresh_data = d.pop("panel_refresh_data", UNSET)
        panel_refresh_data: RoomGiftsResultPanelRefreshData | Unset
        if isinstance(_panel_refresh_data, Unset):
            panel_refresh_data = UNSET
        else:
            panel_refresh_data = RoomGiftsResultPanelRefreshData.from_dict(_panel_refresh_data)

        room_gifts_result = cls(
            room_id=room_id,
            page_gifts=page_gifts,
            gift_overrides=gift_overrides,
            panel_refresh_data=panel_refresh_data,
        )

        room_gifts_result.additional_properties = d
        return room_gifts_result

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

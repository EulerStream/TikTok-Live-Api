from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_feed_response_item_flare_info import WebcastFeedResponseItemFlareInfo
    from ..models.webcast_feed_response_room_data import WebcastFeedResponseRoomData


T = TypeVar("T", bound="WebcastFeedResponseItem")


@_attrs_define
class WebcastFeedResponseItem:
    """
    Attributes:
        type_ (float):
        rid (str):
        data (WebcastFeedResponseRoomData):
        flare_info (WebcastFeedResponseItemFlareInfo):
        room_event_tracking (str):
    """

    type_: float
    rid: str
    data: WebcastFeedResponseRoomData
    flare_info: WebcastFeedResponseItemFlareInfo
    room_event_tracking: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        rid = self.rid

        data = self.data.to_dict()

        flare_info = self.flare_info.to_dict()

        room_event_tracking = self.room_event_tracking

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "rid": rid,
                "data": data,
                "flare_info": flare_info,
                "room_event_tracking": room_event_tracking,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_feed_response_item_flare_info import WebcastFeedResponseItemFlareInfo  # noqa: PLC0415
        from ..models.webcast_feed_response_room_data import WebcastFeedResponseRoomData  # noqa: PLC0415

        d = dict(src_dict)
        type_ = d.pop("type")

        rid = d.pop("rid")

        data = WebcastFeedResponseRoomData.from_dict(d.pop("data"))

        flare_info = WebcastFeedResponseItemFlareInfo.from_dict(d.pop("flare_info"))

        room_event_tracking = d.pop("room_event_tracking")

        webcast_feed_response_item = cls(
            type_=type_,
            rid=rid,
            data=data,
            flare_info=flare_info,
            room_event_tracking=room_event_tracking,
        )

        webcast_feed_response_item.additional_properties = d
        return webcast_feed_response_item

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

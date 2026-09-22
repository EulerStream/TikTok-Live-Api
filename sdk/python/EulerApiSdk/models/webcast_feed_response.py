from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_feed_response_extra import WebcastFeedResponseExtra
    from ..models.webcast_feed_response_item import WebcastFeedResponseItem


T = TypeVar("T", bound="WebcastFeedResponse")


@_attrs_define
class WebcastFeedResponse:
    """
    Attributes:
        status_code (float):
        extra (WebcastFeedResponseExtra):
        data (list[WebcastFeedResponseItem]):
    """

    status_code: float
    extra: WebcastFeedResponseExtra
    data: list[WebcastFeedResponseItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_code = self.status_code

        extra = self.extra.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status_code": status_code,
                "extra": extra,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_feed_response_extra import WebcastFeedResponseExtra  # noqa: PLC0415
        from ..models.webcast_feed_response_item import WebcastFeedResponseItem  # noqa: PLC0415

        d = dict(src_dict)
        status_code = d.pop("status_code")

        extra = WebcastFeedResponseExtra.from_dict(d.pop("extra"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = WebcastFeedResponseItem.from_dict(data_item_data)

            data.append(data_item)

        webcast_feed_response = cls(
            status_code=status_code,
            extra=extra,
            data=data,
        )

        webcast_feed_response.additional_properties = d
        return webcast_feed_response

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webcast_event_list_item import WebcastEventListItem


T = TypeVar("T", bound="RetrieveWebcastAnchorEventsResponse")


@_attrs_define
class RetrieveWebcastAnchorEventsResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        events (list[WebcastEventListItem] | Unset):
        has_more (bool | Unset):
        page (float | Unset):
    """

    code: float
    message: str | Unset = UNSET
    events: list[WebcastEventListItem] | Unset = UNSET
    has_more: bool | Unset = UNSET
    page: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        has_more = self.has_more

        page = self.page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if events is not UNSET:
            field_dict["events"] = events
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if page is not UNSET:
            field_dict["page"] = page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_event_list_item import WebcastEventListItem

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _events = d.pop("events", UNSET)
        events: list[WebcastEventListItem] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = WebcastEventListItem.from_dict(events_item_data)

                events.append(events_item)

        has_more = d.pop("has_more", UNSET)

        page = d.pop("page", UNSET)

        retrieve_webcast_anchor_events_response = cls(
            code=code,
            message=message,
            events=events,
            has_more=has_more,
            page=page,
        )

        retrieve_webcast_anchor_events_response.additional_properties = d
        return retrieve_webcast_anchor_events_response

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

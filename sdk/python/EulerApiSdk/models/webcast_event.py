from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_event_host import WebcastEventHost


T = TypeVar("T", bound="WebcastEvent")


@_attrs_define
class WebcastEvent:
    """
    Attributes:
        id (str):
        start_time (float):
        duration (float):
        title (str):
        desc (str):
        status (float):
        host (WebcastEventHost):
        subscriber_count (float):
        type_ (float):
        enable_update (bool):
        has_subscribed (bool):
        is_paid_event (bool):
        ticket_amount (float):
    """

    id: str
    start_time: float
    duration: float
    title: str
    desc: str
    status: float
    host: WebcastEventHost
    subscriber_count: float
    type_: float
    enable_update: bool
    has_subscribed: bool
    is_paid_event: bool
    ticket_amount: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        start_time = self.start_time

        duration = self.duration

        title = self.title

        desc = self.desc

        status = self.status

        host = self.host.to_dict()

        subscriber_count = self.subscriber_count

        type_ = self.type_

        enable_update = self.enable_update

        has_subscribed = self.has_subscribed

        is_paid_event = self.is_paid_event

        ticket_amount = self.ticket_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "start_time": start_time,
                "duration": duration,
                "title": title,
                "desc": desc,
                "status": status,
                "host": host,
                "subscriber_count": subscriber_count,
                "type": type_,
                "enable_update": enable_update,
                "has_subscribed": has_subscribed,
                "is_paid_event": is_paid_event,
                "ticket_amount": ticket_amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_event_host import WebcastEventHost  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        start_time = d.pop("start_time")

        duration = d.pop("duration")

        title = d.pop("title")

        desc = d.pop("desc")

        status = d.pop("status")

        host = WebcastEventHost.from_dict(d.pop("host"))

        subscriber_count = d.pop("subscriber_count")

        type_ = d.pop("type")

        enable_update = d.pop("enable_update")

        has_subscribed = d.pop("has_subscribed")

        is_paid_event = d.pop("is_paid_event")

        ticket_amount = d.pop("ticket_amount")

        webcast_event = cls(
            id=id,
            start_time=start_time,
            duration=duration,
            title=title,
            desc=desc,
            status=status,
            host=host,
            subscriber_count=subscriber_count,
            type_=type_,
            enable_update=enable_update,
            has_subscribed=has_subscribed,
            is_paid_event=is_paid_event,
            ticket_amount=ticket_amount,
        )

        webcast_event.additional_properties = d
        return webcast_event

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

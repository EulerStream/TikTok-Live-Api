from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webcast_event import WebcastEvent


T = TypeVar("T", bound="RetrieveWebcastEventResponse")


@_attrs_define
class RetrieveWebcastEventResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        event (WebcastEvent | Unset):
    """

    code: float
    message: str | Unset = UNSET
    event: WebcastEvent | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        event: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if event is not UNSET:
            field_dict["event"] = event

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_event import WebcastEvent

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _event = d.pop("event", UNSET)
        event: WebcastEvent | Unset
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = WebcastEvent.from_dict(_event)

        retrieve_webcast_event_response = cls(
            code=code,
            message=message,
            event=event,
        )

        retrieve_webcast_event_response.additional_properties = d
        return retrieve_webcast_event_response

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

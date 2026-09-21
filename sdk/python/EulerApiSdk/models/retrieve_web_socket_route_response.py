from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.web_socket_state import WebSocketState


T = TypeVar("T", bound="RetrieveWebSocketRouteResponse")


@_attrs_define
class RetrieveWebSocketRouteResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        state (WebSocketState | Unset):
    """

    code: float
    message: str | Unset = UNSET
    state: WebSocketState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.web_socket_state import WebSocketState

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _state = d.pop("state", UNSET)
        state: WebSocketState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = WebSocketState.from_dict(_state)

        retrieve_web_socket_route_response = cls(
            code=code,
            message=message,
            state=state,
        )

        retrieve_web_socket_route_response.additional_properties = d
        return retrieve_web_socket_route_response

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

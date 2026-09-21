from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.peer_presence import PeerPresence


T = TypeVar("T", bound="RetrieveAgentHostsResponse")


@_attrs_define
class RetrieveAgentHostsResponse:
    """
    Attributes:
        code (float):
        agents (list[PeerPresence]):
        message (str | Unset):
    """

    code: float
    agents: list[PeerPresence]
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        agents = []
        for agents_item_data in self.agents:
            agents_item = agents_item_data.to_dict()
            agents.append(agents_item)

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "agents": agents,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.peer_presence import PeerPresence

        d = dict(src_dict)
        code = d.pop("code")

        agents = []
        _agents = d.pop("agents")
        for agents_item_data in _agents:
            agents_item = PeerPresence.from_dict(agents_item_data)

            agents.append(agents_item)

        message = d.pop("message", UNSET)

        retrieve_agent_hosts_response = cls(
            code=code,
            agents=agents,
            message=message,
        )

        retrieve_agent_hosts_response.additional_properties = d
        return retrieve_agent_hosts_response

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

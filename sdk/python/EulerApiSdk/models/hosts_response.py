from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.peer_presence import PeerPresence


T = TypeVar("T", bound="HostsResponse")


@_attrs_define
class HostsResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        hosts (list[PeerPresence] | Unset):
    """

    code: float
    message: str | Unset = UNSET
    hosts: list[PeerPresence] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        hosts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hosts, Unset):
            hosts = []
            for hosts_item_data in self.hosts:
                hosts_item = hosts_item_data.to_dict()
                hosts.append(hosts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if hosts is not UNSET:
            field_dict["hosts"] = hosts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.peer_presence import PeerPresence  # noqa: PLC0415

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _hosts = d.pop("hosts", UNSET)
        hosts: list[PeerPresence] | Unset = UNSET
        if _hosts is not UNSET:
            hosts = []
            for hosts_item_data in _hosts:
                hosts_item = PeerPresence.from_dict(hosts_item_data)

                hosts.append(hosts_item)

        hosts_response = cls(
            code=code,
            message=message,
            hosts=hosts,
        )

        hosts_response.additional_properties = d
        return hosts_response

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

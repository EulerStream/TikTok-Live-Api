from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accounts_table_request_limits import AccountsTableRequestLimits
    from ..models.jwt_configuration_web_socket_data import JWTConfigurationWebSocketData


T = TypeVar("T", bound="LegacyJWTConfiguration")


@_attrs_define
class LegacyJWTConfiguration:
    """
    Attributes:
        expire_after (float):
        limits (AccountsTableRequestLimits | Unset):
        websockets (JWTConfigurationWebSocketData | Unset):
        name (str | Unset):
    """

    expire_after: float
    limits: AccountsTableRequestLimits | Unset = UNSET
    websockets: JWTConfigurationWebSocketData | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expire_after = self.expire_after

        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        websockets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.websockets, Unset):
            websockets = self.websockets.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expireAfter": expire_after,
            }
        )
        if limits is not UNSET:
            field_dict["limits"] = limits
        if websockets is not UNSET:
            field_dict["websockets"] = websockets
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accounts_table_request_limits import AccountsTableRequestLimits
        from ..models.jwt_configuration_web_socket_data import JWTConfigurationWebSocketData

        d = dict(src_dict)
        expire_after = d.pop("expireAfter")

        _limits = d.pop("limits", UNSET)
        limits: AccountsTableRequestLimits | Unset
        if isinstance(_limits, Unset):
            limits = UNSET
        else:
            limits = AccountsTableRequestLimits.from_dict(_limits)

        _websockets = d.pop("websockets", UNSET)
        websockets: JWTConfigurationWebSocketData | Unset
        if isinstance(_websockets, Unset):
            websockets = UNSET
        else:
            websockets = JWTConfigurationWebSocketData.from_dict(_websockets)

        name = d.pop("name", UNSET)

        legacy_jwt_configuration = cls(
            expire_after=expire_after,
            limits=limits,
            websockets=websockets,
            name=name,
        )

        legacy_jwt_configuration.additional_properties = d
        return legacy_jwt_configuration

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

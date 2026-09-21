from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jwt_configuration_web_socket_data import JWTConfigurationWebSocketData


T = TypeVar("T", bound="PartialEnabledBooleanConfigJWTConfigurationWebSocketData")


@_attrs_define
class PartialEnabledBooleanConfigJWTConfigurationWebSocketData:
    """
    Attributes:
        enabled (bool | Unset):
        config (JWTConfigurationWebSocketData | Unset):
    """

    enabled: bool | Unset = UNSET
    config: JWTConfigurationWebSocketData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jwt_configuration_web_socket_data import JWTConfigurationWebSocketData

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _config = d.pop("config", UNSET)
        config: JWTConfigurationWebSocketData | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = JWTConfigurationWebSocketData.from_dict(_config)

        partial_enabled_boolean_config_jwt_configuration_web_socket_data = cls(
            enabled=enabled,
            config=config,
        )

        partial_enabled_boolean_config_jwt_configuration_web_socket_data.additional_properties = d
        return partial_enabled_boolean_config_jwt_configuration_web_socket_data

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

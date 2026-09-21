from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jwt_configuration_metadata import JWTConfigurationMetadata
    from ..models.partial_enabled_boolean_config_jwt_configuration_web_socket_data import (
        PartialEnabledBooleanConfigJWTConfigurationWebSocketData,
    )
    from ..models.partial_enabled_boolean_limits_accounts_table_request_limits_or_null import (
        PartialEnabledBooleanLimitsAccountsTableRequestLimitsOrNull,
    )
    from ..models.partial_enabled_boolean_matches_string_array_access_permitted_boolean_upload_permitted_boolean import (
        PartialEnabledBooleanMatchesStringArrayAccessPermittedBooleanUploadPermittedBoolean,
    )


T = TypeVar("T", bound="JWTConfiguration")


@_attrs_define
class JWTConfiguration:
    """
    Attributes:
        metadata (JWTConfigurationMetadata):
        api (PartialEnabledBooleanLimitsAccountsTableRequestLimitsOrNull):
        websockets (PartialEnabledBooleanConfigJWTConfigurationWebSocketData | Unset):
        cdn (PartialEnabledBooleanMatchesStringArrayAccessPermittedBooleanUploadPermittedBoolean | Unset):
    """

    metadata: JWTConfigurationMetadata
    api: PartialEnabledBooleanLimitsAccountsTableRequestLimitsOrNull
    websockets: PartialEnabledBooleanConfigJWTConfigurationWebSocketData | Unset = UNSET
    cdn: PartialEnabledBooleanMatchesStringArrayAccessPermittedBooleanUploadPermittedBoolean | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata = self.metadata.to_dict()

        api = self.api.to_dict()

        websockets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.websockets, Unset):
            websockets = self.websockets.to_dict()

        cdn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cdn, Unset):
            cdn = self.cdn.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata": metadata,
                "api": api,
            }
        )
        if websockets is not UNSET:
            field_dict["websockets"] = websockets
        if cdn is not UNSET:
            field_dict["cdn"] = cdn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jwt_configuration_metadata import JWTConfigurationMetadata
        from ..models.partial_enabled_boolean_config_jwt_configuration_web_socket_data import (
            PartialEnabledBooleanConfigJWTConfigurationWebSocketData,
        )
        from ..models.partial_enabled_boolean_limits_accounts_table_request_limits_or_null import (
            PartialEnabledBooleanLimitsAccountsTableRequestLimitsOrNull,
        )
        from ..models.partial_enabled_boolean_matches_string_array_access_permitted_boolean_upload_permitted_boolean import (
            PartialEnabledBooleanMatchesStringArrayAccessPermittedBooleanUploadPermittedBoolean,
        )

        d = dict(src_dict)
        metadata = JWTConfigurationMetadata.from_dict(d.pop("metadata"))

        api = PartialEnabledBooleanLimitsAccountsTableRequestLimitsOrNull.from_dict(d.pop("api"))

        _websockets = d.pop("websockets", UNSET)
        websockets: PartialEnabledBooleanConfigJWTConfigurationWebSocketData | Unset
        if isinstance(_websockets, Unset):
            websockets = UNSET
        else:
            websockets = PartialEnabledBooleanConfigJWTConfigurationWebSocketData.from_dict(_websockets)

        _cdn = d.pop("cdn", UNSET)
        cdn: PartialEnabledBooleanMatchesStringArrayAccessPermittedBooleanUploadPermittedBoolean | Unset
        if isinstance(_cdn, Unset):
            cdn = UNSET
        else:
            cdn = PartialEnabledBooleanMatchesStringArrayAccessPermittedBooleanUploadPermittedBoolean.from_dict(_cdn)

        jwt_configuration = cls(
            metadata=metadata,
            api=api,
            websockets=websockets,
            cdn=cdn,
        )

        jwt_configuration.additional_properties = d
        return jwt_configuration

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

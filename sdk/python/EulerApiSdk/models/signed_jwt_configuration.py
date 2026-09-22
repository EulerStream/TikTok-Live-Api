from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accounts_table_request_limits import AccountsTableRequestLimits
    from ..models.partial_enabled_boolean_matches_string_array_access_permitted_boolean_upload_permitted_boolean import (
        PartialEnabledBooleanMatchesStringArrayAccessPermittedBooleanUploadPermittedBoolean,
    )
    from ..models.signed_jwt_configuration_extra import SignedJWTConfigurationExtra
    from ..models.signed_jwt_configuration_web_socket_data import SignedJWTConfigurationWebSocketData


T = TypeVar("T", bound="SignedJWTConfiguration")


@_attrs_define
class SignedJWTConfiguration:
    """
    Attributes:
        id (str):
        expires_at (float):
        ttl (float):
        account_id (float):
        api_key_id (float):
        name (None | str):
        extra (SignedJWTConfigurationExtra):
        limits (AccountsTableRequestLimits | Unset):
        web_socket_data (SignedJWTConfigurationWebSocketData | Unset):
        cdn (PartialEnabledBooleanMatchesStringArrayAccessPermittedBooleanUploadPermittedBoolean | Unset):
    """

    id: str
    expires_at: float
    ttl: float
    account_id: float
    api_key_id: float
    name: None | str
    extra: SignedJWTConfigurationExtra
    limits: AccountsTableRequestLimits | Unset = UNSET
    web_socket_data: SignedJWTConfigurationWebSocketData | Unset = UNSET
    cdn: PartialEnabledBooleanMatchesStringArrayAccessPermittedBooleanUploadPermittedBoolean | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        expires_at = self.expires_at

        ttl = self.ttl

        account_id = self.account_id

        api_key_id = self.api_key_id

        name: None | str
        name = self.name

        extra = self.extra.to_dict()

        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        web_socket_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.web_socket_data, Unset):
            web_socket_data = self.web_socket_data.to_dict()

        cdn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cdn, Unset):
            cdn = self.cdn.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "expiresAt": expires_at,
                "ttl": ttl,
                "accountId": account_id,
                "apiKeyId": api_key_id,
                "name": name,
                "extra": extra,
            }
        )
        if limits is not UNSET:
            field_dict["limits"] = limits
        if web_socket_data is not UNSET:
            field_dict["webSocketData"] = web_socket_data
        if cdn is not UNSET:
            field_dict["cdn"] = cdn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accounts_table_request_limits import AccountsTableRequestLimits  # noqa: PLC0415
        from ..models.partial_enabled_boolean_matches_string_array_access_permitted_boolean_upload_permitted_boolean import (
            PartialEnabledBooleanMatchesStringArrayAccessPermittedBooleanUploadPermittedBoolean,  # noqa: PLC0415
        )
        from ..models.signed_jwt_configuration_extra import SignedJWTConfigurationExtra  # noqa: PLC0415
        from ..models.signed_jwt_configuration_web_socket_data import (
            SignedJWTConfigurationWebSocketData,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        expires_at = d.pop("expiresAt")

        ttl = d.pop("ttl")

        account_id = d.pop("accountId")

        api_key_id = d.pop("apiKeyId")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        extra = SignedJWTConfigurationExtra.from_dict(d.pop("extra"))

        _limits = d.pop("limits", UNSET)
        limits: AccountsTableRequestLimits | Unset
        if isinstance(_limits, Unset):
            limits = UNSET
        else:
            limits = AccountsTableRequestLimits.from_dict(_limits)

        _web_socket_data = d.pop("webSocketData", UNSET)
        web_socket_data: SignedJWTConfigurationWebSocketData | Unset
        if isinstance(_web_socket_data, Unset):
            web_socket_data = UNSET
        else:
            web_socket_data = SignedJWTConfigurationWebSocketData.from_dict(_web_socket_data)

        _cdn = d.pop("cdn", UNSET)
        cdn: PartialEnabledBooleanMatchesStringArrayAccessPermittedBooleanUploadPermittedBoolean | Unset
        if isinstance(_cdn, Unset):
            cdn = UNSET
        else:
            cdn = PartialEnabledBooleanMatchesStringArrayAccessPermittedBooleanUploadPermittedBoolean.from_dict(_cdn)

        signed_jwt_configuration = cls(
            id=id,
            expires_at=expires_at,
            ttl=ttl,
            account_id=account_id,
            api_key_id=api_key_id,
            name=name,
            extra=extra,
            limits=limits,
            web_socket_data=web_socket_data,
            cdn=cdn,
        )

        signed_jwt_configuration.additional_properties = d
        return signed_jwt_configuration

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

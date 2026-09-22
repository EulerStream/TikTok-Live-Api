from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accounts_table_request_limits import AccountsTableRequestLimits


T = TypeVar("T", bound="PartialEnabledBooleanLimitsAccountsTableRequestLimitsOrNull")


@_attrs_define
class PartialEnabledBooleanLimitsAccountsTableRequestLimitsOrNull:
    """
    Attributes:
        enabled (bool | Unset):
        limits (AccountsTableRequestLimits | Unset):
    """

    enabled: bool | Unset = UNSET
    limits: AccountsTableRequestLimits | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if limits is not UNSET:
            field_dict["limits"] = limits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accounts_table_request_limits import AccountsTableRequestLimits  # noqa: PLC0415

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _limits = d.pop("limits", UNSET)
        limits: AccountsTableRequestLimits | Unset
        if isinstance(_limits, Unset):
            limits = UNSET
        else:
            limits = AccountsTableRequestLimits.from_dict(_limits)

        partial_enabled_boolean_limits_accounts_table_request_limits_or_null = cls(
            enabled=enabled,
            limits=limits,
        )

        partial_enabled_boolean_limits_accounts_table_request_limits_or_null.additional_properties = d
        return partial_enabled_boolean_limits_accounts_table_request_limits_or_null

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

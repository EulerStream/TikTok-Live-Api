from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartialEnabledBooleanMatchesStringArrayAccessPermittedBooleanUploadPermittedBoolean")


@_attrs_define
class PartialEnabledBooleanMatchesStringArrayAccessPermittedBooleanUploadPermittedBoolean:
    """
    Attributes:
        enabled (bool | Unset):
        matches (list[str] | Unset):
        access_permitted (bool | Unset):
        upload_permitted (bool | Unset):
    """

    enabled: bool | Unset = UNSET
    matches: list[str] | Unset = UNSET
    access_permitted: bool | Unset = UNSET
    upload_permitted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        matches: list[str] | Unset = UNSET
        if not isinstance(self.matches, Unset):
            matches = self.matches

        access_permitted = self.access_permitted

        upload_permitted = self.upload_permitted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if matches is not UNSET:
            field_dict["matches"] = matches
        if access_permitted is not UNSET:
            field_dict["access_permitted"] = access_permitted
        if upload_permitted is not UNSET:
            field_dict["upload_permitted"] = upload_permitted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        matches = cast(list[str], d.pop("matches", UNSET))

        access_permitted = d.pop("access_permitted", UNSET)

        upload_permitted = d.pop("upload_permitted", UNSET)

        partial_enabled_boolean_matches_string_array_access_permitted_boolean_upload_permitted_boolean = cls(
            enabled=enabled,
            matches=matches,
            access_permitted=access_permitted,
            upload_permitted=upload_permitted,
        )

        partial_enabled_boolean_matches_string_array_access_permitted_boolean_upload_permitted_boolean.additional_properties = d
        return partial_enabled_boolean_matches_string_array_access_permitted_boolean_upload_permitted_boolean

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

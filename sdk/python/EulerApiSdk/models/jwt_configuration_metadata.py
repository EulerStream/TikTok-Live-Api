from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.jwt_configuration_metadata_version import JWTConfigurationMetadataVersion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jwt_configuration_metadata_extra import JWTConfigurationMetadataExtra


T = TypeVar("T", bound="JWTConfigurationMetadata")


@_attrs_define
class JWTConfigurationMetadata:
    """
    Attributes:
        version (JWTConfigurationMetadataVersion):
        expire_after (float):
        extra (JWTConfigurationMetadataExtra | Unset):
        name (str | Unset):
    """

    version: JWTConfigurationMetadataVersion
    expire_after: float
    extra: JWTConfigurationMetadataExtra | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version.value

        expire_after = self.expire_after

        extra: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extra, Unset):
            extra = self.extra.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "expireAfter": expire_after,
            }
        )
        if extra is not UNSET:
            field_dict["extra"] = extra
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jwt_configuration_metadata_extra import JWTConfigurationMetadataExtra

        d = dict(src_dict)
        version = JWTConfigurationMetadataVersion(d.pop("version"))

        expire_after = d.pop("expireAfter")

        _extra = d.pop("extra", UNSET)
        extra: JWTConfigurationMetadataExtra | Unset
        if isinstance(_extra, Unset):
            extra = UNSET
        else:
            extra = JWTConfigurationMetadataExtra.from_dict(_extra)

        name = d.pop("name", UNSET)

        jwt_configuration_metadata = cls(
            version=version,
            expire_after=expire_after,
            extra=extra,
            name=name,
        )

        jwt_configuration_metadata.additional_properties = d
        return jwt_configuration_metadata

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

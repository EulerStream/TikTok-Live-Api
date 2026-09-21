from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_alert_target_payload_metadata import CreateAlertTargetPayloadMetadata


T = TypeVar("T", bound="CreateAlertTargetPayload")


@_attrs_define
class CreateAlertTargetPayload:
    """
    Attributes:
        url (str):
        metadata (CreateAlertTargetPayloadMetadata | Unset):
    """

    url: str
    metadata: CreateAlertTargetPayloadMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_alert_target_payload_metadata import CreateAlertTargetPayloadMetadata

        d = dict(src_dict)
        url = d.pop("url")

        _metadata = d.pop("metadata", UNSET)
        metadata: CreateAlertTargetPayloadMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateAlertTargetPayloadMetadata.from_dict(_metadata)

        create_alert_target_payload = cls(
            url=url,
            metadata=metadata,
        )

        create_alert_target_payload.additional_properties = d
        return create_alert_target_payload

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

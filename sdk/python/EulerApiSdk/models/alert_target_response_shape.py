from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.live_push_alert_target_format import LivePushAlertTargetFormat
from ..models.live_push_alert_target_status import LivePushAlertTargetStatus

if TYPE_CHECKING:
    from ..models.alert_target_response_shape_metadata import AlertTargetResponseShapeMetadata


T = TypeVar("T", bound="AlertTargetResponseShape")


@_attrs_define
class AlertTargetResponseShape:
    """Public, snake_case response shape for an alert target. Mirrors the legacy (`old-schema.json`) target shape as
    closely as the new gRPC {@link LivePushAlertTarget} model allows: field casing is converted, `metadata` is re-
    hydrated from the stored JSON string, the unix-ms timestamps are threaded back into ISO `created_at` / `updated_at`,
    and `alert_creator_id` is coerced to a number.

        Attributes:
            id (float):
            account_id (float):
            alert_id (float):
            alert_creator_id (float):
            url (str):
            metadata (AlertTargetResponseShapeMetadata):
            last_status (LivePushAlertTargetStatus):
            format_ (LivePushAlertTargetFormat):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
    """

    id: float
    account_id: float
    alert_id: float
    alert_creator_id: float
    url: str
    metadata: AlertTargetResponseShapeMetadata
    last_status: LivePushAlertTargetStatus
    format_: LivePushAlertTargetFormat
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        account_id = self.account_id

        alert_id = self.alert_id

        alert_creator_id = self.alert_creator_id

        url = self.url

        metadata = self.metadata.to_dict()

        last_status = self.last_status.value

        format_ = self.format_.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "account_id": account_id,
                "alert_id": alert_id,
                "alert_creator_id": alert_creator_id,
                "url": url,
                "metadata": metadata,
                "last_status": last_status,
                "format": format_,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_target_response_shape_metadata import AlertTargetResponseShapeMetadata

        d = dict(src_dict)
        id = d.pop("id")

        account_id = d.pop("account_id")

        alert_id = d.pop("alert_id")

        alert_creator_id = d.pop("alert_creator_id")

        url = d.pop("url")

        metadata = AlertTargetResponseShapeMetadata.from_dict(d.pop("metadata"))

        last_status = LivePushAlertTargetStatus(d.pop("last_status"))

        format_ = LivePushAlertTargetFormat(d.pop("format"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        alert_target_response_shape = cls(
            id=id,
            account_id=account_id,
            alert_id=alert_id,
            alert_creator_id=alert_creator_id,
            url=url,
            metadata=metadata,
            last_status=last_status,
            format_=format_,
            created_at=created_at,
            updated_at=updated_at,
        )

        alert_target_response_shape.additional_properties = d
        return alert_target_response_shape

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

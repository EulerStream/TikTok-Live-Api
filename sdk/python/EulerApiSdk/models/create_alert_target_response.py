from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_target_response_shape import AlertTargetResponseShape


T = TypeVar("T", bound="CreateAlertTargetResponse")


@_attrs_define
class CreateAlertTargetResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        target (AlertTargetResponseShape | Unset): Public, snake_case response shape for an alert target. Mirrors the
            legacy (`old-schema.json`) target shape as closely as the new gRPC {@link LivePushAlertTarget} model allows:
            field casing is converted, `metadata` is re-hydrated from the stored JSON string, the unix-ms timestamps are
            threaded back into ISO `created_at` / `updated_at`, and `alert_creator_id` is coerced to a number.
    """

    code: float
    message: str | Unset = UNSET
    target: AlertTargetResponseShape | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_target_response_shape import AlertTargetResponseShape

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _target = d.pop("target", UNSET)
        target: AlertTargetResponseShape | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = AlertTargetResponseShape.from_dict(_target)

        create_alert_target_response = cls(
            code=code,
            message=message,
            target=target,
        )

        create_alert_target_response.additional_properties = d
        return create_alert_target_response

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

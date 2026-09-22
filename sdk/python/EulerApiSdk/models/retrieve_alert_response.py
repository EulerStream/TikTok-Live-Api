from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_response_shape import AlertResponseShape
    from ..models.retrieve_alert_response_creator import RetrieveAlertResponseCreator


T = TypeVar("T", bound="RetrieveAlertResponse")


@_attrs_define
class RetrieveAlertResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        alert (AlertResponseShape | Unset): Public, snake_case response shape for an alert. The gRPC {@link
            LivePushAlert} model is camelCase; the public API has always exposed alerts in snake_case, so we convert before
            serializing. Only the field casing is changed here — types and field membership are left as-is.
        creator (RetrieveAlertResponseCreator | Unset):
    """

    code: float
    message: str | Unset = UNSET
    alert: AlertResponseShape | Unset = UNSET
    creator: RetrieveAlertResponseCreator | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        alert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alert, Unset):
            alert = self.alert.to_dict()

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if alert is not UNSET:
            field_dict["alert"] = alert
        if creator is not UNSET:
            field_dict["creator"] = creator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_response_shape import AlertResponseShape  # noqa: PLC0415
        from ..models.retrieve_alert_response_creator import RetrieveAlertResponseCreator  # noqa: PLC0415

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _alert = d.pop("alert", UNSET)
        alert: AlertResponseShape | Unset
        if isinstance(_alert, Unset):
            alert = UNSET
        else:
            alert = AlertResponseShape.from_dict(_alert)

        _creator = d.pop("creator", UNSET)
        creator: RetrieveAlertResponseCreator | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = RetrieveAlertResponseCreator.from_dict(_creator)

        retrieve_alert_response = cls(
            code=code,
            message=message,
            alert=alert,
            creator=creator,
        )

        retrieve_alert_response.additional_properties = d
        return retrieve_alert_response

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

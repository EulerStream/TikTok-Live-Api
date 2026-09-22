from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertResponseShape")


@_attrs_define
class AlertResponseShape:
    """Public, snake_case response shape for an alert. The gRPC {@link LivePushAlert} model is camelCase; the public API
    has always exposed alerts in snake_case, so we convert before serializing. Only the field casing is changed here —
    types and field membership are left as-is.

        Attributes:
            id (float):
            account_id (float):
            alert_creator_id (float):
            read_only (bool):
            enabled (bool):
            alert_creator_username (str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            alert_creator_user_id (str | Unset): The creator's TikTok numeric user id. Unset when the alerts service has not
                yet resolved it (the gRPC layer carries an empty string in that case).
            alert_creator_avatar_url (str | Unset):
            alert_creator_nickname (str | Unset):
    """

    id: float
    account_id: float
    alert_creator_id: float
    read_only: bool
    enabled: bool
    alert_creator_username: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    alert_creator_user_id: str | Unset = UNSET
    alert_creator_avatar_url: str | Unset = UNSET
    alert_creator_nickname: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        account_id = self.account_id

        alert_creator_id = self.alert_creator_id

        read_only = self.read_only

        enabled = self.enabled

        alert_creator_username = self.alert_creator_username

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        alert_creator_user_id = self.alert_creator_user_id

        alert_creator_avatar_url = self.alert_creator_avatar_url

        alert_creator_nickname = self.alert_creator_nickname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "account_id": account_id,
                "alert_creator_id": alert_creator_id,
                "read_only": read_only,
                "enabled": enabled,
                "alert_creator_username": alert_creator_username,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if alert_creator_user_id is not UNSET:
            field_dict["alert_creator_user_id"] = alert_creator_user_id
        if alert_creator_avatar_url is not UNSET:
            field_dict["alert_creator_avatar_url"] = alert_creator_avatar_url
        if alert_creator_nickname is not UNSET:
            field_dict["alert_creator_nickname"] = alert_creator_nickname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        account_id = d.pop("account_id")

        alert_creator_id = d.pop("alert_creator_id")

        read_only = d.pop("read_only")

        enabled = d.pop("enabled")

        alert_creator_username = d.pop("alert_creator_username")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        alert_creator_user_id = d.pop("alert_creator_user_id", UNSET)

        alert_creator_avatar_url = d.pop("alert_creator_avatar_url", UNSET)

        alert_creator_nickname = d.pop("alert_creator_nickname", UNSET)

        alert_response_shape = cls(
            id=id,
            account_id=account_id,
            alert_creator_id=alert_creator_id,
            read_only=read_only,
            enabled=enabled,
            alert_creator_username=alert_creator_username,
            created_at=created_at,
            updated_at=updated_at,
            alert_creator_user_id=alert_creator_user_id,
            alert_creator_avatar_url=alert_creator_avatar_url,
            alert_creator_nickname=alert_creator_nickname,
        )

        alert_response_shape.additional_properties = d
        return alert_response_shape

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

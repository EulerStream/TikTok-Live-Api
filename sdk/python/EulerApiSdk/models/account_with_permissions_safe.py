from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_scopes import AccountScopes

T = TypeVar("T", bound="AccountWithPermissionsSafe")


@_attrs_define
class AccountWithPermissionsSafe:
    """
    Attributes:
        day (float):
        hour (float):
        minute (float):
        name (str):
        webhook_secret (str):
        max_alerts (float):
        max_websockets (float):
        expires_at (datetime.datetime | None):
        purchased_captcha_credits (float):
        updated_at (datetime.datetime):
        created_at (datetime.datetime):
        id (float):
        scopes (list[AccountScopes]):
    """

    day: float
    hour: float
    minute: float
    name: str
    webhook_secret: str
    max_alerts: float
    max_websockets: float
    expires_at: datetime.datetime | None
    purchased_captcha_credits: float
    updated_at: datetime.datetime
    created_at: datetime.datetime
    id: float
    scopes: list[AccountScopes]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day = self.day

        hour = self.hour

        minute = self.minute

        name = self.name

        webhook_secret = self.webhook_secret

        max_alerts = self.max_alerts

        max_websockets = self.max_websockets

        expires_at: None | str
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        purchased_captcha_credits = self.purchased_captcha_credits

        updated_at = self.updated_at.isoformat()

        created_at = self.created_at.isoformat()

        id = self.id

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.value
            scopes.append(scopes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "day": day,
                "hour": hour,
                "minute": minute,
                "name": name,
                "webhook_secret": webhook_secret,
                "max_alerts": max_alerts,
                "max_websockets": max_websockets,
                "expires_at": expires_at,
                "purchased_captcha_credits": purchased_captcha_credits,
                "updated_at": updated_at,
                "created_at": created_at,
                "id": id,
                "scopes": scopes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        day = d.pop("day")

        hour = d.pop("hour")

        minute = d.pop("minute")

        name = d.pop("name")

        webhook_secret = d.pop("webhook_secret")

        max_alerts = d.pop("max_alerts")

        max_websockets = d.pop("max_websockets")

        def _parse_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        purchased_captcha_credits = d.pop("purchased_captcha_credits")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = AccountScopes(scopes_item_data)

            scopes.append(scopes_item)

        account_with_permissions_safe = cls(
            day=day,
            hour=hour,
            minute=minute,
            name=name,
            webhook_secret=webhook_secret,
            max_alerts=max_alerts,
            max_websockets=max_websockets,
            expires_at=expires_at,
            purchased_captcha_credits=purchased_captcha_credits,
            updated_at=updated_at,
            created_at=created_at,
            id=id,
            scopes=scopes,
        )

        account_with_permissions_safe.additional_properties = d
        return account_with_permissions_safe

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

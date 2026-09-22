from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ApiKey")


@_attrs_define
class ApiKey:
    """
    Attributes:
        name (str):
        value (str):
        account_id (float):
        updated_at (datetime.datetime):
        created_at (datetime.datetime):
        id (float):
    """

    name: str
    value: str
    account_id: float
    updated_at: datetime.datetime
    created_at: datetime.datetime
    id: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = self.value

        account_id = self.account_id

        updated_at = self.updated_at.isoformat()

        created_at = self.created_at.isoformat()

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
                "account_id": account_id,
                "updated_at": updated_at,
                "created_at": created_at,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        value = d.pop("value")

        account_id = d.pop("account_id")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        api_key = cls(
            name=name,
            value=value,
            account_id=account_id,
            updated_at=updated_at,
            created_at=created_at,
            id=id,
        )

        api_key.additional_properties = d
        return api_key

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.o_auth_scope import OAuthScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidateRefreshResponse")


@_attrs_define
class ValidateRefreshResponse:
    """
    Attributes:
        code (float):
        valid (bool):
        message (str | Unset):
        scopes (list[OAuthScope] | Unset):
        tiktok_user_id (None | str | Unset):
        country_code (None | str | Unset):
    """

    code: float
    valid: bool
    message: str | Unset = UNSET
    scopes: list[OAuthScope] | Unset = UNSET
    tiktok_user_id: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        valid = self.valid

        message = self.message

        scopes: list[str] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = []
            for scopes_item_data in self.scopes:
                scopes_item = scopes_item_data.value
                scopes.append(scopes_item)

        tiktok_user_id: None | str | Unset
        if isinstance(self.tiktok_user_id, Unset):
            tiktok_user_id = UNSET
        else:
            tiktok_user_id = self.tiktok_user_id

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "valid": valid,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if tiktok_user_id is not UNSET:
            field_dict["tiktok_user_id"] = tiktok_user_id
        if country_code is not UNSET:
            field_dict["country_code"] = country_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        valid = d.pop("valid")

        message = d.pop("message", UNSET)

        _scopes = d.pop("scopes", UNSET)
        scopes: list[OAuthScope] | Unset = UNSET
        if _scopes is not UNSET:
            scopes = []
            for scopes_item_data in _scopes:
                scopes_item = OAuthScope(scopes_item_data)

                scopes.append(scopes_item)

        def _parse_tiktok_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tiktok_user_id = _parse_tiktok_user_id(d.pop("tiktok_user_id", UNSET))

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("country_code", UNSET))

        validate_refresh_response = cls(
            code=code,
            valid=valid,
            message=message,
            scopes=scopes,
            tiktok_user_id=tiktok_user_id,
            country_code=country_code,
        )

        validate_refresh_response.additional_properties = d
        return validate_refresh_response

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

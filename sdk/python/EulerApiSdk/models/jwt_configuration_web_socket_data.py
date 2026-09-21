from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JWTConfigurationWebSocketData")


@_attrs_define
class JWTConfigurationWebSocketData:
    """
    Attributes:
        allowed_creators (list[str] | None):
        max_web_sockets (float):
        oauth_token (str | Unset):
        tt_target_idc (str | Unset):
        session_id (str | Unset):
    """

    allowed_creators: list[str] | None
    max_web_sockets: float
    oauth_token: str | Unset = UNSET
    tt_target_idc: str | Unset = UNSET
    session_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_creators: list[str] | None
        if isinstance(self.allowed_creators, list):
            allowed_creators = self.allowed_creators

        else:
            allowed_creators = self.allowed_creators

        max_web_sockets = self.max_web_sockets

        oauth_token = self.oauth_token

        tt_target_idc = self.tt_target_idc

        session_id = self.session_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowedCreators": allowed_creators,
                "maxWebSockets": max_web_sockets,
            }
        )
        if oauth_token is not UNSET:
            field_dict["oauthToken"] = oauth_token
        if tt_target_idc is not UNSET:
            field_dict["ttTargetIdc"] = tt_target_idc
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_allowed_creators(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_creators_type_0 = cast(list[str], data)

                return allowed_creators_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        allowed_creators = _parse_allowed_creators(d.pop("allowedCreators"))

        max_web_sockets = d.pop("maxWebSockets")

        oauth_token = d.pop("oauthToken", UNSET)

        tt_target_idc = d.pop("ttTargetIdc", UNSET)

        session_id = d.pop("sessionId", UNSET)

        jwt_configuration_web_socket_data = cls(
            allowed_creators=allowed_creators,
            max_web_sockets=max_web_sockets,
            oauth_token=oauth_token,
            tt_target_idc=tt_target_idc,
            session_id=session_id,
        )

        jwt_configuration_web_socket_data.additional_properties = d
        return jwt_configuration_web_socket_data

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

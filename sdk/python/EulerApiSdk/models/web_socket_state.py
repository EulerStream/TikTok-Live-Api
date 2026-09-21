from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.peer_role import PeerRole

T = TypeVar("T", bound="WebSocketState")


@_attrs_define
class WebSocketState:
    """
    Attributes:
        deployment (PeerRole):
        account_id (float):
        unique_id (str):
        created_at (float):
        api_key_id (float):
        jwt_has_session_id (bool):
        jwt_name (None | str):
        jwt_id (None | str):
        heartbeat (float):
        ws_id (str):
    """

    deployment: PeerRole
    account_id: float
    unique_id: str
    created_at: float
    api_key_id: float
    jwt_has_session_id: bool
    jwt_name: None | str
    jwt_id: None | str
    heartbeat: float
    ws_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deployment = self.deployment.value

        account_id = self.account_id

        unique_id = self.unique_id

        created_at = self.created_at

        api_key_id = self.api_key_id

        jwt_has_session_id = self.jwt_has_session_id

        jwt_name: None | str
        jwt_name = self.jwt_name

        jwt_id: None | str
        jwt_id = self.jwt_id

        heartbeat = self.heartbeat

        ws_id = self.ws_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deployment": deployment,
                "accountId": account_id,
                "uniqueId": unique_id,
                "createdAt": created_at,
                "apiKeyId": api_key_id,
                "jwtHasSessionId": jwt_has_session_id,
                "jwtName": jwt_name,
                "jwtId": jwt_id,
                "heartbeat": heartbeat,
                "wsId": ws_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deployment = PeerRole(d.pop("deployment"))

        account_id = d.pop("accountId")

        unique_id = d.pop("uniqueId")

        created_at = d.pop("createdAt")

        api_key_id = d.pop("apiKeyId")

        jwt_has_session_id = d.pop("jwtHasSessionId")

        def _parse_jwt_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        jwt_name = _parse_jwt_name(d.pop("jwtName"))

        def _parse_jwt_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        jwt_id = _parse_jwt_id(d.pop("jwtId"))

        heartbeat = d.pop("heartbeat")

        ws_id = d.pop("wsId")

        web_socket_state = cls(
            deployment=deployment,
            account_id=account_id,
            unique_id=unique_id,
            created_at=created_at,
            api_key_id=api_key_id,
            jwt_has_session_id=jwt_has_session_id,
            jwt_name=jwt_name,
            jwt_id=jwt_id,
            heartbeat=heartbeat,
            ws_id=ws_id,
        )

        web_socket_state.additional_properties = d
        return web_socket_state

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_o_auth_client_info import PublicOAuthClientInfo


T = TypeVar("T", bound="GetPublicClientResponse")


@_attrs_define
class GetPublicClientResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        client (PublicOAuthClientInfo | Unset):
    """

    code: float
    message: str | Unset = UNSET
    client: PublicOAuthClientInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        client: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if client is not UNSET:
            field_dict["client"] = client

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_o_auth_client_info import PublicOAuthClientInfo  # noqa: PLC0415

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _client = d.pop("client", UNSET)
        client: PublicOAuthClientInfo | Unset
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = PublicOAuthClientInfo.from_dict(_client)

        get_public_client_response = cls(
            code=code,
            message=message,
            client=client,
        )

        get_public_client_response.additional_properties = d
        return get_public_client_response

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.o_auth_client_mode import OAuthClientMode
from ..models.o_auth_scope import OAuthScope

T = TypeVar("T", bound="PublicOAuthClientInfo")


@_attrs_define
class PublicOAuthClientInfo:
    """
    Attributes:
        client_id (str):
        name (str):
        description (None | str):
        redirect_uris (list[str]):
        supported_scopes (list[OAuthScope]):
        theme (None | str):
        mode (None | OAuthClientMode):
        logo (None | str):
    """

    client_id: str
    name: str
    description: None | str
    redirect_uris: list[str]
    supported_scopes: list[OAuthScope]
    theme: None | str
    mode: None | OAuthClientMode
    logo: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        name = self.name

        description: None | str
        description = self.description

        redirect_uris = self.redirect_uris

        supported_scopes = []
        for supported_scopes_item_data in self.supported_scopes:
            supported_scopes_item = supported_scopes_item_data.value
            supported_scopes.append(supported_scopes_item)

        theme: None | str
        theme = self.theme

        mode: None | str
        if isinstance(self.mode, OAuthClientMode):
            mode = self.mode.value
        else:
            mode = self.mode

        logo: None | str
        logo = self.logo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client_id": client_id,
                "name": name,
                "description": description,
                "redirect_uris": redirect_uris,
                "supported_scopes": supported_scopes,
                "theme": theme,
                "mode": mode,
                "logo": logo,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("client_id")

        name = d.pop("name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        redirect_uris = cast(list[str], d.pop("redirect_uris"))

        supported_scopes = []
        _supported_scopes = d.pop("supported_scopes")
        for supported_scopes_item_data in _supported_scopes:
            supported_scopes_item = OAuthScope(supported_scopes_item_data)

            supported_scopes.append(supported_scopes_item)

        def _parse_theme(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        theme = _parse_theme(d.pop("theme"))

        def _parse_mode(data: object) -> None | OAuthClientMode:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_1 = OAuthClientMode(data)

                return mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OAuthClientMode, data)

        mode = _parse_mode(d.pop("mode"))

        def _parse_logo(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        logo = _parse_logo(d.pop("logo"))

        public_o_auth_client_info = cls(
            client_id=client_id,
            name=name,
            description=description,
            redirect_uris=redirect_uris,
            supported_scopes=supported_scopes,
            theme=theme,
            mode=mode,
            logo=logo,
        )

        public_o_auth_client_info.additional_properties = d
        return public_o_auth_client_info

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tik_tok_o_auth_user_info import TikTokOAuthUserInfo


T = TypeVar("T", bound="OAuthUserInfoResponse")


@_attrs_define
class OAuthUserInfoResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        user (TikTokOAuthUserInfo | Unset):
    """

    code: float
    message: str | Unset = UNSET
    user: TikTokOAuthUserInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tik_tok_o_auth_user_info import TikTokOAuthUserInfo

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _user = d.pop("user", UNSET)
        user: TikTokOAuthUserInfo | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = TikTokOAuthUserInfo.from_dict(_user)

        o_auth_user_info_response = cls(
            code=code,
            message=message,
            user=user,
        )

        o_auth_user_info_response.additional_properties = d
        return o_auth_user_info_response

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

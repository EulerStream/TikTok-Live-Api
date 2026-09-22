from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tik_tok_user_basic_user import TikTokUserBasicUser


T = TypeVar("T", bound="RetrieveTikTokUserBasicResponse")


@_attrs_define
class RetrieveTikTokUserBasicResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        user (TikTokUserBasicUser | Unset):
    """

    code: float
    message: str | Unset = UNSET
    user: TikTokUserBasicUser | Unset = UNSET
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
        from ..models.tik_tok_user_basic_user import TikTokUserBasicUser  # noqa: PLC0415

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _user = d.pop("user", UNSET)
        user: TikTokUserBasicUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = TikTokUserBasicUser.from_dict(_user)

        retrieve_tik_tok_user_basic_response = cls(
            code=code,
            message=message,
            user=user,
        )

        retrieve_tik_tok_user_basic_response.additional_properties = d
        return retrieve_tik_tok_user_basic_response

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

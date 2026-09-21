from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.whirl_result import WhirlResult


T = TypeVar("T", bound="WhirlCaptchaResponse")


@_attrs_define
class WhirlCaptchaResponse:
    """
    Attributes:
        code (float):
        response (WhirlResult):
        cached (bool):
        message (str | Unset):
    """

    code: float
    response: WhirlResult
    cached: bool
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        response = self.response.to_dict()

        cached = self.cached

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "response": response,
                "cached": cached,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.whirl_result import WhirlResult

        d = dict(src_dict)
        code = d.pop("code")

        response = WhirlResult.from_dict(d.pop("response"))

        cached = d.pop("cached")

        message = d.pop("message", UNSET)

        whirl_captcha_response = cls(
            code=code,
            response=response,
            cached=cached,
            message=message,
        )

        whirl_captcha_response.additional_properties = d
        return whirl_captcha_response

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

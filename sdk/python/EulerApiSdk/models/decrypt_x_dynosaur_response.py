from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.decrypt_x_dynosaur_response_data import DecryptXDynosaurResponseData
    from ..models.x_dynosaur_header import XDynosaurHeader


T = TypeVar("T", bound="DecryptXDynosaurResponse")


@_attrs_define
class DecryptXDynosaurResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        header (XDynosaurHeader | Unset):
        data (DecryptXDynosaurResponseData | Unset): Decoded records under their mapped names. Records the version does
            not map appear as `field_<tag>`.
        unknown_tags (list[float] | Unset): Record tags carried by the token but missing from this version's field map.
        truncated (bool | Unset): A trailing fragment could not be read as a whole record. The records above are still
            valid.
    """

    code: float
    message: str | Unset = UNSET
    header: XDynosaurHeader | Unset = UNSET
    data: DecryptXDynosaurResponseData | Unset = UNSET
    unknown_tags: list[float] | Unset = UNSET
    truncated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.header, Unset):
            header = self.header.to_dict()

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        unknown_tags: list[float] | Unset = UNSET
        if not isinstance(self.unknown_tags, Unset):
            unknown_tags = self.unknown_tags

        truncated = self.truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if header is not UNSET:
            field_dict["header"] = header
        if data is not UNSET:
            field_dict["data"] = data
        if unknown_tags is not UNSET:
            field_dict["unknown_tags"] = unknown_tags
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.decrypt_x_dynosaur_response_data import DecryptXDynosaurResponseData  # noqa: PLC0415
        from ..models.x_dynosaur_header import XDynosaurHeader  # noqa: PLC0415

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _header = d.pop("header", UNSET)
        header: XDynosaurHeader | Unset
        if isinstance(_header, Unset):
            header = UNSET
        else:
            header = XDynosaurHeader.from_dict(_header)

        _data = d.pop("data", UNSET)
        data: DecryptXDynosaurResponseData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = DecryptXDynosaurResponseData.from_dict(_data)

        unknown_tags = cast(list[float], d.pop("unknown_tags", UNSET))

        truncated = d.pop("truncated", UNSET)

        decrypt_x_dynosaur_response = cls(
            code=code,
            message=message,
            header=header,
            data=data,
            unknown_tags=unknown_tags,
            truncated=truncated,
        )

        decrypt_x_dynosaur_response.additional_properties = d
        return decrypt_x_dynosaur_response

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

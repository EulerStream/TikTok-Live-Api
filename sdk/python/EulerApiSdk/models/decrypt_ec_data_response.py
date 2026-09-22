from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.decrypt_ec_data_response_data import DecryptEcDataResponseData


T = TypeVar("T", bound="DecryptEcDataResponse")


@_attrs_define
class DecryptEcDataResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        data (DecryptEcDataResponseData | Unset): The decoded report as objects keyed by field id, its trailer under
            `_trailer`. Free-form, and lossy: field order cannot be recovered from it.
        tree (list[Any] | Unset): The same report as the `[id, type, value]` tuple tree it arrived as, in wire order,
            with string and integer leaves in plaintext. Lossless.
    """

    code: float
    message: str | Unset = UNSET
    data: DecryptEcDataResponseData | Unset = UNSET
    tree: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        tree: list[Any] | Unset = UNSET
        if not isinstance(self.tree, Unset):
            tree = self.tree

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if data is not UNSET:
            field_dict["data"] = data
        if tree is not UNSET:
            field_dict["tree"] = tree

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.decrypt_ec_data_response_data import DecryptEcDataResponseData  # noqa: PLC0415

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _data = d.pop("data", UNSET)
        data: DecryptEcDataResponseData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = DecryptEcDataResponseData.from_dict(_data)

        tree = cast(list[Any], d.pop("tree", UNSET))

        decrypt_ec_data_response = cls(
            code=code,
            message=message,
            data=data,
            tree=tree,
        )

        decrypt_ec_data_response.additional_properties = d
        return decrypt_ec_data_response

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

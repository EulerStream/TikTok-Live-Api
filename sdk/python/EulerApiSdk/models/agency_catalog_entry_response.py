from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agency_catalog_entry import AgencyCatalogEntry


T = TypeVar("T", bound="AgencyCatalogEntryResponse")


@_attrs_define
class AgencyCatalogEntryResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        agency (AgencyCatalogEntry | Unset): Public (snake_case) projection of a catalog agency row.
    """

    code: float
    message: str | Unset = UNSET
    agency: AgencyCatalogEntry | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        agency: dict[str, Any] | Unset = UNSET
        if not isinstance(self.agency, Unset):
            agency = self.agency.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if agency is not UNSET:
            field_dict["agency"] = agency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agency_catalog_entry import AgencyCatalogEntry  # noqa: PLC0415

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _agency = d.pop("agency", UNSET)
        agency: AgencyCatalogEntry | Unset
        if isinstance(_agency, Unset):
            agency = UNSET
        else:
            agency = AgencyCatalogEntry.from_dict(_agency)

        agency_catalog_entry_response = cls(
            code=code,
            message=message,
            agency=agency,
        )

        agency_catalog_entry_response.additional_properties = d
        return agency_catalog_entry_response

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

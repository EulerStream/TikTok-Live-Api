from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agency_catalog_entry import AgencyCatalogEntry


T = TypeVar("T", bound="AgencyCatalogSearchResponse")


@_attrs_define
class AgencyCatalogSearchResponse:
    """
    Attributes:
        code (float):
        agencies (list[AgencyCatalogEntry]):
        message (str | Unset):
        page (float | Unset):
        page_size (float | Unset):
        has_more (bool | Unset):
    """

    code: float
    agencies: list[AgencyCatalogEntry]
    message: str | Unset = UNSET
    page: float | Unset = UNSET
    page_size: float | Unset = UNSET
    has_more: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        agencies = []
        for agencies_item_data in self.agencies:
            agencies_item = agencies_item_data.to_dict()
            agencies.append(agencies_item)

        message = self.message

        page = self.page

        page_size = self.page_size

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "agencies": agencies,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["page_size"] = page_size
        if has_more is not UNSET:
            field_dict["has_more"] = has_more

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agency_catalog_entry import AgencyCatalogEntry  # noqa: PLC0415

        d = dict(src_dict)
        code = d.pop("code")

        agencies = []
        _agencies = d.pop("agencies")
        for agencies_item_data in _agencies:
            agencies_item = AgencyCatalogEntry.from_dict(agencies_item_data)

            agencies.append(agencies_item)

        message = d.pop("message", UNSET)

        page = d.pop("page", UNSET)

        page_size = d.pop("page_size", UNSET)

        has_more = d.pop("has_more", UNSET)

        agency_catalog_search_response = cls(
            code=code,
            agencies=agencies,
            message=message,
            page=page,
            page_size=page_size,
            has_more=has_more,
        )

        agency_catalog_search_response.additional_properties = d
        return agency_catalog_search_response

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

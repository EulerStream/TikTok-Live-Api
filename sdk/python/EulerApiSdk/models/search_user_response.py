from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_user_result import SearchUserResult


T = TypeVar("T", bound="SearchUserResponse")


@_attrs_define
class SearchUserResponse:
    """
    Attributes:
        code (float):
        results (list[SearchUserResult]):
        message (str | Unset):
    """

    code: float
    results: list[SearchUserResult]
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "results": results,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_user_result import SearchUserResult

        d = dict(src_dict)
        code = d.pop("code")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = SearchUserResult.from_dict(results_item_data)

            results.append(results_item)

        message = d.pop("message", UNSET)

        search_user_response = cls(
            code=code,
            results=results,
            message=message,
        )

        search_user_response.additional_properties = d
        return search_user_response

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

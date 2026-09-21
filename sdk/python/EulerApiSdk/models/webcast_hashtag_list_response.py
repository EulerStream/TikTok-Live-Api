from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_hashtag_list_response_data import WebcastHashtagListResponseData
    from ..models.webcast_hashtag_list_response_extra import WebcastHashtagListResponseExtra


T = TypeVar("T", bound="WebcastHashtagListResponse")


@_attrs_define
class WebcastHashtagListResponse:
    """
    Attributes:
        data (WebcastHashtagListResponseData):
        extra (WebcastHashtagListResponseExtra):
        status_code (float):
    """

    data: WebcastHashtagListResponseData
    extra: WebcastHashtagListResponseExtra
    status_code: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        extra = self.extra.to_dict()

        status_code = self.status_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "extra": extra,
                "status_code": status_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_hashtag_list_response_data import WebcastHashtagListResponseData
        from ..models.webcast_hashtag_list_response_extra import WebcastHashtagListResponseExtra

        d = dict(src_dict)
        data = WebcastHashtagListResponseData.from_dict(d.pop("data"))

        extra = WebcastHashtagListResponseExtra.from_dict(d.pop("extra"))

        status_code = d.pop("status_code")

        webcast_hashtag_list_response = cls(
            data=data,
            extra=extra,
            status_code=status_code,
        )

        webcast_hashtag_list_response.additional_properties = d
        return webcast_hashtag_list_response

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

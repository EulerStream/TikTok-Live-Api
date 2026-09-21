from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_user_interactions_response_data import (
        WebcastLiveAnalyticsUserInteractionsResponseData,
    )
    from ..models.webcast_live_analytics_user_interactions_response_extra import (
        WebcastLiveAnalyticsUserInteractionsResponseExtra,
    )


T = TypeVar("T", bound="WebcastLiveAnalyticsUserInteractionsResponse")


@_attrs_define
class WebcastLiveAnalyticsUserInteractionsResponse:
    """
    Attributes:
        data (WebcastLiveAnalyticsUserInteractionsResponseData):
        extra (WebcastLiveAnalyticsUserInteractionsResponseExtra):
        status_code (float):
    """

    data: WebcastLiveAnalyticsUserInteractionsResponseData
    extra: WebcastLiveAnalyticsUserInteractionsResponseExtra
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
        from ..models.webcast_live_analytics_user_interactions_response_data import (
            WebcastLiveAnalyticsUserInteractionsResponseData,
        )
        from ..models.webcast_live_analytics_user_interactions_response_extra import (
            WebcastLiveAnalyticsUserInteractionsResponseExtra,
        )

        d = dict(src_dict)
        data = WebcastLiveAnalyticsUserInteractionsResponseData.from_dict(d.pop("data"))

        extra = WebcastLiveAnalyticsUserInteractionsResponseExtra.from_dict(d.pop("extra"))

        status_code = d.pop("status_code")

        webcast_live_analytics_user_interactions_response = cls(
            data=data,
            extra=extra,
            status_code=status_code,
        )

        webcast_live_analytics_user_interactions_response.additional_properties = d
        return webcast_live_analytics_user_interactions_response

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

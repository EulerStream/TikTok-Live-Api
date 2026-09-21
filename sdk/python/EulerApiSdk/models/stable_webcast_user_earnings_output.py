from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.stable_webcast_user_earnings_output_earnings_estimate_currency import (
    StableWebcastUserEarningsOutputEarningsEstimateCurrency,
)
from ..models.webcast_user_earnings_output_period import WebcastUserEarningsOutputPeriod

if TYPE_CHECKING:
    from ..models.stable_tik_tok_live_user import StableTikTokLiveUser


T = TypeVar("T", bound="StableWebcastUserEarningsOutput")


@_attrs_define
class StableWebcastUserEarningsOutput:
    """
    Attributes:
        resets_in (float | None):
        resets_at (datetime.datetime | None):
        period (WebcastUserEarningsOutputPeriod):
        diamonds (float | None):
        earnings_estimate (float | None):
        earnings_estimate_currency (StableWebcastUserEarningsOutputEarningsEstimateCurrency):
        user (StableTikTokLiveUser):
    """

    resets_in: float | None
    resets_at: datetime.datetime | None
    period: WebcastUserEarningsOutputPeriod
    diamonds: float | None
    earnings_estimate: float | None
    earnings_estimate_currency: StableWebcastUserEarningsOutputEarningsEstimateCurrency
    user: StableTikTokLiveUser
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resets_in: float | None
        resets_in = self.resets_in

        resets_at: None | str
        if isinstance(self.resets_at, datetime.datetime):
            resets_at = self.resets_at.isoformat()
        else:
            resets_at = self.resets_at

        period = self.period.value

        diamonds: float | None
        diamonds = self.diamonds

        earnings_estimate: float | None
        earnings_estimate = self.earnings_estimate

        earnings_estimate_currency = self.earnings_estimate_currency.value

        user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resets_in": resets_in,
                "resets_at": resets_at,
                "period": period,
                "diamonds": diamonds,
                "earnings_estimate": earnings_estimate,
                "earnings_estimate_currency": earnings_estimate_currency,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stable_tik_tok_live_user import StableTikTokLiveUser

        d = dict(src_dict)

        def _parse_resets_in(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        resets_in = _parse_resets_in(d.pop("resets_in"))

        def _parse_resets_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resets_at_type_0 = isoparse(data)

                return resets_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        resets_at = _parse_resets_at(d.pop("resets_at"))

        period = WebcastUserEarningsOutputPeriod(d.pop("period"))

        def _parse_diamonds(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        diamonds = _parse_diamonds(d.pop("diamonds"))

        def _parse_earnings_estimate(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        earnings_estimate = _parse_earnings_estimate(d.pop("earnings_estimate"))

        earnings_estimate_currency = StableWebcastUserEarningsOutputEarningsEstimateCurrency(
            d.pop("earnings_estimate_currency")
        )

        user = StableTikTokLiveUser.from_dict(d.pop("user"))

        stable_webcast_user_earnings_output = cls(
            resets_in=resets_in,
            resets_at=resets_at,
            period=period,
            diamonds=diamonds,
            earnings_estimate=earnings_estimate,
            earnings_estimate_currency=earnings_estimate_currency,
            user=user,
        )

        stable_webcast_user_earnings_output.additional_properties = d
        return stable_webcast_user_earnings_output

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

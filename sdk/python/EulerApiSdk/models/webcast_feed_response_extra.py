from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_feed_response_extra_banner import WebcastFeedResponseExtraBanner
    from ..models.webcast_feed_response_extra_log_pb import WebcastFeedResponseExtraLogPb


T = TypeVar("T", bound="WebcastFeedResponseExtra")


@_attrs_define
class WebcastFeedResponseExtra:
    """
    Attributes:
        now (float):
        unread_extra (str):
        banner (WebcastFeedResponseExtraBanner):
        total (float):
        max_time (float):
        cost (float):
        is_backup (float):
        has_more (bool):
        log_pb (WebcastFeedResponseExtraLogPb):
    """

    now: float
    unread_extra: str
    banner: WebcastFeedResponseExtraBanner
    total: float
    max_time: float
    cost: float
    is_backup: float
    has_more: bool
    log_pb: WebcastFeedResponseExtraLogPb
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        now = self.now

        unread_extra = self.unread_extra

        banner = self.banner.to_dict()

        total = self.total

        max_time = self.max_time

        cost = self.cost

        is_backup = self.is_backup

        has_more = self.has_more

        log_pb = self.log_pb.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "now": now,
                "unread_extra": unread_extra,
                "banner": banner,
                "total": total,
                "max_time": max_time,
                "cost": cost,
                "is_backup": is_backup,
                "has_more": has_more,
                "log_pb": log_pb,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_feed_response_extra_banner import WebcastFeedResponseExtraBanner  # noqa: PLC0415
        from ..models.webcast_feed_response_extra_log_pb import WebcastFeedResponseExtraLogPb  # noqa: PLC0415

        d = dict(src_dict)
        now = d.pop("now")

        unread_extra = d.pop("unread_extra")

        banner = WebcastFeedResponseExtraBanner.from_dict(d.pop("banner"))

        total = d.pop("total")

        max_time = d.pop("max_time")

        cost = d.pop("cost")

        is_backup = d.pop("is_backup")

        has_more = d.pop("has_more")

        log_pb = WebcastFeedResponseExtraLogPb.from_dict(d.pop("log_pb"))

        webcast_feed_response_extra = cls(
            now=now,
            unread_extra=unread_extra,
            banner=banner,
            total=total,
            max_time=max_time,
            cost=cost,
            is_backup=is_backup,
            has_more=has_more,
            log_pb=log_pb,
        )

        webcast_feed_response_extra.additional_properties = d
        return webcast_feed_response_extra

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

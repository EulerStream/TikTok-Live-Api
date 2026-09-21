from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_event_image import WebcastEventImage


T = TypeVar("T", bound="WebcastEventHost")


@_attrs_define
class WebcastEventHost:
    """
    Attributes:
        uid (str):
        short_id (str):
        nickname (str):
        signature (str):
        unique_id (str):
        sec_uid (str):
        region (str):
        avatar_larger (WebcastEventImage): Look up a single TikTok LIVE event (a scheduled/subscription stream) by its
            `event_id` via the unsigned `/tiktok/event/get/v1` endpoint on `webcast.tiktok.com`. No cookies and no signature
            are required; every query param is a baked-in constant except `event_id` and a generated `device_id`. The
            request is routed through the caller-provided proxy (the route does not self-select one). Success is signalled
            by a top-level `status_code === 0` with an `event` payload.
        avatar_medium (WebcastEventImage): Look up a single TikTok LIVE event (a scheduled/subscription stream) by its
            `event_id` via the unsigned `/tiktok/event/get/v1` endpoint on `webcast.tiktok.com`. No cookies and no signature
            are required; every query param is a baked-in constant except `event_id` and a generated `device_id`. The
            request is routed through the caller-provided proxy (the route does not self-select one). Success is signalled
            by a top-level `status_code === 0` with an `event` payload.
        avatar_thumb (WebcastEventImage): Look up a single TikTok LIVE event (a scheduled/subscription stream) by its
            `event_id` via the unsigned `/tiktok/event/get/v1` endpoint on `webcast.tiktok.com`. No cookies and no signature
            are required; every query param is a baked-in constant except `event_id` and a generated `device_id`. The
            request is routed through the caller-provided proxy (the route does not self-select one). Success is signalled
            by a top-level `status_code === 0` with an `event` payload.
        custom_verify (str):
        enterprise_verify_reason (str):
        verify_info (str):
        verification_type (float):
        follow_status (float):
        follower_status (float):
        language (str):
    """

    uid: str
    short_id: str
    nickname: str
    signature: str
    unique_id: str
    sec_uid: str
    region: str
    avatar_larger: WebcastEventImage
    avatar_medium: WebcastEventImage
    avatar_thumb: WebcastEventImage
    custom_verify: str
    enterprise_verify_reason: str
    verify_info: str
    verification_type: float
    follow_status: float
    follower_status: float
    language: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uid = self.uid

        short_id = self.short_id

        nickname = self.nickname

        signature = self.signature

        unique_id = self.unique_id

        sec_uid = self.sec_uid

        region = self.region

        avatar_larger = self.avatar_larger.to_dict()

        avatar_medium = self.avatar_medium.to_dict()

        avatar_thumb = self.avatar_thumb.to_dict()

        custom_verify = self.custom_verify

        enterprise_verify_reason = self.enterprise_verify_reason

        verify_info = self.verify_info

        verification_type = self.verification_type

        follow_status = self.follow_status

        follower_status = self.follower_status

        language = self.language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uid": uid,
                "short_id": short_id,
                "nickname": nickname,
                "signature": signature,
                "unique_id": unique_id,
                "sec_uid": sec_uid,
                "region": region,
                "avatar_larger": avatar_larger,
                "avatar_medium": avatar_medium,
                "avatar_thumb": avatar_thumb,
                "custom_verify": custom_verify,
                "enterprise_verify_reason": enterprise_verify_reason,
                "verify_info": verify_info,
                "verification_type": verification_type,
                "follow_status": follow_status,
                "follower_status": follower_status,
                "language": language,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_event_image import WebcastEventImage

        d = dict(src_dict)
        uid = d.pop("uid")

        short_id = d.pop("short_id")

        nickname = d.pop("nickname")

        signature = d.pop("signature")

        unique_id = d.pop("unique_id")

        sec_uid = d.pop("sec_uid")

        region = d.pop("region")

        avatar_larger = WebcastEventImage.from_dict(d.pop("avatar_larger"))

        avatar_medium = WebcastEventImage.from_dict(d.pop("avatar_medium"))

        avatar_thumb = WebcastEventImage.from_dict(d.pop("avatar_thumb"))

        custom_verify = d.pop("custom_verify")

        enterprise_verify_reason = d.pop("enterprise_verify_reason")

        verify_info = d.pop("verify_info")

        verification_type = d.pop("verification_type")

        follow_status = d.pop("follow_status")

        follower_status = d.pop("follower_status")

        language = d.pop("language")

        webcast_event_host = cls(
            uid=uid,
            short_id=short_id,
            nickname=nickname,
            signature=signature,
            unique_id=unique_id,
            sec_uid=sec_uid,
            region=region,
            avatar_larger=avatar_larger,
            avatar_medium=avatar_medium,
            avatar_thumb=avatar_thumb,
            custom_verify=custom_verify,
            enterprise_verify_reason=enterprise_verify_reason,
            verify_info=verify_info,
            verification_type=verification_type,
            follow_status=follow_status,
            follower_status=follower_status,
            language=language,
        )

        webcast_event_host.additional_properties = d
        return webcast_event_host

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tik_tok_user_info_by_id_follow_info import TikTokUserInfoByIdFollowInfo
    from ..models.tik_tok_user_info_by_id_image import TikTokUserInfoByIdImage


T = TypeVar("T", bound="TikTokUserInfoById")


@_attrs_define
class TikTokUserInfoById:
    """Cleaned user profile (deprecated/null/empty fields + author_stats removed). The listed fields are the stable, useful
    ones; the index signature covers the remaining non-empty fields TikTok returns.

        Attributes:
            id_str (str):
            display_id (str):
            nickname (str):
            sec_uid (str):
            bio_description (str):
            avatar_thumb (TikTokUserInfoByIdImage): Resolve a TikTok LIVE user's profile card from their numeric
                `target_uid` via the SIGNED `/webcast/user/` endpoint on `webcast.tiktokv.com`. Signed like a normal webcast
                route (ttwid + X-Bogus/X-Gnarly) and routed through the caller-provided proxy, but does NOT require a session
                id. The raw response carries a large `data` object riddled with `deprecated*` placeholders, `author_stats`, and
                null/empty fields; the route strips those out and returns the cleaned user under `user`.
            avatar_medium (TikTokUserInfoByIdImage): Resolve a TikTok LIVE user's profile card from their numeric
                `target_uid` via the SIGNED `/webcast/user/` endpoint on `webcast.tiktokv.com`. Signed like a normal webcast
                route (ttwid + X-Bogus/X-Gnarly) and routed through the caller-provided proxy, but does NOT require a session
                id. The raw response carries a large `data` object riddled with `deprecated*` placeholders, `author_stats`, and
                null/empty fields; the route strips those out and returns the cleaned user under `user`.
            avatar_large (TikTokUserInfoByIdImage): Resolve a TikTok LIVE user's profile card from their numeric
                `target_uid` via the SIGNED `/webcast/user/` endpoint on `webcast.tiktokv.com`. Signed like a normal webcast
                route (ttwid + X-Bogus/X-Gnarly) and routed through the caller-provided proxy, but does NOT require a session
                id. The raw response carries a large `data` object riddled with `deprecated*` placeholders, `author_stats`, and
                null/empty fields; the route strips those out and returns the cleaned user under `user`.
            follow_info (TikTokUserInfoByIdFollowInfo):
            verified (bool):
            create_time (float):
            modify_time (float):
            status (float):
    """

    id_str: str
    display_id: str
    nickname: str
    sec_uid: str
    bio_description: str
    avatar_thumb: TikTokUserInfoByIdImage
    avatar_medium: TikTokUserInfoByIdImage
    avatar_large: TikTokUserInfoByIdImage
    follow_info: TikTokUserInfoByIdFollowInfo
    verified: bool
    create_time: float
    modify_time: float
    status: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id_str = self.id_str

        display_id = self.display_id

        nickname = self.nickname

        sec_uid = self.sec_uid

        bio_description = self.bio_description

        avatar_thumb = self.avatar_thumb.to_dict()

        avatar_medium = self.avatar_medium.to_dict()

        avatar_large = self.avatar_large.to_dict()

        follow_info = self.follow_info.to_dict()

        verified = self.verified

        create_time = self.create_time

        modify_time = self.modify_time

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_str": id_str,
                "display_id": display_id,
                "nickname": nickname,
                "sec_uid": sec_uid,
                "bio_description": bio_description,
                "avatar_thumb": avatar_thumb,
                "avatar_medium": avatar_medium,
                "avatar_large": avatar_large,
                "follow_info": follow_info,
                "verified": verified,
                "create_time": create_time,
                "modify_time": modify_time,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tik_tok_user_info_by_id_follow_info import TikTokUserInfoByIdFollowInfo  # noqa: PLC0415
        from ..models.tik_tok_user_info_by_id_image import TikTokUserInfoByIdImage  # noqa: PLC0415

        d = dict(src_dict)
        id_str = d.pop("id_str")

        display_id = d.pop("display_id")

        nickname = d.pop("nickname")

        sec_uid = d.pop("sec_uid")

        bio_description = d.pop("bio_description")

        avatar_thumb = TikTokUserInfoByIdImage.from_dict(d.pop("avatar_thumb"))

        avatar_medium = TikTokUserInfoByIdImage.from_dict(d.pop("avatar_medium"))

        avatar_large = TikTokUserInfoByIdImage.from_dict(d.pop("avatar_large"))

        follow_info = TikTokUserInfoByIdFollowInfo.from_dict(d.pop("follow_info"))

        verified = d.pop("verified")

        create_time = d.pop("create_time")

        modify_time = d.pop("modify_time")

        status = d.pop("status")

        tik_tok_user_info_by_id = cls(
            id_str=id_str,
            display_id=display_id,
            nickname=nickname,
            sec_uid=sec_uid,
            bio_description=bio_description,
            avatar_thumb=avatar_thumb,
            avatar_medium=avatar_medium,
            avatar_large=avatar_large,
            follow_info=follow_info,
            verified=verified,
            create_time=create_time,
            modify_time=modify_time,
            status=status,
        )

        tik_tok_user_info_by_id.additional_properties = d
        return tik_tok_user_info_by_id

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

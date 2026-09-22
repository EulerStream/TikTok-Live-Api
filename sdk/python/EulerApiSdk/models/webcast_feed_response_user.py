from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webcast_feed_response_image import WebcastFeedResponseImage
    from ..models.webcast_feed_response_user_follow_info import WebcastFeedResponseUserFollowInfo
    from ..models.webcast_feed_response_user_own_room import WebcastFeedResponseUserOwnRoom
    from ..models.webcast_feed_response_user_pay_grade import WebcastFeedResponseUserPayGrade
    from ..models.webcast_feed_response_user_user_attr import WebcastFeedResponseUserUserAttr


T = TypeVar("T", bound="WebcastFeedResponseUser")


@_attrs_define
class WebcastFeedResponseUser:
    """
    Attributes:
        id (float):
        nickname (str):
        avatar_thumb (WebcastFeedResponseImage):
        avatar_medium (WebcastFeedResponseImage):
        avatar_large (WebcastFeedResponseImage):
        status (float):
        modify_time (float):
        follow_info (WebcastFeedResponseUserFollowInfo):
        pay_grade (WebcastFeedResponseUserPayGrade):
        user_attr (WebcastFeedResponseUserUserAttr):
        display_id (str):
        sec_uid (str):
        id_str (str):
        bio_description (str | Unset):
        own_room (WebcastFeedResponseUserOwnRoom | Unset):
    """

    id: float
    nickname: str
    avatar_thumb: WebcastFeedResponseImage
    avatar_medium: WebcastFeedResponseImage
    avatar_large: WebcastFeedResponseImage
    status: float
    modify_time: float
    follow_info: WebcastFeedResponseUserFollowInfo
    pay_grade: WebcastFeedResponseUserPayGrade
    user_attr: WebcastFeedResponseUserUserAttr
    display_id: str
    sec_uid: str
    id_str: str
    bio_description: str | Unset = UNSET
    own_room: WebcastFeedResponseUserOwnRoom | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        nickname = self.nickname

        avatar_thumb = self.avatar_thumb.to_dict()

        avatar_medium = self.avatar_medium.to_dict()

        avatar_large = self.avatar_large.to_dict()

        status = self.status

        modify_time = self.modify_time

        follow_info = self.follow_info.to_dict()

        pay_grade = self.pay_grade.to_dict()

        user_attr = self.user_attr.to_dict()

        display_id = self.display_id

        sec_uid = self.sec_uid

        id_str = self.id_str

        bio_description = self.bio_description

        own_room: dict[str, Any] | Unset = UNSET
        if not isinstance(self.own_room, Unset):
            own_room = self.own_room.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "nickname": nickname,
                "avatar_thumb": avatar_thumb,
                "avatar_medium": avatar_medium,
                "avatar_large": avatar_large,
                "status": status,
                "modify_time": modify_time,
                "follow_info": follow_info,
                "pay_grade": pay_grade,
                "user_attr": user_attr,
                "display_id": display_id,
                "sec_uid": sec_uid,
                "id_str": id_str,
            }
        )
        if bio_description is not UNSET:
            field_dict["bio_description"] = bio_description
        if own_room is not UNSET:
            field_dict["own_room"] = own_room

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_feed_response_image import WebcastFeedResponseImage  # noqa: PLC0415
        from ..models.webcast_feed_response_user_follow_info import WebcastFeedResponseUserFollowInfo  # noqa: PLC0415
        from ..models.webcast_feed_response_user_own_room import WebcastFeedResponseUserOwnRoom  # noqa: PLC0415
        from ..models.webcast_feed_response_user_pay_grade import WebcastFeedResponseUserPayGrade  # noqa: PLC0415
        from ..models.webcast_feed_response_user_user_attr import WebcastFeedResponseUserUserAttr  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        nickname = d.pop("nickname")

        avatar_thumb = WebcastFeedResponseImage.from_dict(d.pop("avatar_thumb"))

        avatar_medium = WebcastFeedResponseImage.from_dict(d.pop("avatar_medium"))

        avatar_large = WebcastFeedResponseImage.from_dict(d.pop("avatar_large"))

        status = d.pop("status")

        modify_time = d.pop("modify_time")

        follow_info = WebcastFeedResponseUserFollowInfo.from_dict(d.pop("follow_info"))

        pay_grade = WebcastFeedResponseUserPayGrade.from_dict(d.pop("pay_grade"))

        user_attr = WebcastFeedResponseUserUserAttr.from_dict(d.pop("user_attr"))

        display_id = d.pop("display_id")

        sec_uid = d.pop("sec_uid")

        id_str = d.pop("id_str")

        bio_description = d.pop("bio_description", UNSET)

        _own_room = d.pop("own_room", UNSET)
        own_room: WebcastFeedResponseUserOwnRoom | Unset
        if isinstance(_own_room, Unset):
            own_room = UNSET
        else:
            own_room = WebcastFeedResponseUserOwnRoom.from_dict(_own_room)

        webcast_feed_response_user = cls(
            id=id,
            nickname=nickname,
            avatar_thumb=avatar_thumb,
            avatar_medium=avatar_medium,
            avatar_large=avatar_large,
            status=status,
            modify_time=modify_time,
            follow_info=follow_info,
            pay_grade=pay_grade,
            user_attr=user_attr,
            display_id=display_id,
            sec_uid=sec_uid,
            id_str=id_str,
            bio_description=bio_description,
            own_room=own_room,
        )

        webcast_feed_response_user.additional_properties = d
        return webcast_feed_response_user

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

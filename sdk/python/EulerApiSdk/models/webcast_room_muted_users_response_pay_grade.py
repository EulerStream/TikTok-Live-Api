from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebcastRoomMutedUsersResponsePayGrade")


@_attrs_define
class WebcastRoomMutedUsersResponsePayGrade:
    """
    Attributes:
        deprecated20 (float):
        deprecated22 (float):
        deprecated23 (float):
        deprecated24 (float):
        deprecated25 (float):
        deprecated26 (float):
        grade_banner (str):
        grade_describe (str):
        grade_icon_list (list[Any]):
        level (float):
        name (str):
        next_name (str):
        next_privileges (str):
        score (float):
        screen_chat_type (float):
        upgrade_need_consume (float):
    """

    deprecated20: float
    deprecated22: float
    deprecated23: float
    deprecated24: float
    deprecated25: float
    deprecated26: float
    grade_banner: str
    grade_describe: str
    grade_icon_list: list[Any]
    level: float
    name: str
    next_name: str
    next_privileges: str
    score: float
    screen_chat_type: float
    upgrade_need_consume: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deprecated20 = self.deprecated20

        deprecated22 = self.deprecated22

        deprecated23 = self.deprecated23

        deprecated24 = self.deprecated24

        deprecated25 = self.deprecated25

        deprecated26 = self.deprecated26

        grade_banner = self.grade_banner

        grade_describe = self.grade_describe

        grade_icon_list = self.grade_icon_list

        level = self.level

        name = self.name

        next_name = self.next_name

        next_privileges = self.next_privileges

        score = self.score

        screen_chat_type = self.screen_chat_type

        upgrade_need_consume = self.upgrade_need_consume

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deprecated20": deprecated20,
                "deprecated22": deprecated22,
                "deprecated23": deprecated23,
                "deprecated24": deprecated24,
                "deprecated25": deprecated25,
                "deprecated26": deprecated26,
                "grade_banner": grade_banner,
                "grade_describe": grade_describe,
                "grade_icon_list": grade_icon_list,
                "level": level,
                "name": name,
                "next_name": next_name,
                "next_privileges": next_privileges,
                "score": score,
                "screen_chat_type": screen_chat_type,
                "upgrade_need_consume": upgrade_need_consume,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deprecated20 = d.pop("deprecated20")

        deprecated22 = d.pop("deprecated22")

        deprecated23 = d.pop("deprecated23")

        deprecated24 = d.pop("deprecated24")

        deprecated25 = d.pop("deprecated25")

        deprecated26 = d.pop("deprecated26")

        grade_banner = d.pop("grade_banner")

        grade_describe = d.pop("grade_describe")

        grade_icon_list = cast(list[Any], d.pop("grade_icon_list"))

        level = d.pop("level")

        name = d.pop("name")

        next_name = d.pop("next_name")

        next_privileges = d.pop("next_privileges")

        score = d.pop("score")

        screen_chat_type = d.pop("screen_chat_type")

        upgrade_need_consume = d.pop("upgrade_need_consume")

        webcast_room_muted_users_response_pay_grade = cls(
            deprecated20=deprecated20,
            deprecated22=deprecated22,
            deprecated23=deprecated23,
            deprecated24=deprecated24,
            deprecated25=deprecated25,
            deprecated26=deprecated26,
            grade_banner=grade_banner,
            grade_describe=grade_describe,
            grade_icon_list=grade_icon_list,
            level=level,
            name=name,
            next_name=next_name,
            next_privileges=next_privileges,
            score=score,
            screen_chat_type=screen_chat_type,
            upgrade_need_consume=upgrade_need_consume,
        )

        webcast_room_muted_users_response_pay_grade.additional_properties = d
        return webcast_room_muted_users_response_pay_grade

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

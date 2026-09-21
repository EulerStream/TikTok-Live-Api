from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetrieveBulkLiveCheckPayloadV1")


@_attrs_define
class RetrieveBulkLiveCheckPayloadV1:
    """
    Attributes:
        user_numeric_ids (list[str]):
        session_id (str | Unset):
        tt_target_idc (str | Unset):
    """

    user_numeric_ids: list[str]
    session_id: str | Unset = UNSET
    tt_target_idc: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_numeric_ids = self.user_numeric_ids

        session_id = self.session_id

        tt_target_idc = self.tt_target_idc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_numeric_ids": user_numeric_ids,
            }
        )
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if tt_target_idc is not UNSET:
            field_dict["tt_target_idc"] = tt_target_idc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_numeric_ids = cast(list[str], d.pop("user_numeric_ids"))

        session_id = d.pop("session_id", UNSET)

        tt_target_idc = d.pop("tt_target_idc", UNSET)

        retrieve_bulk_live_check_payload_v1 = cls(
            user_numeric_ids=user_numeric_ids,
            session_id=session_id,
            tt_target_idc=tt_target_idc,
        )

        retrieve_bulk_live_check_payload_v1.additional_properties = d
        return retrieve_bulk_live_check_payload_v1

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sign_tik_tok_url_body_method import SignTikTokUrlBodyMethod
from ..models.sign_tik_tok_url_body_type import SignTikTokUrlBodyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SignTikTokUrlBody")


@_attrs_define
class SignTikTokUrlBody:
    """
    Attributes:
        url (str):
        user_agent (str | Unset):
        method (SignTikTokUrlBodyMethod | Unset):
        session_id (str | Unset):
        tt_target_idc (str | Unset):
        ttwid (str | Unset):
        payload (str | Unset):
        type_ (SignTikTokUrlBodyType | Unset):
        include_browser_params (bool | Unset):
        include_verify_fp (bool | Unset):
    """

    url: str
    user_agent: str | Unset = UNSET
    method: SignTikTokUrlBodyMethod | Unset = UNSET
    session_id: str | Unset = UNSET
    tt_target_idc: str | Unset = UNSET
    ttwid: str | Unset = UNSET
    payload: str | Unset = UNSET
    type_: SignTikTokUrlBodyType | Unset = UNSET
    include_browser_params: bool | Unset = UNSET
    include_verify_fp: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        user_agent = self.user_agent

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        session_id = self.session_id

        tt_target_idc = self.tt_target_idc

        ttwid = self.ttwid

        payload = self.payload

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        include_browser_params = self.include_browser_params

        include_verify_fp = self.include_verify_fp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if user_agent is not UNSET:
            field_dict["userAgent"] = user_agent
        if method is not UNSET:
            field_dict["method"] = method
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if tt_target_idc is not UNSET:
            field_dict["ttTargetIdc"] = tt_target_idc
        if ttwid is not UNSET:
            field_dict["ttwid"] = ttwid
        if payload is not UNSET:
            field_dict["payload"] = payload
        if type_ is not UNSET:
            field_dict["type"] = type_
        if include_browser_params is not UNSET:
            field_dict["includeBrowserParams"] = include_browser_params
        if include_verify_fp is not UNSET:
            field_dict["includeVerifyFp"] = include_verify_fp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        user_agent = d.pop("userAgent", UNSET)

        _method = d.pop("method", UNSET)
        method: SignTikTokUrlBodyMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = SignTikTokUrlBodyMethod(_method)

        session_id = d.pop("sessionId", UNSET)

        tt_target_idc = d.pop("ttTargetIdc", UNSET)

        ttwid = d.pop("ttwid", UNSET)

        payload = d.pop("payload", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: SignTikTokUrlBodyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SignTikTokUrlBodyType(_type_)

        include_browser_params = d.pop("includeBrowserParams", UNSET)

        include_verify_fp = d.pop("includeVerifyFp", UNSET)

        sign_tik_tok_url_body = cls(
            url=url,
            user_agent=user_agent,
            method=method,
            session_id=session_id,
            tt_target_idc=tt_target_idc,
            ttwid=ttwid,
            payload=payload,
            type_=type_,
            include_browser_params=include_browser_params,
            include_verify_fp=include_verify_fp,
        )

        sign_tik_tok_url_body.additional_properties = d
        return sign_tik_tok_url_body

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.proxy_sign_result_cookies_item import ProxySignResultCookiesItem
    from ..models.proxy_sign_result_request_headers import ProxySignResultRequestHeaders
    from ..models.proxy_sign_result_tokens import ProxySignResultTokens


T = TypeVar("T", bound="ProxySignResult")


@_attrs_define
class ProxySignResult:
    """
    Attributes:
        signed_url (str | Unset):
        user_agent (str | Unset):
        browser_name (str | Unset):
        browser_version (str | Unset):
        tokens (ProxySignResultTokens | Unset):
        request_headers (ProxySignResultRequestHeaders | Unset):
        cookies (list[ProxySignResultCookiesItem] | Unset):
    """

    signed_url: str | Unset = UNSET
    user_agent: str | Unset = UNSET
    browser_name: str | Unset = UNSET
    browser_version: str | Unset = UNSET
    tokens: ProxySignResultTokens | Unset = UNSET
    request_headers: ProxySignResultRequestHeaders | Unset = UNSET
    cookies: list[ProxySignResultCookiesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signed_url = self.signed_url

        user_agent = self.user_agent

        browser_name = self.browser_name

        browser_version = self.browser_version

        tokens: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tokens, Unset):
            tokens = self.tokens.to_dict()

        request_headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request_headers, Unset):
            request_headers = self.request_headers.to_dict()

        cookies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cookies, Unset):
            cookies = []
            for cookies_item_data in self.cookies:
                cookies_item = cookies_item_data.to_dict()
                cookies.append(cookies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if signed_url is not UNSET:
            field_dict["signedUrl"] = signed_url
        if user_agent is not UNSET:
            field_dict["userAgent"] = user_agent
        if browser_name is not UNSET:
            field_dict["browserName"] = browser_name
        if browser_version is not UNSET:
            field_dict["browserVersion"] = browser_version
        if tokens is not UNSET:
            field_dict["tokens"] = tokens
        if request_headers is not UNSET:
            field_dict["requestHeaders"] = request_headers
        if cookies is not UNSET:
            field_dict["cookies"] = cookies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proxy_sign_result_cookies_item import ProxySignResultCookiesItem  # noqa: PLC0415
        from ..models.proxy_sign_result_request_headers import ProxySignResultRequestHeaders  # noqa: PLC0415
        from ..models.proxy_sign_result_tokens import ProxySignResultTokens  # noqa: PLC0415

        d = dict(src_dict)
        signed_url = d.pop("signedUrl", UNSET)

        user_agent = d.pop("userAgent", UNSET)

        browser_name = d.pop("browserName", UNSET)

        browser_version = d.pop("browserVersion", UNSET)

        _tokens = d.pop("tokens", UNSET)
        tokens: ProxySignResultTokens | Unset
        if isinstance(_tokens, Unset):
            tokens = UNSET
        else:
            tokens = ProxySignResultTokens.from_dict(_tokens)

        _request_headers = d.pop("requestHeaders", UNSET)
        request_headers: ProxySignResultRequestHeaders | Unset
        if isinstance(_request_headers, Unset):
            request_headers = UNSET
        else:
            request_headers = ProxySignResultRequestHeaders.from_dict(_request_headers)

        _cookies = d.pop("cookies", UNSET)
        cookies: list[ProxySignResultCookiesItem] | Unset = UNSET
        if _cookies is not UNSET:
            cookies = []
            for cookies_item_data in _cookies:
                cookies_item = ProxySignResultCookiesItem.from_dict(cookies_item_data)

                cookies.append(cookies_item)

        proxy_sign_result = cls(
            signed_url=signed_url,
            user_agent=user_agent,
            browser_name=browser_name,
            browser_version=browser_version,
            tokens=tokens,
            request_headers=request_headers,
            cookies=cookies,
        )

        proxy_sign_result.additional_properties = d
        return proxy_sign_result

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

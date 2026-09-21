from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TikTokUserInfoByIdImage")


@_attrs_define
class TikTokUserInfoByIdImage:
    """Resolve a TikTok LIVE user's profile card from their numeric `target_uid` via the SIGNED `/webcast/user/` endpoint
    on `webcast.tiktokv.com`. Signed like a normal webcast route (ttwid + X-Bogus/X-Gnarly) and routed through the
    caller-provided proxy, but does NOT require a session id. The raw response carries a large `data` object riddled
    with `deprecated*` placeholders, `author_stats`, and null/empty fields; the route strips those out and returns the
    cleaned user under `user`.

        Attributes:
            uri (str):
            url_list (list[str]):
    """

    uri: str
    url_list: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uri = self.uri

        url_list = self.url_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uri": uri,
                "url_list": url_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uri = d.pop("uri")

        url_list = cast(list[str], d.pop("url_list"))

        tik_tok_user_info_by_id_image = cls(
            uri=uri,
            url_list=url_list,
        )

        tik_tok_user_info_by_id_image.additional_properties = d
        return tik_tok_user_info_by_id_image

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

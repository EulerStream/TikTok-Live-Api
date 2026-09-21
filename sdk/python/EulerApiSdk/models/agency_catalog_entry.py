from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgencyCatalogEntry")


@_attrs_define
class AgencyCatalogEntry:
    """Public (snake_case) projection of a catalog agency row.

    Attributes:
        agency_id (float):
        name (str):
        languages (list[str]): 2-letter ISO-639-1 language codes.
        tags (list[str]): Category tags, e.g. "gaming", "talk_show".
        regions (list[str]): 2-letter ISO-3166-1 operating-region codes.
        claimed (bool): Whether a EulerStream account has claimed this agency.
        display_name (str | Unset):
        description_short (str | Unset):
        contact (str | Unset):
        website_url (str | Unset):
        recruitment_url (str | Unset):
        discord_url (str | Unset):
        tiktok_user_id (str | Unset): Numeric TikTok user id of the agency's linked creator (the "anchor").
        icon_image_url (str | Unset): Short-lived presigned image URLs — do not cache long-term.
        cover_image_url (str | Unset):
        created_at (str | Unset):
        updated_at (str | Unset):
    """

    agency_id: float
    name: str
    languages: list[str]
    tags: list[str]
    regions: list[str]
    claimed: bool
    display_name: str | Unset = UNSET
    description_short: str | Unset = UNSET
    contact: str | Unset = UNSET
    website_url: str | Unset = UNSET
    recruitment_url: str | Unset = UNSET
    discord_url: str | Unset = UNSET
    tiktok_user_id: str | Unset = UNSET
    icon_image_url: str | Unset = UNSET
    cover_image_url: str | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agency_id = self.agency_id

        name = self.name

        languages = self.languages

        tags = self.tags

        regions = self.regions

        claimed = self.claimed

        display_name = self.display_name

        description_short = self.description_short

        contact = self.contact

        website_url = self.website_url

        recruitment_url = self.recruitment_url

        discord_url = self.discord_url

        tiktok_user_id = self.tiktok_user_id

        icon_image_url = self.icon_image_url

        cover_image_url = self.cover_image_url

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agency_id": agency_id,
                "name": name,
                "languages": languages,
                "tags": tags,
                "regions": regions,
                "claimed": claimed,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if description_short is not UNSET:
            field_dict["description_short"] = description_short
        if contact is not UNSET:
            field_dict["contact"] = contact
        if website_url is not UNSET:
            field_dict["website_url"] = website_url
        if recruitment_url is not UNSET:
            field_dict["recruitment_url"] = recruitment_url
        if discord_url is not UNSET:
            field_dict["discord_url"] = discord_url
        if tiktok_user_id is not UNSET:
            field_dict["tiktok_user_id"] = tiktok_user_id
        if icon_image_url is not UNSET:
            field_dict["icon_image_url"] = icon_image_url
        if cover_image_url is not UNSET:
            field_dict["cover_image_url"] = cover_image_url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agency_id = d.pop("agency_id")

        name = d.pop("name")

        languages = cast(list[str], d.pop("languages"))

        tags = cast(list[str], d.pop("tags"))

        regions = cast(list[str], d.pop("regions"))

        claimed = d.pop("claimed")

        display_name = d.pop("display_name", UNSET)

        description_short = d.pop("description_short", UNSET)

        contact = d.pop("contact", UNSET)

        website_url = d.pop("website_url", UNSET)

        recruitment_url = d.pop("recruitment_url", UNSET)

        discord_url = d.pop("discord_url", UNSET)

        tiktok_user_id = d.pop("tiktok_user_id", UNSET)

        icon_image_url = d.pop("icon_image_url", UNSET)

        cover_image_url = d.pop("cover_image_url", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        agency_catalog_entry = cls(
            agency_id=agency_id,
            name=name,
            languages=languages,
            tags=tags,
            regions=regions,
            claimed=claimed,
            display_name=display_name,
            description_short=description_short,
            contact=contact,
            website_url=website_url,
            recruitment_url=recruitment_url,
            discord_url=discord_url,
            tiktok_user_id=tiktok_user_id,
            icon_image_url=icon_image_url,
            cover_image_url=cover_image_url,
            created_at=created_at,
            updated_at=updated_at,
        )

        agency_catalog_entry.additional_properties = d
        return agency_catalog_entry

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

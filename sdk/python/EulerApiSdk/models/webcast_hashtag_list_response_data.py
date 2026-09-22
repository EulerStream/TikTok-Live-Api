from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_hashtag_list_response_game_tag import WebcastHashtagListResponseGameTag
    from ..models.webcast_hashtag_list_response_hashtag import WebcastHashtagListResponseHashtag


T = TypeVar("T", bound="WebcastHashtagListResponseData")


@_attrs_define
class WebcastHashtagListResponseData:
    """
    Attributes:
        game_hashtag (WebcastHashtagListResponseHashtag):
        game_tag_list (list[WebcastHashtagListResponseGameTag]):
        hashtag (list[WebcastHashtagListResponseHashtag]):
        live_studio_hashtag (list[WebcastHashtagListResponseHashtag]):
        live_voice_hashtag (list[WebcastHashtagListResponseHashtag]):
        third_party_hashtag (list[WebcastHashtagListResponseHashtag]):
    """

    game_hashtag: WebcastHashtagListResponseHashtag
    game_tag_list: list[WebcastHashtagListResponseGameTag]
    hashtag: list[WebcastHashtagListResponseHashtag]
    live_studio_hashtag: list[WebcastHashtagListResponseHashtag]
    live_voice_hashtag: list[WebcastHashtagListResponseHashtag]
    third_party_hashtag: list[WebcastHashtagListResponseHashtag]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        game_hashtag = self.game_hashtag.to_dict()

        game_tag_list = []
        for game_tag_list_item_data in self.game_tag_list:
            game_tag_list_item = game_tag_list_item_data.to_dict()
            game_tag_list.append(game_tag_list_item)

        hashtag = []
        for hashtag_item_data in self.hashtag:
            hashtag_item = hashtag_item_data.to_dict()
            hashtag.append(hashtag_item)

        live_studio_hashtag = []
        for live_studio_hashtag_item_data in self.live_studio_hashtag:
            live_studio_hashtag_item = live_studio_hashtag_item_data.to_dict()
            live_studio_hashtag.append(live_studio_hashtag_item)

        live_voice_hashtag = []
        for live_voice_hashtag_item_data in self.live_voice_hashtag:
            live_voice_hashtag_item = live_voice_hashtag_item_data.to_dict()
            live_voice_hashtag.append(live_voice_hashtag_item)

        third_party_hashtag = []
        for third_party_hashtag_item_data in self.third_party_hashtag:
            third_party_hashtag_item = third_party_hashtag_item_data.to_dict()
            third_party_hashtag.append(third_party_hashtag_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "game_hashtag": game_hashtag,
                "game_tag_list": game_tag_list,
                "hashtag": hashtag,
                "live_studio_hashtag": live_studio_hashtag,
                "live_voice_hashtag": live_voice_hashtag,
                "third_party_hashtag": third_party_hashtag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_hashtag_list_response_game_tag import WebcastHashtagListResponseGameTag  # noqa: PLC0415
        from ..models.webcast_hashtag_list_response_hashtag import WebcastHashtagListResponseHashtag  # noqa: PLC0415

        d = dict(src_dict)
        game_hashtag = WebcastHashtagListResponseHashtag.from_dict(d.pop("game_hashtag"))

        game_tag_list = []
        _game_tag_list = d.pop("game_tag_list")
        for game_tag_list_item_data in _game_tag_list:
            game_tag_list_item = WebcastHashtagListResponseGameTag.from_dict(game_tag_list_item_data)

            game_tag_list.append(game_tag_list_item)

        hashtag = []
        _hashtag = d.pop("hashtag")
        for hashtag_item_data in _hashtag:
            hashtag_item = WebcastHashtagListResponseHashtag.from_dict(hashtag_item_data)

            hashtag.append(hashtag_item)

        live_studio_hashtag = []
        _live_studio_hashtag = d.pop("live_studio_hashtag")
        for live_studio_hashtag_item_data in _live_studio_hashtag:
            live_studio_hashtag_item = WebcastHashtagListResponseHashtag.from_dict(live_studio_hashtag_item_data)

            live_studio_hashtag.append(live_studio_hashtag_item)

        live_voice_hashtag = []
        _live_voice_hashtag = d.pop("live_voice_hashtag")
        for live_voice_hashtag_item_data in _live_voice_hashtag:
            live_voice_hashtag_item = WebcastHashtagListResponseHashtag.from_dict(live_voice_hashtag_item_data)

            live_voice_hashtag.append(live_voice_hashtag_item)

        third_party_hashtag = []
        _third_party_hashtag = d.pop("third_party_hashtag")
        for third_party_hashtag_item_data in _third_party_hashtag:
            third_party_hashtag_item = WebcastHashtagListResponseHashtag.from_dict(third_party_hashtag_item_data)

            third_party_hashtag.append(third_party_hashtag_item)

        webcast_hashtag_list_response_data = cls(
            game_hashtag=game_hashtag,
            game_tag_list=game_tag_list,
            hashtag=hashtag,
            live_studio_hashtag=live_studio_hashtag,
            live_voice_hashtag=live_voice_hashtag,
            third_party_hashtag=third_party_hashtag,
        )

        webcast_hashtag_list_response_data.additional_properties = d
        return webcast_hashtag_list_response_data

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

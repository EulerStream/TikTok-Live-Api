from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_room_add_sensitive_word_response_data_words_item import (
        WebcastRoomAddSensitiveWordResponseDataWordsItem,
    )


T = TypeVar("T", bound="WebcastRoomAddSensitiveWordResponseData")


@_attrs_define
class WebcastRoomAddSensitiveWordResponseData:
    """
    Attributes:
        words (list[WebcastRoomAddSensitiveWordResponseDataWordsItem]):
    """

    words: list[WebcastRoomAddSensitiveWordResponseDataWordsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        words = []
        for words_item_data in self.words:
            words_item = words_item_data.to_dict()
            words.append(words_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "words": words,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_room_add_sensitive_word_response_data_words_item import (
            WebcastRoomAddSensitiveWordResponseDataWordsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        words = []
        _words = d.pop("words")
        for words_item_data in _words:
            words_item = WebcastRoomAddSensitiveWordResponseDataWordsItem.from_dict(words_item_data)

            words.append(words_item)

        webcast_room_add_sensitive_word_response_data = cls(
            words=words,
        )

        webcast_room_add_sensitive_word_response_data.additional_properties = d
        return webcast_room_add_sensitive_word_response_data

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

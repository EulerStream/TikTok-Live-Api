from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_hashtag_list_response_image import WebcastHashtagListResponseImage


T = TypeVar("T", bound="WebcastHashtagListResponseHashtag")


@_attrs_define
class WebcastHashtagListResponseHashtag:
    """
    Attributes:
        id (float):
        image (WebcastHashtagListResponseImage):
        namespace (float):
        title (str):
    """

    id: float
    image: WebcastHashtagListResponseImage
    namespace: float
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        image = self.image.to_dict()

        namespace = self.namespace

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "image": image,
                "namespace": namespace,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_hashtag_list_response_image import WebcastHashtagListResponseImage

        d = dict(src_dict)
        id = d.pop("id")

        image = WebcastHashtagListResponseImage.from_dict(d.pop("image"))

        namespace = d.pop("namespace")

        title = d.pop("title")

        webcast_hashtag_list_response_hashtag = cls(
            id=id,
            image=image,
            namespace=namespace,
            title=title,
        )

        webcast_hashtag_list_response_hashtag.additional_properties = d
        return webcast_hashtag_list_response_hashtag

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

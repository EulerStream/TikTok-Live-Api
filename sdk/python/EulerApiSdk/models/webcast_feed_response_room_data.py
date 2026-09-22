from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webcast_feed_response_hashtag import WebcastFeedResponseHashtag
    from ..models.webcast_feed_response_image import WebcastFeedResponseImage
    from ..models.webcast_feed_response_room_data_blurred_cover import WebcastFeedResponseRoomDataBlurredCover
    from ..models.webcast_feed_response_room_data_commerce_info import WebcastFeedResponseRoomDataCommerceInfo
    from ..models.webcast_feed_response_room_data_feed_room_label import WebcastFeedResponseRoomDataFeedRoomLabel
    from ..models.webcast_feed_response_room_data_game_tag_detail import WebcastFeedResponseRoomDataGameTagDetail
    from ..models.webcast_feed_response_room_data_multi_stream_url import WebcastFeedResponseRoomDataMultiStreamUrl
    from ..models.webcast_feed_response_room_data_rectangle_cover_img import (
        WebcastFeedResponseRoomDataRectangleCoverImg,
    )
    from ..models.webcast_feed_response_room_data_room_auth import WebcastFeedResponseRoomDataRoomAuth
    from ..models.webcast_feed_response_room_data_square_cover_img import WebcastFeedResponseRoomDataSquareCoverImg
    from ..models.webcast_feed_response_room_data_stats import WebcastFeedResponseRoomDataStats
    from ..models.webcast_feed_response_room_data_stream_url_filtered_info import (
        WebcastFeedResponseRoomDataStreamUrlFilteredInfo,
    )
    from ..models.webcast_feed_response_room_data_taxonomy_tag_info import WebcastFeedResponseRoomDataTaxonomyTagInfo
    from ..models.webcast_feed_response_stream_url import WebcastFeedResponseStreamUrl
    from ..models.webcast_feed_response_user import WebcastFeedResponseUser


T = TypeVar("T", bound="WebcastFeedResponseRoomData")


@_attrs_define
class WebcastFeedResponseRoomData:
    """
    Attributes:
        id (float):
        id_str (str):
        status (float):
        owner_user_id (float):
        title (str):
        user_count (float):
        client_version (float):
        cover (WebcastFeedResponseImage):
        stream_url (WebcastFeedResponseStreamUrl):
        stats (WebcastFeedResponseRoomDataStats):
        feed_room_label (WebcastFeedResponseRoomDataFeedRoomLabel):
        owner (WebcastFeedResponseUser):
        room_auth (WebcastFeedResponseRoomDataRoomAuth):
        anchor_tab_type (float):
        commerce_info (WebcastFeedResponseRoomDataCommerceInfo):
        stream_url_filtered_info (WebcastFeedResponseRoomDataStreamUrlFilteredInfo):
        blurred_cover (WebcastFeedResponseRoomDataBlurredCover):
        multi_stream_url (WebcastFeedResponseRoomDataMultiStreamUrl):
        live_type_third_party (bool | Unset):
        like_count (float | Unset):
        hashtag (WebcastFeedResponseHashtag | Unset):
        live_room_mode (float | Unset):
        square_cover_img (WebcastFeedResponseRoomDataSquareCoverImg | Unset):
        rectangle_cover_img (WebcastFeedResponseRoomDataRectangleCoverImg | Unset):
        game_tag_detail (WebcastFeedResponseRoomDataGameTagDetail | Unset):
        taxonomy_tag_info (WebcastFeedResponseRoomDataTaxonomyTagInfo | Unset):
    """

    id: float
    id_str: str
    status: float
    owner_user_id: float
    title: str
    user_count: float
    client_version: float
    cover: WebcastFeedResponseImage
    stream_url: WebcastFeedResponseStreamUrl
    stats: WebcastFeedResponseRoomDataStats
    feed_room_label: WebcastFeedResponseRoomDataFeedRoomLabel
    owner: WebcastFeedResponseUser
    room_auth: WebcastFeedResponseRoomDataRoomAuth
    anchor_tab_type: float
    commerce_info: WebcastFeedResponseRoomDataCommerceInfo
    stream_url_filtered_info: WebcastFeedResponseRoomDataStreamUrlFilteredInfo
    blurred_cover: WebcastFeedResponseRoomDataBlurredCover
    multi_stream_url: WebcastFeedResponseRoomDataMultiStreamUrl
    live_type_third_party: bool | Unset = UNSET
    like_count: float | Unset = UNSET
    hashtag: WebcastFeedResponseHashtag | Unset = UNSET
    live_room_mode: float | Unset = UNSET
    square_cover_img: WebcastFeedResponseRoomDataSquareCoverImg | Unset = UNSET
    rectangle_cover_img: WebcastFeedResponseRoomDataRectangleCoverImg | Unset = UNSET
    game_tag_detail: WebcastFeedResponseRoomDataGameTagDetail | Unset = UNSET
    taxonomy_tag_info: WebcastFeedResponseRoomDataTaxonomyTagInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        id_str = self.id_str

        status = self.status

        owner_user_id = self.owner_user_id

        title = self.title

        user_count = self.user_count

        client_version = self.client_version

        cover = self.cover.to_dict()

        stream_url = self.stream_url.to_dict()

        stats = self.stats.to_dict()

        feed_room_label = self.feed_room_label.to_dict()

        owner = self.owner.to_dict()

        room_auth = self.room_auth.to_dict()

        anchor_tab_type = self.anchor_tab_type

        commerce_info = self.commerce_info.to_dict()

        stream_url_filtered_info = self.stream_url_filtered_info.to_dict()

        blurred_cover = self.blurred_cover.to_dict()

        multi_stream_url = self.multi_stream_url.to_dict()

        live_type_third_party = self.live_type_third_party

        like_count = self.like_count

        hashtag: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hashtag, Unset):
            hashtag = self.hashtag.to_dict()

        live_room_mode = self.live_room_mode

        square_cover_img: dict[str, Any] | Unset = UNSET
        if not isinstance(self.square_cover_img, Unset):
            square_cover_img = self.square_cover_img.to_dict()

        rectangle_cover_img: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rectangle_cover_img, Unset):
            rectangle_cover_img = self.rectangle_cover_img.to_dict()

        game_tag_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.game_tag_detail, Unset):
            game_tag_detail = self.game_tag_detail.to_dict()

        taxonomy_tag_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.taxonomy_tag_info, Unset):
            taxonomy_tag_info = self.taxonomy_tag_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "id_str": id_str,
                "status": status,
                "owner_user_id": owner_user_id,
                "title": title,
                "user_count": user_count,
                "client_version": client_version,
                "cover": cover,
                "stream_url": stream_url,
                "stats": stats,
                "feed_room_label": feed_room_label,
                "owner": owner,
                "room_auth": room_auth,
                "anchor_tab_type": anchor_tab_type,
                "commerce_info": commerce_info,
                "stream_url_filtered_info": stream_url_filtered_info,
                "blurred_cover": blurred_cover,
                "multi_stream_url": multi_stream_url,
            }
        )
        if live_type_third_party is not UNSET:
            field_dict["live_type_third_party"] = live_type_third_party
        if like_count is not UNSET:
            field_dict["like_count"] = like_count
        if hashtag is not UNSET:
            field_dict["hashtag"] = hashtag
        if live_room_mode is not UNSET:
            field_dict["live_room_mode"] = live_room_mode
        if square_cover_img is not UNSET:
            field_dict["square_cover_img"] = square_cover_img
        if rectangle_cover_img is not UNSET:
            field_dict["rectangle_cover_img"] = rectangle_cover_img
        if game_tag_detail is not UNSET:
            field_dict["game_tag_detail"] = game_tag_detail
        if taxonomy_tag_info is not UNSET:
            field_dict["taxonomy_tag_info"] = taxonomy_tag_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_feed_response_hashtag import WebcastFeedResponseHashtag  # noqa: PLC0415
        from ..models.webcast_feed_response_image import WebcastFeedResponseImage  # noqa: PLC0415
        from ..models.webcast_feed_response_room_data_blurred_cover import (
            WebcastFeedResponseRoomDataBlurredCover,  # noqa: PLC0415
        )
        from ..models.webcast_feed_response_room_data_commerce_info import (
            WebcastFeedResponseRoomDataCommerceInfo,  # noqa: PLC0415
        )
        from ..models.webcast_feed_response_room_data_feed_room_label import (
            WebcastFeedResponseRoomDataFeedRoomLabel,  # noqa: PLC0415
        )
        from ..models.webcast_feed_response_room_data_game_tag_detail import (
            WebcastFeedResponseRoomDataGameTagDetail,  # noqa: PLC0415
        )
        from ..models.webcast_feed_response_room_data_multi_stream_url import (
            WebcastFeedResponseRoomDataMultiStreamUrl,  # noqa: PLC0415
        )
        from ..models.webcast_feed_response_room_data_rectangle_cover_img import (
            WebcastFeedResponseRoomDataRectangleCoverImg,  # noqa: PLC0415
        )
        from ..models.webcast_feed_response_room_data_room_auth import (
            WebcastFeedResponseRoomDataRoomAuth,  # noqa: PLC0415
        )
        from ..models.webcast_feed_response_room_data_square_cover_img import (
            WebcastFeedResponseRoomDataSquareCoverImg,  # noqa: PLC0415
        )
        from ..models.webcast_feed_response_room_data_stats import WebcastFeedResponseRoomDataStats  # noqa: PLC0415
        from ..models.webcast_feed_response_room_data_stream_url_filtered_info import (
            WebcastFeedResponseRoomDataStreamUrlFilteredInfo,  # noqa: PLC0415
        )
        from ..models.webcast_feed_response_room_data_taxonomy_tag_info import (
            WebcastFeedResponseRoomDataTaxonomyTagInfo,  # noqa: PLC0415
        )
        from ..models.webcast_feed_response_stream_url import WebcastFeedResponseStreamUrl  # noqa: PLC0415
        from ..models.webcast_feed_response_user import WebcastFeedResponseUser  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        id_str = d.pop("id_str")

        status = d.pop("status")

        owner_user_id = d.pop("owner_user_id")

        title = d.pop("title")

        user_count = d.pop("user_count")

        client_version = d.pop("client_version")

        cover = WebcastFeedResponseImage.from_dict(d.pop("cover"))

        stream_url = WebcastFeedResponseStreamUrl.from_dict(d.pop("stream_url"))

        stats = WebcastFeedResponseRoomDataStats.from_dict(d.pop("stats"))

        feed_room_label = WebcastFeedResponseRoomDataFeedRoomLabel.from_dict(d.pop("feed_room_label"))

        owner = WebcastFeedResponseUser.from_dict(d.pop("owner"))

        room_auth = WebcastFeedResponseRoomDataRoomAuth.from_dict(d.pop("room_auth"))

        anchor_tab_type = d.pop("anchor_tab_type")

        commerce_info = WebcastFeedResponseRoomDataCommerceInfo.from_dict(d.pop("commerce_info"))

        stream_url_filtered_info = WebcastFeedResponseRoomDataStreamUrlFilteredInfo.from_dict(
            d.pop("stream_url_filtered_info")
        )

        blurred_cover = WebcastFeedResponseRoomDataBlurredCover.from_dict(d.pop("blurred_cover"))

        multi_stream_url = WebcastFeedResponseRoomDataMultiStreamUrl.from_dict(d.pop("multi_stream_url"))

        live_type_third_party = d.pop("live_type_third_party", UNSET)

        like_count = d.pop("like_count", UNSET)

        _hashtag = d.pop("hashtag", UNSET)
        hashtag: WebcastFeedResponseHashtag | Unset
        if isinstance(_hashtag, Unset):
            hashtag = UNSET
        else:
            hashtag = WebcastFeedResponseHashtag.from_dict(_hashtag)

        live_room_mode = d.pop("live_room_mode", UNSET)

        _square_cover_img = d.pop("square_cover_img", UNSET)
        square_cover_img: WebcastFeedResponseRoomDataSquareCoverImg | Unset
        if isinstance(_square_cover_img, Unset):
            square_cover_img = UNSET
        else:
            square_cover_img = WebcastFeedResponseRoomDataSquareCoverImg.from_dict(_square_cover_img)

        _rectangle_cover_img = d.pop("rectangle_cover_img", UNSET)
        rectangle_cover_img: WebcastFeedResponseRoomDataRectangleCoverImg | Unset
        if isinstance(_rectangle_cover_img, Unset):
            rectangle_cover_img = UNSET
        else:
            rectangle_cover_img = WebcastFeedResponseRoomDataRectangleCoverImg.from_dict(_rectangle_cover_img)

        _game_tag_detail = d.pop("game_tag_detail", UNSET)
        game_tag_detail: WebcastFeedResponseRoomDataGameTagDetail | Unset
        if isinstance(_game_tag_detail, Unset):
            game_tag_detail = UNSET
        else:
            game_tag_detail = WebcastFeedResponseRoomDataGameTagDetail.from_dict(_game_tag_detail)

        _taxonomy_tag_info = d.pop("taxonomy_tag_info", UNSET)
        taxonomy_tag_info: WebcastFeedResponseRoomDataTaxonomyTagInfo | Unset
        if isinstance(_taxonomy_tag_info, Unset):
            taxonomy_tag_info = UNSET
        else:
            taxonomy_tag_info = WebcastFeedResponseRoomDataTaxonomyTagInfo.from_dict(_taxonomy_tag_info)

        webcast_feed_response_room_data = cls(
            id=id,
            id_str=id_str,
            status=status,
            owner_user_id=owner_user_id,
            title=title,
            user_count=user_count,
            client_version=client_version,
            cover=cover,
            stream_url=stream_url,
            stats=stats,
            feed_room_label=feed_room_label,
            owner=owner,
            room_auth=room_auth,
            anchor_tab_type=anchor_tab_type,
            commerce_info=commerce_info,
            stream_url_filtered_info=stream_url_filtered_info,
            blurred_cover=blurred_cover,
            multi_stream_url=multi_stream_url,
            live_type_third_party=live_type_third_party,
            like_count=like_count,
            hashtag=hashtag,
            live_room_mode=live_room_mode,
            square_cover_img=square_cover_img,
            rectangle_cover_img=rectangle_cover_img,
            game_tag_detail=game_tag_detail,
            taxonomy_tag_info=taxonomy_tag_info,
        )

        webcast_feed_response_room_data.additional_properties = d
        return webcast_feed_response_room_data

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

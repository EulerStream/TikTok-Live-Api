from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webcast_live_analytics_user_interactions_response_enigma_info import (
        WebcastLiveAnalyticsUserInteractionsResponseEnigmaInfo,
    )
    from ..models.webcast_live_analytics_user_interactions_response_image import (
        WebcastLiveAnalyticsUserInteractionsResponseImage,
    )
    from ..models.webcast_live_analytics_user_interactions_response_pay_grade import (
        WebcastLiveAnalyticsUserInteractionsResponsePayGrade,
    )
    from ..models.webcast_live_analytics_user_interactions_response_user_attr import (
        WebcastLiveAnalyticsUserInteractionsResponseUserAttr,
    )


T = TypeVar("T", bound="WebcastLiveAnalyticsUserInteractionsResponseUser")


@_attrs_define
class WebcastLiveAnalyticsUserInteractionsResponseUser:
    """
    Attributes:
        allow_find_by_contacts (bool):
        allow_others_download_video (bool):
        allow_others_download_when_sharing_video (bool):
        allow_share_show_profile (bool):
        allow_show_in_gossip (bool):
        allow_show_my_action (bool):
        allow_strange_comment (bool):
        allow_unfollower_comment (bool):
        allow_use_linkmic (bool):
        avatar_thumb (WebcastLiveAnalyticsUserInteractionsResponseImage):
        badge_image_list (list[Any]):
        badge_list (list[Any]):
        bg_img_url (str):
        bio_description (str):
        block_status (float):
        border_list (list[Any]):
        comment_restrict (float):
        commerce_webcast_config_ids (list[Any]):
        constellation (str):
        create_time (float):
        disable_ichat (float):
        display_id (str):
        enable_ichat_img (float):
        enigma_info (WebcastLiveAnalyticsUserInteractionsResponseEnigmaInfo):
        exp (float):
        fan_ticket_count (float):
        fold_stranger_chat (bool):
        follow_status (float):
        ichat_restrict_type (float):
        id (float):
        id_str (str):
        is_anchor_marked (bool):
        is_block (bool):
        is_follower (bool):
        is_following (bool):
        is_subscribe (bool):
        link_mic_stats (float):
        media_badge_image_list (list[Any]):
        mint_type_label (list[Any]):
        modify_time (float):
        need_profile_guide (bool):
        new_real_time_icons (list[Any]):
        nickname (str):
        pay_grade (WebcastLiveAnalyticsUserInteractionsResponsePayGrade):
        pay_score (float):
        pay_scores (float):
        push_comment_status (bool):
        push_digg (bool):
        push_follow (bool):
        push_friend_action (bool):
        push_ichat (bool):
        push_status (bool):
        push_video_post (bool):
        push_video_recommend (bool):
        real_time_icons (list[Any]):
        scm_label (str):
        sec_uid (str):
        secret (float):
        share_qrcode_uri (str):
        special_id (str):
        status (float):
        ticket_count (float):
        top_fans (list[Any]):
        top_vip_no (float):
        upcoming_event_list (list[Any]):
        user_attr (WebcastLiveAnalyticsUserInteractionsResponseUserAttr):
        user_role (float):
        verified (bool):
        verified_content (str):
        verified_reason (str):
        with_car_management_permission (bool):
        with_commerce_permission (bool):
        with_fusion_shop_entry (bool):
    """

    allow_find_by_contacts: bool
    allow_others_download_video: bool
    allow_others_download_when_sharing_video: bool
    allow_share_show_profile: bool
    allow_show_in_gossip: bool
    allow_show_my_action: bool
    allow_strange_comment: bool
    allow_unfollower_comment: bool
    allow_use_linkmic: bool
    avatar_thumb: WebcastLiveAnalyticsUserInteractionsResponseImage
    badge_image_list: list[Any]
    badge_list: list[Any]
    bg_img_url: str
    bio_description: str
    block_status: float
    border_list: list[Any]
    comment_restrict: float
    commerce_webcast_config_ids: list[Any]
    constellation: str
    create_time: float
    disable_ichat: float
    display_id: str
    enable_ichat_img: float
    enigma_info: WebcastLiveAnalyticsUserInteractionsResponseEnigmaInfo
    exp: float
    fan_ticket_count: float
    fold_stranger_chat: bool
    follow_status: float
    ichat_restrict_type: float
    id: float
    id_str: str
    is_anchor_marked: bool
    is_block: bool
    is_follower: bool
    is_following: bool
    is_subscribe: bool
    link_mic_stats: float
    media_badge_image_list: list[Any]
    mint_type_label: list[Any]
    modify_time: float
    need_profile_guide: bool
    new_real_time_icons: list[Any]
    nickname: str
    pay_grade: WebcastLiveAnalyticsUserInteractionsResponsePayGrade
    pay_score: float
    pay_scores: float
    push_comment_status: bool
    push_digg: bool
    push_follow: bool
    push_friend_action: bool
    push_ichat: bool
    push_status: bool
    push_video_post: bool
    push_video_recommend: bool
    real_time_icons: list[Any]
    scm_label: str
    sec_uid: str
    secret: float
    share_qrcode_uri: str
    special_id: str
    status: float
    ticket_count: float
    top_fans: list[Any]
    top_vip_no: float
    upcoming_event_list: list[Any]
    user_attr: WebcastLiveAnalyticsUserInteractionsResponseUserAttr
    user_role: float
    verified: bool
    verified_content: str
    verified_reason: str
    with_car_management_permission: bool
    with_commerce_permission: bool
    with_fusion_shop_entry: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_find_by_contacts = self.allow_find_by_contacts

        allow_others_download_video = self.allow_others_download_video

        allow_others_download_when_sharing_video = self.allow_others_download_when_sharing_video

        allow_share_show_profile = self.allow_share_show_profile

        allow_show_in_gossip = self.allow_show_in_gossip

        allow_show_my_action = self.allow_show_my_action

        allow_strange_comment = self.allow_strange_comment

        allow_unfollower_comment = self.allow_unfollower_comment

        allow_use_linkmic = self.allow_use_linkmic

        avatar_thumb = self.avatar_thumb.to_dict()

        badge_image_list = self.badge_image_list

        badge_list = self.badge_list

        bg_img_url = self.bg_img_url

        bio_description = self.bio_description

        block_status = self.block_status

        border_list = self.border_list

        comment_restrict = self.comment_restrict

        commerce_webcast_config_ids = self.commerce_webcast_config_ids

        constellation = self.constellation

        create_time = self.create_time

        disable_ichat = self.disable_ichat

        display_id = self.display_id

        enable_ichat_img = self.enable_ichat_img

        enigma_info = self.enigma_info.to_dict()

        exp = self.exp

        fan_ticket_count = self.fan_ticket_count

        fold_stranger_chat = self.fold_stranger_chat

        follow_status = self.follow_status

        ichat_restrict_type = self.ichat_restrict_type

        id = self.id

        id_str = self.id_str

        is_anchor_marked = self.is_anchor_marked

        is_block = self.is_block

        is_follower = self.is_follower

        is_following = self.is_following

        is_subscribe = self.is_subscribe

        link_mic_stats = self.link_mic_stats

        media_badge_image_list = self.media_badge_image_list

        mint_type_label = self.mint_type_label

        modify_time = self.modify_time

        need_profile_guide = self.need_profile_guide

        new_real_time_icons = self.new_real_time_icons

        nickname = self.nickname

        pay_grade = self.pay_grade.to_dict()

        pay_score = self.pay_score

        pay_scores = self.pay_scores

        push_comment_status = self.push_comment_status

        push_digg = self.push_digg

        push_follow = self.push_follow

        push_friend_action = self.push_friend_action

        push_ichat = self.push_ichat

        push_status = self.push_status

        push_video_post = self.push_video_post

        push_video_recommend = self.push_video_recommend

        real_time_icons = self.real_time_icons

        scm_label = self.scm_label

        sec_uid = self.sec_uid

        secret = self.secret

        share_qrcode_uri = self.share_qrcode_uri

        special_id = self.special_id

        status = self.status

        ticket_count = self.ticket_count

        top_fans = self.top_fans

        top_vip_no = self.top_vip_no

        upcoming_event_list = self.upcoming_event_list

        user_attr = self.user_attr.to_dict()

        user_role = self.user_role

        verified = self.verified

        verified_content = self.verified_content

        verified_reason = self.verified_reason

        with_car_management_permission = self.with_car_management_permission

        with_commerce_permission = self.with_commerce_permission

        with_fusion_shop_entry = self.with_fusion_shop_entry

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allow_find_by_contacts": allow_find_by_contacts,
                "allow_others_download_video": allow_others_download_video,
                "allow_others_download_when_sharing_video": allow_others_download_when_sharing_video,
                "allow_share_show_profile": allow_share_show_profile,
                "allow_show_in_gossip": allow_show_in_gossip,
                "allow_show_my_action": allow_show_my_action,
                "allow_strange_comment": allow_strange_comment,
                "allow_unfollower_comment": allow_unfollower_comment,
                "allow_use_linkmic": allow_use_linkmic,
                "avatar_thumb": avatar_thumb,
                "badge_image_list": badge_image_list,
                "badge_list": badge_list,
                "bg_img_url": bg_img_url,
                "bio_description": bio_description,
                "block_status": block_status,
                "border_list": border_list,
                "comment_restrict": comment_restrict,
                "commerce_webcast_config_ids": commerce_webcast_config_ids,
                "constellation": constellation,
                "create_time": create_time,
                "disable_ichat": disable_ichat,
                "display_id": display_id,
                "enable_ichat_img": enable_ichat_img,
                "enigma_info": enigma_info,
                "exp": exp,
                "fan_ticket_count": fan_ticket_count,
                "fold_stranger_chat": fold_stranger_chat,
                "follow_status": follow_status,
                "ichat_restrict_type": ichat_restrict_type,
                "id": id,
                "id_str": id_str,
                "is_anchor_marked": is_anchor_marked,
                "is_block": is_block,
                "is_follower": is_follower,
                "is_following": is_following,
                "is_subscribe": is_subscribe,
                "link_mic_stats": link_mic_stats,
                "media_badge_image_list": media_badge_image_list,
                "mint_type_label": mint_type_label,
                "modify_time": modify_time,
                "need_profile_guide": need_profile_guide,
                "new_real_time_icons": new_real_time_icons,
                "nickname": nickname,
                "pay_grade": pay_grade,
                "pay_score": pay_score,
                "pay_scores": pay_scores,
                "push_comment_status": push_comment_status,
                "push_digg": push_digg,
                "push_follow": push_follow,
                "push_friend_action": push_friend_action,
                "push_ichat": push_ichat,
                "push_status": push_status,
                "push_video_post": push_video_post,
                "push_video_recommend": push_video_recommend,
                "real_time_icons": real_time_icons,
                "scm_label": scm_label,
                "sec_uid": sec_uid,
                "secret": secret,
                "share_qrcode_uri": share_qrcode_uri,
                "special_id": special_id,
                "status": status,
                "ticket_count": ticket_count,
                "top_fans": top_fans,
                "top_vip_no": top_vip_no,
                "upcoming_event_list": upcoming_event_list,
                "user_attr": user_attr,
                "user_role": user_role,
                "verified": verified,
                "verified_content": verified_content,
                "verified_reason": verified_reason,
                "with_car_management_permission": with_car_management_permission,
                "with_commerce_permission": with_commerce_permission,
                "with_fusion_shop_entry": with_fusion_shop_entry,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webcast_live_analytics_user_interactions_response_enigma_info import (
            WebcastLiveAnalyticsUserInteractionsResponseEnigmaInfo,  # noqa: PLC0415
        )
        from ..models.webcast_live_analytics_user_interactions_response_image import (
            WebcastLiveAnalyticsUserInteractionsResponseImage,  # noqa: PLC0415
        )
        from ..models.webcast_live_analytics_user_interactions_response_pay_grade import (
            WebcastLiveAnalyticsUserInteractionsResponsePayGrade,  # noqa: PLC0415
        )
        from ..models.webcast_live_analytics_user_interactions_response_user_attr import (
            WebcastLiveAnalyticsUserInteractionsResponseUserAttr,  # noqa: PLC0415
        )

        d = dict(src_dict)
        allow_find_by_contacts = d.pop("allow_find_by_contacts")

        allow_others_download_video = d.pop("allow_others_download_video")

        allow_others_download_when_sharing_video = d.pop("allow_others_download_when_sharing_video")

        allow_share_show_profile = d.pop("allow_share_show_profile")

        allow_show_in_gossip = d.pop("allow_show_in_gossip")

        allow_show_my_action = d.pop("allow_show_my_action")

        allow_strange_comment = d.pop("allow_strange_comment")

        allow_unfollower_comment = d.pop("allow_unfollower_comment")

        allow_use_linkmic = d.pop("allow_use_linkmic")

        avatar_thumb = WebcastLiveAnalyticsUserInteractionsResponseImage.from_dict(d.pop("avatar_thumb"))

        badge_image_list = cast(list[Any], d.pop("badge_image_list"))

        badge_list = cast(list[Any], d.pop("badge_list"))

        bg_img_url = d.pop("bg_img_url")

        bio_description = d.pop("bio_description")

        block_status = d.pop("block_status")

        border_list = cast(list[Any], d.pop("border_list"))

        comment_restrict = d.pop("comment_restrict")

        commerce_webcast_config_ids = cast(list[Any], d.pop("commerce_webcast_config_ids"))

        constellation = d.pop("constellation")

        create_time = d.pop("create_time")

        disable_ichat = d.pop("disable_ichat")

        display_id = d.pop("display_id")

        enable_ichat_img = d.pop("enable_ichat_img")

        enigma_info = WebcastLiveAnalyticsUserInteractionsResponseEnigmaInfo.from_dict(d.pop("enigma_info"))

        exp = d.pop("exp")

        fan_ticket_count = d.pop("fan_ticket_count")

        fold_stranger_chat = d.pop("fold_stranger_chat")

        follow_status = d.pop("follow_status")

        ichat_restrict_type = d.pop("ichat_restrict_type")

        id = d.pop("id")

        id_str = d.pop("id_str")

        is_anchor_marked = d.pop("is_anchor_marked")

        is_block = d.pop("is_block")

        is_follower = d.pop("is_follower")

        is_following = d.pop("is_following")

        is_subscribe = d.pop("is_subscribe")

        link_mic_stats = d.pop("link_mic_stats")

        media_badge_image_list = cast(list[Any], d.pop("media_badge_image_list"))

        mint_type_label = cast(list[Any], d.pop("mint_type_label"))

        modify_time = d.pop("modify_time")

        need_profile_guide = d.pop("need_profile_guide")

        new_real_time_icons = cast(list[Any], d.pop("new_real_time_icons"))

        nickname = d.pop("nickname")

        pay_grade = WebcastLiveAnalyticsUserInteractionsResponsePayGrade.from_dict(d.pop("pay_grade"))

        pay_score = d.pop("pay_score")

        pay_scores = d.pop("pay_scores")

        push_comment_status = d.pop("push_comment_status")

        push_digg = d.pop("push_digg")

        push_follow = d.pop("push_follow")

        push_friend_action = d.pop("push_friend_action")

        push_ichat = d.pop("push_ichat")

        push_status = d.pop("push_status")

        push_video_post = d.pop("push_video_post")

        push_video_recommend = d.pop("push_video_recommend")

        real_time_icons = cast(list[Any], d.pop("real_time_icons"))

        scm_label = d.pop("scm_label")

        sec_uid = d.pop("sec_uid")

        secret = d.pop("secret")

        share_qrcode_uri = d.pop("share_qrcode_uri")

        special_id = d.pop("special_id")

        status = d.pop("status")

        ticket_count = d.pop("ticket_count")

        top_fans = cast(list[Any], d.pop("top_fans"))

        top_vip_no = d.pop("top_vip_no")

        upcoming_event_list = cast(list[Any], d.pop("upcoming_event_list"))

        user_attr = WebcastLiveAnalyticsUserInteractionsResponseUserAttr.from_dict(d.pop("user_attr"))

        user_role = d.pop("user_role")

        verified = d.pop("verified")

        verified_content = d.pop("verified_content")

        verified_reason = d.pop("verified_reason")

        with_car_management_permission = d.pop("with_car_management_permission")

        with_commerce_permission = d.pop("with_commerce_permission")

        with_fusion_shop_entry = d.pop("with_fusion_shop_entry")

        webcast_live_analytics_user_interactions_response_user = cls(
            allow_find_by_contacts=allow_find_by_contacts,
            allow_others_download_video=allow_others_download_video,
            allow_others_download_when_sharing_video=allow_others_download_when_sharing_video,
            allow_share_show_profile=allow_share_show_profile,
            allow_show_in_gossip=allow_show_in_gossip,
            allow_show_my_action=allow_show_my_action,
            allow_strange_comment=allow_strange_comment,
            allow_unfollower_comment=allow_unfollower_comment,
            allow_use_linkmic=allow_use_linkmic,
            avatar_thumb=avatar_thumb,
            badge_image_list=badge_image_list,
            badge_list=badge_list,
            bg_img_url=bg_img_url,
            bio_description=bio_description,
            block_status=block_status,
            border_list=border_list,
            comment_restrict=comment_restrict,
            commerce_webcast_config_ids=commerce_webcast_config_ids,
            constellation=constellation,
            create_time=create_time,
            disable_ichat=disable_ichat,
            display_id=display_id,
            enable_ichat_img=enable_ichat_img,
            enigma_info=enigma_info,
            exp=exp,
            fan_ticket_count=fan_ticket_count,
            fold_stranger_chat=fold_stranger_chat,
            follow_status=follow_status,
            ichat_restrict_type=ichat_restrict_type,
            id=id,
            id_str=id_str,
            is_anchor_marked=is_anchor_marked,
            is_block=is_block,
            is_follower=is_follower,
            is_following=is_following,
            is_subscribe=is_subscribe,
            link_mic_stats=link_mic_stats,
            media_badge_image_list=media_badge_image_list,
            mint_type_label=mint_type_label,
            modify_time=modify_time,
            need_profile_guide=need_profile_guide,
            new_real_time_icons=new_real_time_icons,
            nickname=nickname,
            pay_grade=pay_grade,
            pay_score=pay_score,
            pay_scores=pay_scores,
            push_comment_status=push_comment_status,
            push_digg=push_digg,
            push_follow=push_follow,
            push_friend_action=push_friend_action,
            push_ichat=push_ichat,
            push_status=push_status,
            push_video_post=push_video_post,
            push_video_recommend=push_video_recommend,
            real_time_icons=real_time_icons,
            scm_label=scm_label,
            sec_uid=sec_uid,
            secret=secret,
            share_qrcode_uri=share_qrcode_uri,
            special_id=special_id,
            status=status,
            ticket_count=ticket_count,
            top_fans=top_fans,
            top_vip_no=top_vip_no,
            upcoming_event_list=upcoming_event_list,
            user_attr=user_attr,
            user_role=user_role,
            verified=verified,
            verified_content=verified_content,
            verified_reason=verified_reason,
            with_car_management_permission=with_car_management_permission,
            with_commerce_permission=with_commerce_permission,
            with_fusion_shop_entry=with_fusion_shop_entry,
        )

        webcast_live_analytics_user_interactions_response_user.additional_properties = d
        return webcast_live_analytics_user_interactions_response_user

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

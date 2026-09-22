from enum import StrEnum


class OAuthScope(StrEnum):
    USERCONSENTS = "user:consents"
    USERINFO = "user:info"
    WEBCASTBAN = "webcast:ban"
    WEBCASTBULK_LIVE_CHECK = "webcast:bulk_live_check"
    WEBCASTCHAT = "webcast:chat"
    WEBCASTCOMMENTS = "webcast:comments"
    WEBCASTFETCH = "webcast:fetch"
    WEBCASTLIVE_ANALYTICS = "webcast:live_analytics"
    WEBCASTMODERATORS = "webcast:moderators"
    WEBCASTMUTE = "webcast:mute"
    WEBCASTRANKINGS = "webcast:rankings"
    WEBCASTSENSITIVE_WORDS = "webcast:sensitive_words"
    WEBCASTSIGN_URL = "webcast:sign_url"
    WEBCASTUSER_EARNINGS = "webcast:user_earnings"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class RoomInfoFetchApiRoute(str, Enum):
    ALERTS = "ALERTS"
    API_LIVE = "API_LIVE"
    CACHE = "CACHE"
    CACHE_UNVERIFIED = "CACHE_UNVERIFIED"
    GET_LATEST_ROOM = "GET_LATEST_ROOM"
    INFO_BY_USER = "INFO_BY_USER"
    LIVE_ROOM_ID = "LIVE_ROOM_ID"
    MGET_INFO = "MGET_INFO"
    PRELOAD_ROOM = "PRELOAD_ROOM"
    ROOM_INFO_BY_ID = "ROOM_INFO_BY_ID"

    def __str__(self) -> str:
        return str(self.value)

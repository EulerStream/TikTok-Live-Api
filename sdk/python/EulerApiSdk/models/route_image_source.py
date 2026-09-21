from enum import Enum


class RouteImageSource(str, Enum):
    CDN = "CDN"
    CDN_CNAME = "CDN_CNAME"
    ORIGIN = "ORIGIN"

    def __str__(self) -> str:
        return str(self.value)

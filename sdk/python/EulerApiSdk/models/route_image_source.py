from enum import StrEnum


class RouteImageSource(StrEnum):
    CDN = "CDN"
    CDN_CNAME = "CDN_CNAME"
    ORIGIN = "ORIGIN"

    def __str__(self) -> str:
        return str(self.value)

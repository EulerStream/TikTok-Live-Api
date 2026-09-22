from enum import StrEnum


class WebcastFetchPlatform(StrEnum):
    MOBILE = "mobile"
    WEB = "web"

    def __str__(self) -> str:
        return str(self.value)

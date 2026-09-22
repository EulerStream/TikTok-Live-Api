from enum import StrEnum


class SignTikTokUrlBodyType(StrEnum):
    FETCH = "fetch"
    XHR = "xhr"

    def __str__(self) -> str:
        return str(self.value)

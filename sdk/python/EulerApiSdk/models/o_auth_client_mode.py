from enum import Enum


class OAuthClientMode(str, Enum):
    AUTO = "auto"
    DARK = "dark"
    LIGHT = "light"

    def __str__(self) -> str:
        return str(self.value)

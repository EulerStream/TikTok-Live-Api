from enum import StrEnum


class RevokeRequestBodyTokenTypeHint(StrEnum):
    ACCESS_TOKEN = "access_token"
    REFRESH_TOKEN = "refresh_token"

    def __str__(self) -> str:
        return str(self.value)

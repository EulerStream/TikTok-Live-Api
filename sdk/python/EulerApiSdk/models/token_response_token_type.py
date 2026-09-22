from enum import StrEnum


class TokenResponseTokenType(StrEnum):
    BEARER = "Bearer"

    def __str__(self) -> str:
        return str(self.value)

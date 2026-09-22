from enum import StrEnum


class IntrospectionResponseTokenType(StrEnum):
    BEARER = "Bearer"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class IntrospectionResponseTokenType(str, Enum):
    BEARER = "Bearer"

    def __str__(self) -> str:
        return str(self.value)

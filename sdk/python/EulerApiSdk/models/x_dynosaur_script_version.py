from enum import StrEnum


class XDynosaurScriptVersion(StrEnum):
    VALUE_0 = "5.3.0"

    def __str__(self) -> str:
        return str(self.value)

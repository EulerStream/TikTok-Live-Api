from enum import StrEnum


class XGnarlyScriptVersion(StrEnum):
    VALUE_0 = "5.3.2"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class XGnarlyScriptVersion(str, Enum):
    VALUE_0 = "5.3.2"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class StableStreamType(str, Enum):
    FLV = "FLV"
    HLS = "HLS"

    def __str__(self) -> str:
        return str(self.value)

from enum import StrEnum


class StableStreamType(StrEnum):
    FLV = "FLV"
    HLS = "HLS"

    def __str__(self) -> str:
        return str(self.value)

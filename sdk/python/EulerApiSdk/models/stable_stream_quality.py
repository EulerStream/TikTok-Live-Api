from enum import Enum


class StableStreamQuality(str, Enum):
    AUDIO_ONLY = "AUDIO_ONLY"
    AUTO = "AUTO"
    HD = "HD"
    HD_60 = "HD_60"
    LD = "LD"
    ORIGIN = "ORIGIN"
    SD = "SD"
    UHD = "UHD"
    UHD_60 = "UHD_60"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)

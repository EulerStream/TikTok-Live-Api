from enum import StrEnum


class WebcastGiftGalleryDataAnchorRankingLeague(StrEnum):
    TOEXPONENTIAL = "toExponential"
    TOFIXED = "toFixed"
    TOLOCALESTRING = "toLocaleString"
    TOPRECISION = "toPrecision"
    TOSTRING = "toString"
    VALUEOF = "valueOf"

    def __str__(self) -> str:
        return str(self.value)

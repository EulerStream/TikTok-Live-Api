from enum import Enum


class AvailableWebcastRankName(str, Enum):
    DAILY_RANK = "DAILY_RANK"
    FANS_TEAM_RANK = "FANS_TEAM_RANK"
    RANKING_LEAGUE = "RANKING_LEAGUE"
    SALE_RANK = "SALE_RANK"

    def __str__(self) -> str:
        return str(self.value)

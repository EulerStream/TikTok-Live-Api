from enum import StrEnum


class RetrieveWebcastRankingsRankType(StrEnum):
    DAILY_RANK = "DAILY_RANK"
    FANS_TEAM_RANK = "FANS_TEAM_RANK"

    def __str__(self) -> str:
        return str(self.value)

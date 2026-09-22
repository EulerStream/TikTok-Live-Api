from enum import StrEnum


class WebcastUserEarningsOutputPeriod(StrEnum):
    DAILY = "daily"

    def __str__(self) -> str:
        return str(self.value)

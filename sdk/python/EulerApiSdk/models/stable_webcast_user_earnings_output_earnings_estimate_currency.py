from enum import StrEnum


class StableWebcastUserEarningsOutputEarningsEstimateCurrency(StrEnum):
    USD = "USD"

    def __str__(self) -> str:
        return str(self.value)

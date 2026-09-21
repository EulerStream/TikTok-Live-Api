from enum import Enum


class StableWebcastUserEarningsOutputEarningsEstimateCurrency(str, Enum):
    USD = "USD"

    def __str__(self) -> str:
        return str(self.value)

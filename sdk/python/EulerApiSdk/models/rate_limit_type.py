from enum import StrEnum


class RateLimitType(StrEnum):
    ALERTS = "ALERTS"
    CATALOG = "CATALOG"
    RANKINGS = "RANKINGS"
    RATE_LIMITS = "RATE_LIMITS"
    WEBCAST = "WEBCAST"

    def __str__(self) -> str:
        return str(self.value)

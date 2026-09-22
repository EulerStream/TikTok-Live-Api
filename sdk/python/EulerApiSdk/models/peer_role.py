from enum import StrEnum


class PeerRole(StrEnum):
    ENTERPRISE = "enterprise"
    PUBLIC = "public"
    STAGING = "staging"

    def __str__(self) -> str:
        return str(self.value)

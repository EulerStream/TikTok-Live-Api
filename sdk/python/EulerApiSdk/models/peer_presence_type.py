from enum import StrEnum


class PeerPresenceType(StrEnum):
    AGENT = "agent"
    API = "api"

    def __str__(self) -> str:
        return str(self.value)

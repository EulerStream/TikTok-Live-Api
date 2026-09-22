from enum import StrEnum


class JWTConfigurationMetadataVersion(StrEnum):
    V1 = "v1"
    V2 = "v2"

    def __str__(self) -> str:
        return str(self.value)

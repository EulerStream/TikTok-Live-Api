from enum import StrEnum


class GetKeyRetrieveBy(StrEnum):
    ID = "id"
    VALUE = "value"

    def __str__(self) -> str:
        return str(self.value)

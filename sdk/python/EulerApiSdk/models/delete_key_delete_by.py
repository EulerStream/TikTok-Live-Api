from enum import StrEnum


class DeleteKeyDeleteBy(StrEnum):
    ID = "id"
    VALUE = "value"

    def __str__(self) -> str:
        return str(self.value)

from enum import StrEnum


class RetrieveWebcastGiftsWebcastLanguage(StrEnum):
    EN = "en"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class RetrieveWebcastGiftsWebcastLanguage(str, Enum):
    EN = "en"

    def __str__(self) -> str:
        return str(self.value)

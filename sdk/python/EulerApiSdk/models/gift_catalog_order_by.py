from enum import StrEnum


class GiftCatalogOrderBy(StrEnum):
    NAME = "name"
    PRICE = "price"

    def __str__(self) -> str:
        return str(self.value)

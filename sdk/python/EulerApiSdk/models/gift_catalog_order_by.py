from enum import Enum


class GiftCatalogOrderBy(str, Enum):
    NAME = "name"
    PRICE = "price"

    def __str__(self) -> str:
        return str(self.value)

from enum import IntEnum


class AccountScopes(IntEnum):
    VALUE_NEGATIVE_1 = -1
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_3 = 3
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_8 = 8
    VALUE_6 = 6
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19

    def __str__(self) -> str:
        return str(self.value)

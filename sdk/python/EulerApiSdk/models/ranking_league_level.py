from enum import IntEnum


class RankingLeagueLevel(IntEnum):
    VALUE_0 = 0
    VALUE_100 = 100
    VALUE_200 = 200
    VALUE_300 = 300
    VALUE_400 = 400
    VALUE_500 = 500
    VALUE_600 = 600
    VALUE_700 = 700
    VALUE_800 = 800
    VALUE_900 = 900
    VALUE_1000 = 1000
    VALUE_1100 = 1100
    VALUE_1200 = 1200
    VALUE_1300 = 1300
    VALUE_1400 = 1400
    VALUE_1500 = 1500
    VALUE_1800 = 1800
    VALUE_1900 = 1900
    VALUE_2000 = 2000

    def __str__(self) -> str:
        return str(self.value)

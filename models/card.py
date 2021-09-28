from dataclasses import dataclass
from enum import IntEnum


class SuitEnum(IntEnum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4


class RankEnum(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIZE = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


@dataclass
class Card:
    rank: IntEnum
    suit: IntEnum
    is_face_down: bool = False

    @property
    def name(self) -> str:
        return self.rank.name

    @property
    def value(self) -> int:
        if self.is_ace():
            return 11

        return 10 if self.rank in [
            RankEnum.TEN, RankEnum.JACK, RankEnum.QUEEN, RankEnum.KING
        ] else self.rank.value

    def reverse(self) -> None:
        self.is_face_down = not self.is_face_down

    def is_ace(self) -> bool:
        return self.rank == RankEnum.ACE

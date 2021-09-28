from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import IntEnum
from random import shuffle
from typing import List

from models.card import Card, RankEnum, SuitEnum


class DeckBuildingStrategy(ABC):
    @abstractmethod
    def build(self) -> List[Card]:
        """build the deck with the adequate cards"""


class FrenchDeckBuildingStrategy(DeckBuildingStrategy):
    """French deck building strategy
    A french deck contains four suits with cards ranging from two to ace
    """
    _ranks: List[IntEnum] = list(RankEnum)
    _suits: List[IntEnum] = list(SuitEnum)

    def build(self, n_decks: int = 1) -> List[Card]:
        cards: List[Card] = []
        for rank in self._ranks * n_decks:
            for suit in self._suits:
                cards.append(Card(rank=rank, suit=suit))
        return cards


@dataclass
class Deck(ABC):
    @abstractmethod
    def fill(self) -> None:
        """build the deck with the adequate cards"""

    @abstractmethod
    def shuffle(self) -> None:
        """randomly shuffle all the cards in the deck"""

    @abstractmethod
    def pop(self) -> Card:
        """pop the last card of the deck."""


class BlackjackShoe(Deck):
    _building_strategy: DeckBuildingStrategy = FrenchDeckBuildingStrategy()
    cards: List[Card] = field(default_factory=list)

    def __init__(self, n_decks: int = 1, auto_shuffle: bool = True):
        self.cards = self.fill(n_decks)
        if auto_shuffle:
            self.shuffle()

    def fill(self, n_decks: int) -> None:
        return self._building_strategy.build(n_decks)

    def shuffle(self) -> None:
        shuffle(self.cards)

    def pop(self) -> Card:
        if not self.cards:
            raise IndexError("No more cards in the deck.")
        return self.cards.pop()

    def __len__(self) -> int:
        return len(self.cards)

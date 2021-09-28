
from dataclasses import dataclass, field
from typing import List

from models.card import Card


@dataclass
class Hand:
    cards: List[Card] = field(default_factory=list)

    def clear(self) -> None:
        self.cards = []

    def add(self, card: Card) -> None:
        self.cards.append(card)

    @property
    def value(self) -> int:
        return sum(card.value for card in self.cards)

    def is_blackjack(self) -> bool:
        """
        - Is the hand a blackjack?
        For the hand to be counted as a blackjack:
            the total value should be 21, and,
            the total number of cards should be two.
        """
        return len(self.cards) == 2 and self.value == 21

    def is_busted(self) -> bool:
        """
        - Is the hand busted?
        For the hand to be counter busted:
            the total best_value should exceed 21.
        """
        return self.best_value > 21

    @property
    def best_value(self) -> int:
        """
        - What is the best value of the hand?
        Compute the best value possible,
        taking into account the fact that and Ace can be of value 11 or 1.
        """
        if self.value > 21 and self.has_aces():
            soft_value = self.value
            for _ in range(self.has_aces()):
                soft_value -= 10
                if soft_value <= 21:
                    return soft_value
            return soft_value
        return self.value

    def has_aces(self) -> int:
        """Returns the number of aces in the hand."""
        return sum(1 for card in self.cards if card.is_ace())

    def __len__(self) -> int:
        return len(self.cards)

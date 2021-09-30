from dataclasses import dataclass, field
from typing import List

from models.bankroll import Bankroll
from models.card import Card
from models.hand import Hand


@dataclass
class Player:
    name: str
    br: Bankroll = None
    br_balance: int = None
    hands: List[Hand] = field(default_factory=list)

    @property
    def hand(self):
        if len(self.hands) == 1:
            return self.hands[0]

    @hand.setter
    def hand(self, hand: Hand):
        return hand

    def __post_init__(self):
        self.hands = [Hand()]

        if not self.br:
            if not self.br_balance:
                raise ValueError(
                    'A bankroll balance amount is needed when the player does not have an existing bankroll'
                )

            self.br = Bankroll(balance=self.br_balance)

    def stand(self):
        """TODO:implement"""

    def hit(self, card: Card, hand_index: int = None):
        if hand_index:
            if self.hands[hand_index]:
                raise IndexError(f"{self} does not have this hand")
            self.hands[hand_index].add(card)

        self.hand.add(card)

    def doubling_down(self):
        """TODO:implement"""

    def split(self):
        """TODO:implement"""

    def __str__(self):
        return self.name


@dataclass
class Dealer:
    hand: Hand = Hand()

    def hit(self, card: Card):
        if not self.should_hit():
            raise ValueError(
                f"The dealer should stay. (hand value: {self.hand.value})")
        self.hand.add(card)

    def should_hit(self):
        """The dealer should hit if his hand value < 17, else, should stand"""
        return self.hand.value < 17 or len(self.hand) < 2

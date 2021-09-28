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

    def hit(self, card: Card, hand: Hand = None):
        if hand:
            if hand not in Hand:
                raise IndexError(f"{self} does not have this hand")
            hand.add(card)

        self.hand.add(card)

    def doubling_down(self):
        """TODO:implement"""

    def split(self):
        """TODO:implement"""

    def __str__(self):
        return self.name

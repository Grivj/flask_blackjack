from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from models.deck import BlackjackShoe
from models.player import Dealer, Player


@dataclass
class Table(ABC):
    @abstractmethod
    def add_player(self, player: Player) -> None:
        """add a player to the table"""

    @abstractmethod
    def del_player(self, player: Player) -> None:
        """del a player from the table"""


class BlackjackTable(Table):
    def __init__(self, id: int = None, n_decks: int = 1, maximum_players: int = 7):
        self.id = id
        self.n_decks: int = n_decks
        self.shoe = BlackjackShoe(n_decks)
        self.players: List[Player] = []
        self.dealer: Dealer = Dealer()
        self.maximum_players = maximum_players
        self.dealt: bool = False

    def add_player(self, player: Player) -> None:
        if player in self.players:
            raise IndexError(f"{player} already on the table.")
        self.players.append(player)

    def del_player(self, player: Player) -> None:
        if player not in self.players:
            raise IndexError(f"{player} not on this table.")
        self.players.remove(player)

    @property
    def player(self):
        if len(self.players) == 1:
            return self.players[0]

        return

    def deal_everyone(self):
        if self.dealt:
            raise ValueError("Table already dealt")

        for player in self.players:
            player.hit(self.shoe.pop())
        self.dealer.hit(self.shoe.pop())
        for player in self.players:
            player.hit(self.shoe.pop())
        card = self.shoe.pop()
        card.reverse()
        self.dealer.hit(card)
        self.dealt = True

    def reset(self):
        self.dealt = False
        self._reset_shoe()
        self._reset_dealer_hand()
        self._reset_players_hands()

    def _reset_shoe(self):
        self.shoe = BlackjackShoe(self.n_decks)

    def _reset_dealer_hand(self):
        self.dealer.hand.clear()

    def _reset_players_hands(self):
        for player in self.players:
            for hand in player.hands:
                hand.clear()

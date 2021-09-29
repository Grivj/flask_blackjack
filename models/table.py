from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from models.deck import BlackjackShoe
from models.player import Player


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
        self.shoe = BlackjackShoe(n_decks)
        self.players: List[Player] = []
        self.maximum_players = maximum_players

    def add_player(self, player: Player) -> None:
        if player in self.players:
            raise IndexError(f"{player} already on the table.")
        self.players.append(player)

    def del_player(self, player: Player) -> None:
        if player not in self.players:
            raise IndexError(f"{player} not on this table.")
        self.players.remove(player)

import unittest

from models.bankroll import Bankroll
from models.card import Card, RankEnum, SuitEnum
from models.player import Player


class PlayerTestCase(unittest.TestCase):
    def test_new_player(self):
        p = Player(name='John', br=Bankroll())
        self.assertEqual(p.name, 'John')

    def test_player_hits(self):
        p = Player(name='John', br_balance=10)
        c = Card(rank=RankEnum.TWO, suit=SuitEnum.CLUBS)
        p.hit(c)
        self.assertTrue(c in p.hands[0].cards)

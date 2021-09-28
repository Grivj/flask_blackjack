import unittest

from models.player import Player
from models.table import BlackjackTable


class TableTestCase(unittest.TestCase):
    def test_new_table_has_no_players(self):
        t = BlackjackTable()
        self.assertEqual(len(t.players), 0)

    def test_adding_player(self):
        t = BlackjackTable()
        p = Player("John", 100)
        t.add_player(p)
        self.assertTrue(p in t.players)

    def test_removing_player(self):
        t = BlackjackTable()
        p = Player("John", 100)
        t.add_player(p)
        t.del_player(p)
        self.assertTrue(p not in t.players)

    def test_cant_add_player_already_on_the_table(self):
        t = BlackjackTable()
        p = Player("John", 100)
        t.add_player(p)
        self.assertRaises(IndexError, t.add_player, p)

    def test_cant_del_player_not_on_the_table(self):
        t = BlackjackTable()
        p = Player("John", 100)
        self.assertRaises(IndexError, t.del_player, p)

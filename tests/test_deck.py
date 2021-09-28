import unittest

from models.deck import BlackjackShoe


class BjShoeTestCase(unittest.TestCase):
    def test_shoe_one_deck_has_52_cards(self):
        deck = BlackjackShoe()
        self.assertEqual(len(deck), 52)

    def test_shoe_ten_deck_has_520_cards(self):
        deck = BlackjackShoe(10)
        self.assertEqual(len(deck), 520)

    def test_shoe_pop_one_card_has_one_less_card(self):
        deck = BlackjackShoe(1)
        deck.pop()
        self.assertEqual(len(deck), 51)

    def test_shoe_pop_one_is_the_last_card_of_deck(self):
        deck = BlackjackShoe(1)
        last_card = deck.cards[-1]
        poped_card = deck.pop()
        self.assertEqual(last_card, poped_card)

    def test_poping_an_empty_shoe_raises_error(self):
        deck = BlackjackShoe()
        while(deck.cards):
            deck.pop()
        self.assertRaises(IndexError, deck.pop)

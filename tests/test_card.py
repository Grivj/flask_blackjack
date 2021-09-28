import unittest

from models.card import Card, RankEnum, SuitEnum


class CardTestCase(unittest.TestCase):

    def test_card_is_valid(self):
        self.assertTrue(Card(rank=RankEnum.SEVEN, suit=SuitEnum.CLUBS),
                        Card(rank=RankEnum.SEVEN, suit=SuitEnum.CLUBS))

    def test_card_is_not_reversed(self):
        card = Card(rank=RankEnum.SEVEN, suit=SuitEnum.CLUBS)
        self.assertFalse(card.is_face_down)

    def test_reversed_card_is_reversed(self):
        card = Card(rank=RankEnum.SEVEN, suit=SuitEnum.CLUBS)
        card.reverse()
        self.assertTrue(card.is_face_down)

    def test_reversed_card_twice_is_not_reversed(self):
        card = Card(rank=RankEnum.SEVEN, suit=SuitEnum.CLUBS)
        card.reverse()
        card.reverse()
        self.assertFalse(card.is_face_down)

    def test_face_value_card_has_right_value(self):
        card = Card(rank=RankEnum.SEVEN, suit=SuitEnum.CLUBS)
        self.assertEqual(card.value, 7)

    def test_card_is_an_ace(self):
        card = Card(rank=RankEnum.ACE, suit=SuitEnum.CLUBS)
        self.assertTrue(card.is_ace)

    def test_card_is_not_an_ace(self):
        card = Card(rank=RankEnum.THREE, suit=SuitEnum.CLUBS)
        self.assertFalse(card.is_ace())

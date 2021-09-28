import unittest
from random import choice

from models.card import Card, RankEnum, SuitEnum
from models.hand import Hand


class HandTestCase(unittest.TestCase):
    def test_new_hand_has_no_card(self):
        self.assertEqual(len(Hand()), 0)

    def test_adding_one_card(self):
        card = Card(rank=RankEnum.SEVEN, suit=SuitEnum.CLUBS)
        hand = Hand()
        hand.add(card)
        self.assertEqual(len(hand.cards), 1)

    def test_adding_many_cards_and_clearing_the_hand(self):
        card = Card(rank=RankEnum.SEVEN, suit=SuitEnum.CLUBS)
        hand = Hand()
        hand.add(card)
        hand.add(card)
        hand.add(card)
        hand.add(card)
        hand.clear()
        self.assertEqual(len(hand.cards), 0)

    def test_hand_value_is_0(self):
        hand = Hand()
        self.assertEqual(hand.value, 0)

    def test_hand_value_one_card(self):
        hand = Hand(cards=[
            Card(rank=RankEnum.SEVEN, suit=SuitEnum.CLUBS)
        ])
        self.assertEqual(hand.value, 7)

    def test_hand_value_multiple_cards(self):
        hand = Hand()
        total_value = 0
        for _ in range(1, 10):
            card = Card(rank=choice(list(RankEnum)),
                        suit=choice(list(SuitEnum)))
            total_value += card.value
            hand.add(card)
        self.assertEqual(hand.value, total_value)

    def test_hand_is_not_blackjack_because_of_value(self):
        hand = Hand(cards=[
            Card(rank=RankEnum.SEVEN, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.SEVEN, suit=SuitEnum.CLUBS)
        ])
        self.assertFalse(hand.is_blackjack())

    def test_hand_is_not_blackjack_because_not_two_cards(self):
        hand = Hand(cards=[
            Card(rank=RankEnum.SEVEN, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.SEVEN, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.SEVEN, suit=SuitEnum.CLUBS)
        ])
        self.assertFalse(hand.is_blackjack())

    def test_hand_is_blackjack(self):
        hand = Hand(cards=[
            Card(rank=RankEnum.ACE, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.KING, suit=SuitEnum.CLUBS)
        ])
        self.assertTrue(hand.is_blackjack())

    def test_hand_is_not_busted_no_cards(self):
        hand = Hand()
        self.assertFalse(hand.is_busted())

    def test_hand_is_not_busted_under_21(self):
        hand = Hand(cards=[
            Card(rank=RankEnum.KING, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.TWO, suit=SuitEnum.CLUBS)
        ])
        self.assertFalse(hand.is_busted())

    def test_hand_is_busted_over_21(self):
        hand = Hand(cards=[
            Card(rank=RankEnum.KING, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.QUEEN, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.TWO, suit=SuitEnum.CLUBS),
        ])
        self.assertTrue(hand.is_busted())

    def test_hand_is_not_busted_over_21_but_one_ace(self):
        hand = Hand(cards=[
            Card(rank=RankEnum.KING, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.KING, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.ACE, suit=SuitEnum.CLUBS),
        ])
        self.assertFalse(hand.is_busted())

    def test_hand_best_value_with_one_ace(self):
        hand = Hand(cards=[
            Card(rank=RankEnum.KING, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.KING, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.ACE, suit=SuitEnum.CLUBS),
        ])
        self.assertEqual(hand.best_value, 21)

    def test_hand_best_value_over_21_with_aces(self):
        hand = Hand(cards=[
            Card(rank=RankEnum.KING, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.KING, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.KING, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.ACE, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.ACE, suit=SuitEnum.CLUBS),
        ])
        self.assertEqual(hand.best_value, 32)

    def test_hand_best_value_over_21_without_aces(self):
        hand = Hand(cards=[
            Card(rank=RankEnum.KING, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.KING, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.KING, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.SEVEN, suit=SuitEnum.CLUBS),
        ])
        self.assertEqual(hand.best_value, 37)

    def test_hand_best_value_under_21_without_aces(self):
        hand = Hand(cards=[
            Card(rank=RankEnum.KING, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.SEVEN, suit=SuitEnum.CLUBS),
        ])
        self.assertEqual(hand.best_value, 17)

    def test_hand_best_value_under_21_with_aces(self):
        hand = Hand(cards=[
            Card(rank=RankEnum.KING, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.ACE, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.ACE, suit=SuitEnum.CLUBS),
            Card(rank=RankEnum.SEVEN, suit=SuitEnum.CLUBS),
        ])
        self.assertEqual(hand.best_value, 19)

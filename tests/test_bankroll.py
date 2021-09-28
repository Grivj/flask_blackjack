import unittest

from models.bankroll import Bankroll


class BankrollTestCase(unittest.TestCase):
    def test_new_balance_is_zero(self):
        self.assertEqual(Bankroll().balance, 0)

    def test_new_balance_with_starting_amount(self):
        self.assertEqual(Bankroll(balance=1000).balance, 1000)

    def test_cash_in(self):
        b = Bankroll()
        b.cash_in(1000)
        self.assertEqual(b.balance, 1000)

    def test_cash_in_zero(self):
        b = Bankroll()
        self.assertRaises(ValueError, b.cash_in, 0)

    def test_cash_in_negative(self):
        b = Bankroll()
        self.assertRaises(ValueError, b.cash_in, -1000)

    def test_cash_out(self):
        b = Bankroll()
        b.cash_in(1000)
        b.cash_out(100)
        self.assertEqual(b.balance, 900)

    def test_cash_out_with_zero_balance(self):
        b = Bankroll()
        self.assertRaises(ValueError, b.cash_out, 1000)

    def test_cash_out_with_too_small_balance(self):
        b = Bankroll()
        b.cash_in(100)
        self.assertRaises(ValueError, b.cash_out, 1000)

    def test_cash_out_negative_amount(self):
        b = Bankroll()
        self.assertRaises(ValueError, b.cash_out, -1000)

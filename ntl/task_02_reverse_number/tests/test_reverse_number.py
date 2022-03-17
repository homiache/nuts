# coding=utf-8


import unittest
from ntl.task_02_reverse_number.reverse_number import natural_number_reverse


class TestReverseNumber(unittest.TestCase):

    def test_simple_natural_number(self):
        self.assertEqual(231, natural_number_reverse(132))

    def test_big_natural_number(self):
        self.assertEqual(287159654, natural_number_reverse(456951782))

    def test_palindrome_number(self):
        self.assertEqual(7777, natural_number_reverse(7777))

    def test_leading_zeroes_for_natural_number(self):
        self.assertEqual(42, natural_number_reverse(24000000))

    def test_zero(self):
        self.assertEqual(0, natural_number_reverse(0))

    # TODO Create test for a big numbers in Python 2 after clarifying deviations from task # 1


class TestReverseNumberNegative(unittest.TestCase):

    def test_negative_number(self):
        with self.assertRaises(Exception):
            natural_number_reverse(-2)

    def test_float(self):
        with self.assertRaises(Exception):
            natural_number_reverse(2.55)

    def test_string(self):
        with self.assertRaises(Exception):
            natural_number_reverse("48")


# coding=utf-8


import unittest
from ntl.task_02_number_reverse import reverse


class TestReverseNumber(unittest.TestCase):

    def test_simple_natural_number(self):
        self.assertEqual(231, reverse(132))

    def test_big_natural_number(self):
        self.assertEqual(287159654, reverse(456951782))

    def test_palindrome_number(self):
        self.assertEqual(7777, reverse(7777))

    def test_leading_zeroes_for_natural_number(self):
        self.assertEqual(42, reverse(24000000))

    def test_zero(self):
        self.assertEqual(0, reverse(0))





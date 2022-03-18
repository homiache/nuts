# coding=utf-8

import unittest
from ntl.task_03_generator.generator import Merge


# Positive cases for generator.
class TestMerge(unittest.TestCase):
    def test_smoke(self):

        # Iterables:
        a = [-5, 2, 5, 7]        # List. Int < 0 is also allowed.
        b = "234"                # String.
        c = (8, 9, 10, 34.028)   # Tuple. Note that every float is converted to the int.
        d = range(6)             # Generator.
        e = {1: 1, 2: "bebebe"}  # Please note that dict.__iter__() returns keys, not values.
        f = ""                   # Empty string.
        g = Merge([28, 29])      # Merge object itself. Must correctly stops.

        # Create main generator to test.
        merge = Merge(g, f, b, c, d, e, a)

        # Expectation is a list of ordered expected values.
        expectation = [
            -5,
            0,
            1, 1,
            2, 2, 2, 2,
            3, 3,
            4, 4,
            5, 5,
            7,
            8,
            9,
            10,
            28,
            29,
            34,
        ]

        # Generate current value as a list.
        current = [x for x in merge]

        # Test.
        self.assertEqual(expectation, current)


# Negative cases for generator.
class TestMergeNegative(unittest.TestCase):

    def test_string_symbols(self):
        with self.assertRaises(Exception):
            Merge(".")

    def test_list_of_list(self):
        with self.assertRaises(Exception):
            Merge([[2]])

    @staticmethod
    def iterate_more():
            generator = Merge([2])
            next(generator)  # 2 should be returned
            next(generator)  # StopIteration exception should be returned.

    def test_empty_input(self):
        with self.assertRaises(Exception):
            Merge()


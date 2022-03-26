# coding=utf-8

import unittest
from ntl.task_04_intervals_from_list.intervals_from_list import get_intervals


# Positive tests
class TestGetIntervals(unittest.TestCase):

    # Test from the task description
    def test_acceptance(self):
        self.assertEqual("1-5,7-8,10,12-13", get_intervals([1, 2, 3, 4, 4, 5, 7, 8, 10, 12, 13]))

    def test_empty_list(self):
        self.assertEqual("", get_intervals([]))

    def test_one_negative_element(self):
        self.assertEqual("-2", get_intervals([-2]))

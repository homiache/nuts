# coding=utf-8

import unittest
from ntl.task_01_interval_in_seconds import interval_in_seconds


# Acceptance tests with cases from the task to test interval_in_seconds function.
class TestIntervalInSecondsAcceptance(unittest.TestCase):

    def test_input_string_with_int_delta_without_time_unit(self):
        self.assertEqual(30, interval_in_seconds("30"), "Seconds is default unit so 30 should be returned.")

    def test_input_string_with_int_delta_and_seconds_time_unit(self):
        self.assertEqual(30, interval_in_seconds("30s"), "30 should be returned.")

    def test_input_string_no_delta_seconds_time_unit_in_uppercase(self):
        self.assertEqual(1, interval_in_seconds("S"), "1 should be returned as default value for seconds.")

    def test_input_string_with_fractional_delta_and_minutes_time_unit(self):
        self.assertEqual(3630, interval_in_seconds("60.5m"), "Minutes could be fractional.")

    # Wrong time unit.
    def test_input_string_with_wrong_seconds_time_unit(self):
        with self.assertRaises(Exception):
            interval_in_seconds("10seconds")

    # Mixed deltas with unit types are not allowed.
    def test_input_string_combined_time_units(self):
        with self.assertRaises(Exception):
            interval_in_seconds("1m30s")

    # Wrong time unit.
    def test_input_string_with_wrong_time_unit_y(self):
        with self.assertRaises(Exception):
            interval_in_seconds("1y")

    # Empty string is not a valid value.
    def test_input_empty_string(self):
        with self.assertRaises(Exception):
            interval_in_seconds("  ")


# Additional tests to test interval_in_seconds function.
class TestIntervalInSecondsAdditionalCases(unittest.TestCase):

    def test_input_string_with_zero_without_unit_type(self):
        self.assertEqual(0, interval_in_seconds("0"), "0 should be returned.")

    def test_input_string_with_fractional_delta_more_than_1_but_without_time_unit(self):
        self.assertEqual(2, interval_in_seconds("2.99"), "Integer part of a fraction is expected.")

    def test_input_string_with_fractional_delta_less_than_1_with_minutes_time_unit(self):
        self.assertEqual(59, interval_in_seconds("0.99M"), "Integer part of a fraction is expected.")

    # Invalid input value.
    def test_input_string_with_fractional_delta_without_int_part_of_value(self):
        with self.assertRaises(Exception):
            interval_in_seconds(".65")

    # Invalid input value.
    def test_input_string_with_fraction_as_delta_without_fractional_part_of_value(self):
        with self.assertRaises(Exception):
            interval_in_seconds("42.")

    # The Ultimate Question of Life, the Universe, and Everything. :)
    # This case tests case with more than one number character in an input. Created during acceptable regex research.
    def test_input_string_with_more_than_2_number_chars(self):
        self.assertEqual(42, interval_in_seconds("42"), "Input is a valid int value of seconds.")

    # This case is also related with regex research.
    # Invalid input value.
    def test_input_with_2_points(self):
        with self.assertRaises(Exception):
            interval_in_seconds("2.2.55")


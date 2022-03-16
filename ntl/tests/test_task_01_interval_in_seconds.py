# coding=utf-8

import unittest
from ntl.task_01_interval_in_seconds import interval_in_seconds


# Positive cases for seconds.
# Delta possible values:
#   0
#   any natural
#   0 < float_delta < 1
#   1 <= float_delta
#   no delta value if time unit is present
#
# Possible time units:
#   s
#   S
#   no time unit if delta value is present
class TestIntervalInSecondsForSeconds(unittest.TestCase):
    def test_seconds_without_time_unit(self):
        self.assertEqual(30, interval_in_seconds("30"), "Seconds is default unit so 30 should be returned.")

    def test_seconds_with_time_unit(self):
        self.assertEqual(0, interval_in_seconds("0s"), "30 should be returned.")

    def test_time_unit_for_seconds_in_uppercase_only(self):
        self.assertEqual(1, interval_in_seconds("S"), "1 should be returned as default value for seconds.")

    def test_fractional_seconds(self):
        self.assertEqual(5, interval_in_seconds("5.99S"), "Returns the closest int value less then float result.")

    def test_zero_seconds_without_unit_type(self):
        self.assertEqual(0, interval_in_seconds("0.16"), "0 should be returned.")

    # The Ultimate Question of Life, the Universe, and Everything. :)
    # This case tests case with more than one number character in an input. Created during acceptable regex research.
    # Could be deleted.
    def test_seconds_with_more_than_2_number_chars(self):
        self.assertEqual(42, interval_in_seconds("42"), "Input is a valid int value of seconds.")


# Positive cases for minutes.
# Delta possible values:
#   0
#   any natural
#   0 < float_delta < 1
#   1 <= float_delta
#   no delta value if time unit is present
#
# Possible time units:
#   m
#   M
class TestIntervalInSecondsForMinutes(unittest.TestCase):

    def test_minutes_with_time_unit_in_uppercase(self):
        self.assertEqual(120, interval_in_seconds("2M"), "120 seconds should be returned for 2 minutes.")

    def test_fractional_minutes_with_delta_value_more_then_1(self):
        self.assertEqual(3621, interval_in_seconds("60.354m"), "Minutes could be fractional.")

    def test_fractional_minutes_with_delta_value_less_then_1(self):
        self.assertEqual(59, interval_in_seconds("0.99M"), "Returns the closest int value less then float result.")

    def test_minutes_time_unit_only(self):
        self.assertEqual(60, interval_in_seconds("m"), "60 seconds should be returned for one minute.")

    def test_0_minutes(self):
        self.assertEqual(0, interval_in_seconds("0m"), "0 seconds in 0 minutes.")


# Positive cases for hours.
# Delta possible values:
#   0
#   any natural
#   0 < float_delta < 1
#   1 <= float_delta
#   no delta value if time unit is present
#
# Possible time units:
#   h
#   H
class TestIntervalInSecondsForHours(unittest.TestCase):

    def test_hours_with_time_unit_in_uppercase(self):
        self.assertEqual(93600, interval_in_seconds("26H"), "93600 Seconds in 26 hours.")

    def test_fractional_hours_with_delta_value_more_then_1(self):
        self.assertEqual(3819, interval_in_seconds("1.061h"), "Minutes could be fractional.")

    def test_fractional_hours_with_delta_value_less_then_1(self):
        self.assertEqual(3564, interval_in_seconds("0.99H"), "Returns the closest int value less then float result.")

    def test_hour_time_unit_only(self):
        self.assertEqual(3600, interval_in_seconds("h"), "3600 seconds should be returned for one hour.")

    def test_0_hours(self):
        self.assertEqual(0, interval_in_seconds("0h"), "0 seconds in 0 hours.")


# Positive cases for days.
# Delta possible values:
#   0
#   any natural
#   0 < float_delta < 1
#   1 <= float_delta
#   no delta value if time unit is present
#
# Possible time units:
#   d
#   D
class TestIntervalInSecondsForDays(unittest.TestCase):

    def test_days_with_time_unit_in_uppercase(self):
        self.assertEqual(345600, interval_in_seconds("4D"), "345600 Seconds in 4 days.")

    def test_fractional_days_with_delta_value_more_then_1(self):
        self.assertEqual(86486, interval_in_seconds("1.001d"), "Minutes could be fractional.")

    def test_fractional_days_with_delta_value_less_then_1(self):
        self.assertEqual(1123, interval_in_seconds("0.013d"), "Returns the closest int value less then float result.")

    def test_days_time_unit_only(self):
        self.assertEqual(86400, interval_in_seconds("D"), "3600 seconds should be returned for one hour.")

    def test_0_hours(self):
        self.assertEqual(0, interval_in_seconds("0D"), "0 seconds in 0 hours.")

    # In Python 3 the plain int type is unbound.
    # Max int for Python 2 is 9223372036854775807
    # We have 86400 seconds in a day.
    # 9223372036854775807 seconds is about 106751991167300.64 days
    # Two tests for close to boundary cases:
    def test_less_than_max_int_for_python_2(self):
        self.assertAlmostEqual(
            first=9223372036854775209,
            second=interval_in_seconds("106751991167300.639d"),
            delta=1000
        )

    def test_more_than_max_int_for_python_2(self):
        self.assertAlmostEqual(
            first=9223372036854806400,
            second=interval_in_seconds("106751991167301d"),
            delta=1000
        )


class TestIntervalInSecondsNegative(unittest.TestCase):

    # Invalid input value.
    def test_input_string_with_fractional_delta_without_int_part_of_value(self):
        with self.assertRaises(Exception):
            interval_in_seconds(".65")

    # Invalid input value.
    def test_input_string_with_fraction_as_delta_without_fractional_part_of_value(self):
        with self.assertRaises(Exception):
            interval_in_seconds("42.")

    # This case is also related with regex research.
    # Invalid input value.
    def test_input_with_2_points(self):
        with self.assertRaises(Exception):
            interval_in_seconds("2.2.55")

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

    # Negative value in string.
    def test_input_negative_value(self):
        with self.assertRaises(Exception):
            interval_in_seconds(" -3")

    # Empty string is not a valid value.
    def test_space_in_the_middle(self):
        with self.assertRaises(Exception):
            interval_in_seconds(" 3 5h ")

    # Crazy symbols
    def test_symbols_in_the_input(self):
        with self.assertRaises(Exception):
            interval_in_seconds("!@@#(_+*")

    def test_integer(self):
        with self.assertRaises(Exception):
            interval_in_seconds(6)

    def test_list(self):
        with self.assertRaises(Exception):
            interval_in_seconds(["8s"])





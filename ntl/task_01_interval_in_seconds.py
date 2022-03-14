# coding=utf-8


# Write a function, which accepts time delta specifier as a string argument and returns time interval in seconds
# as an integer. Supported time units: s – second, m – minute, h – hour, d – day, with seconds being default unit
# and 1 being default value. Please supply unit tests for the solution.
#
# Examples of input time delta specifier and output value:
#
# | Time Delta Specifier | Output Value     |
# | -------------------- | ---------------- |
# | 30                   | 30               |
# | 30s                  | 30               |
# | S                    | 1                |
# | 60.5m                | 3630             |
# | 10seconds            | Exception raised |
# | 1m30s                | Exception raised |
# | 1y                   | Exception raised |
# | <empty string>       | Exception raised |


# Solution plan:
# a) validate input values;
# b) process simple cases;
# c) process patterns for every time unit;
# d) create tests.
#
# Templates For seconds:
# - "<delta value>s" where delta value could be positive integer or zero
# - "<delta value>" where delta value could be positive integer or zero
# - "s"
#
# TODO Clarify requirements to define patterns
#
# Notes
# 1. It could be a problems with the int max value in theory but they say that "In Python, value of an integer
# is not restricted by the number of bits and can expand to the limit of the available memory".


import re


def interval_in_seconds(time_delta_specifier):

    # Check type of an input data.
    if time_delta_specifier.__class__ is not str:
        raise Exception("The input value must be a string.")

    # Delete surrounded spaces.
    time_delta_specifier = time_delta_specifier.strip()

    # Check empty string.
    if len(time_delta_specifier) == 0:
        raise Exception("The input value must not be an empty string.")

    # Check simple cases with time unit only.
    if time_delta_specifier == 's':
        return 1  # Default value is 1.
    elif time_delta_specifier == 'm':
        return 60  # Seconds in 1 minute.
    elif time_delta_specifier == 'h':
        return 3600  # Seconds in 1 hour.
    elif time_delta_specifier == "d":
        return 86400  # Seconds in 1 day.

    # Possible pattern for delta value
    pattern = '^[0-9]+$|^[0-9]+[.][0-9]+$'
    if re.match(pattern, time_delta_specifier):
        return True
    else:
        return False


# Just for rough visual pattern testing
for each in [
    "0",
    "2.54",
    ".65",
    "18.",
    "42",
    "2.2.55"
]:
    print("{} is {}".format(each, interval_in_seconds(each)))

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
#
# Notes
#
# * It could be a problems with the int max value in theory but they say that "In Python, value of an integer
#   is not restricted by the number of bits and can expand to the limit of the available memory".
#
# * Acceptance tests use numbers in a decimal from. So lets think that no other format (e. g. hexadecimal with prefix)
#   is allowed.
#
# * In the task description and acceptance tests, there is no exact information on how we round the seconds
#   in case they turn out to be fractional. In this case, I am free to decide what to expect.
#   My choice is to expect a maximum integer that is still less than the input value. Integer part of a fraction.
#   Moreover int(float(str)) do that.


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

    # Time units can be in uppercase or lowercase.
    # Set input to a lowercase for easier processing
    time_delta_specifier = time_delta_specifier.lower()

    # Check simple cases with time unit only.
    if time_delta_specifier == 's':
        return 1  # Default value is 1.
    elif time_delta_specifier == 'm':
        return 60  # Seconds in 1 minute.
    elif time_delta_specifier == 'h':
        return 3600  # Seconds in 1 hour.
    elif time_delta_specifier == "d":
        return 86400  # Seconds in 1 day.

    # Process seconds without time unit.
    if re.match("^[0-9]+$|^[0-9]+[.][0-9]+$", time_delta_specifier):
        return int(float(time_delta_specifier))

    # If no other choice is present then return an Exception about invalid value.
    raise Exception("Invalid input value.")

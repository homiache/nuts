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


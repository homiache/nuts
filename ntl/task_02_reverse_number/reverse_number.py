# coding=utf-8


# Write a function which accepts a natural number and returns another natural number that represents input’s reverse.
# Please supply unit tests for the solution.
#
# Examples of input and output values:
#
# | Input     | Output    |
# | 123       | 321       |
# | 456951782 | 287159654 |
# | 7777      | 7777      |
# | 24000000  | 42        |
#
# Assume our data type can handle numbers of arbitrary length and don’t worry about overflows.
# Obviously there is a simple solution like output = int(str(input)[::-1]) but here we ask not to use character
# representation and work only with numbers.
#
# Extra task. Propose how to generalize this task to floating point numbers. Think not only about how to reverse
# a number but also what user expects from this routine (e.g. should 12.345 result in 21.543 or 543.21
# or any other variant).


def natural_number_reverse(number):
    """
    Function accepts a natural number and returns another natural number that represents input’s reverse.
    :param number:
    :return:
    """

    # Check input value
    if number.__class__ is not int:
        raise Exception("Input value is not an integer.")

    if number < 0:
        raise Exception("Input value is not a natural number.")

    # We will change this number to get value for every natural number order
    current_number = number
    result = 0

    # The algorithm is simple: if we have the remainder X from division by 10 of the current number,
    # then we multiply the result by 10 and add X to it. After that, we assign the value of the integer part
    # of the division to the current number and apply the algorithm again.
    # Until the current number becomes less than one.
    while current_number >= 1:
        result = result * 10 + current_number % 10
        current_number = int(current_number / 10)

    return result

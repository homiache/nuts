# coding=utf-8


# Given a sorted list of natural numbers [1, 2, 3, 4, 4, 5, 7, 8, 10, 12, 13].
# Write a function which returns a string with intervals of every simple sequence "1-5,7-8,10,12-13".


# Solution from the online review.
def get_intervals(list_of_numbers):
    """
    Returns a string with intervals.
    :param list_of_numbers: list, sorted natural numbers
    :return: string
    """

    # Check type of input data.
    if list_of_numbers.__class__ is not list:
        raise Exception("List is expected as an input.")

    # Empty list has no intervals.
    if len(list_of_numbers) == 0:
        return ""

    # Sort list if it is not sorted.
    list_of_numbers.sort()

    # Set "start" and "end" elements as a first element of the input list.
    # Check that it is a number.
    if list_of_numbers[0].__class__ is not int:
        raise Exception("Input list should contains integers only.")

    start = list_of_numbers[0]
    end = list_of_numbers[0]

    # 
    result = ""

    for each in list_of_numbers[1:]:
        if each - end <= 1:
            end = each
        else:
            if each == end:
                result = "{},{}".format(result, end)
            else:
                result = "{},{}-{}".format(result, start, end)
            start = each
            end = each

    if start == end:
        result = "{},{}".format(result, end)
    else:
        result = "{},{}-{}".format(result, start, end)

    return result[1:]




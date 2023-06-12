from functools import reduce


def double_numbers(numbers):
    """
    TODO: Write a function that takes a list of numbers and returns a list with double of each number.
    :param numbers: list of numbers
    :return: list with double of each number
    """
    return None


def get_even_numbers(numbers):
    """
    TODO: Write a function that takes a list of numbers and returns a list with only the even numbers.
    :param numbers: list of numbers
    :return: list with only the even numbers
    """
    return None


def convert_to_uppercase(strings):
    """
    TODO: Write a function that takes a list of strings and returns a list with the strings in uppercase.
    :param strings: list of strings
    :return: list with the strings in uppercase
    """
    return None


def sum_numbers(numbers):
    """
    TODO: Write a function that takes a list of numbers and returns the sum of the numbers.
    :param numbers: list of numbers
    :return: sum of the numbers
    """
    return None


def get_string_lengths(strings):
    """
    Write a function that takes a list of strings and returns a list with the length of each string.
    :param strings: list of strings
    :return: list with the length of each string
    """
    return None


def get_numbers_greater_than_5(numbers):
    """
    Write a function that takes a list of numbers and returns a list with only the numbers greater than 5.
    :param numbers: list of numbers
    :return: list with only the numbers greater than 5
    """
    return None


def sum_lists(list1, list2):
    """
    Write a function that takes two lists of numbers of the same size and returns a list with the sum of the elements
    from the two lists at the same position.
    :param list1: list of numbers
    :param list2: list of numbers
    :return: list with the sum of the elements from the two lists at the same position
    """
    return None


def get_odd_numbers(numbers):
    """
    Write a function that takes a list of numbers and returns a list with only the odd numbers.
    :param numbers: list of numbers
    :return: list with only the odd numbers
    """
    return None


def calculate_average(numbers):
    """
    Write a function that takes a list of numbers and returns the average of the numbers.
    :param numbers: list of numbers
    :return: average of the numbers
    """
    return None


if __name__ == '__main__':
    list_numbers = [1, 32, 45, 2, 3, 36, 100, 4, 5, 87, 6]
    list_strings = ["hello", "world", "python", "is", "fun"]

    print("Exercise 1:")
    print(double_numbers(list_numbers))

    print("Exercise 2:")
    print(get_even_numbers(list_numbers))

    print("Exercise 3:")
    print(convert_to_uppercase(list_strings))

    print("Exercise 4:")
    print(sum_numbers(list_numbers))

    print("Exercise 5:")
    print(get_string_lengths(list_strings))

    print("Exercise 6:")
    print(get_numbers_greater_than_5(list_numbers))

    print("Exercise 7:")
    print(sum_lists(list_numbers, list_numbers))

    print("Exercise 8:")
    print(get_odd_numbers(list_numbers))

    print("Exercise 9:")
    print(calculate_average(list_numbers))

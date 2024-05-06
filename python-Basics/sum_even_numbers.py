#!/usr/bin/env python3
"""Sum of even numbers."""


def sum_even(num_list):
    """
    Function calculates sum of all even numbers in a list.

    Args:
        num_list: list of numbers

    Returns:
        sum of all even numbers
    """
    if not num_list:
        return 0

    even_sum = 0
    for num in num_list:
        if not isinstance(num, int):
            raise ValueError("Input list can only contain integers")
        if num % 2 == 0:
            even_sum += num
    return even_sum


"""Test examples"""
assert sum_even([1, 2, 3, 4, 4, 6, 6, 7, 8, 8, 9, 10]) == 48
assert sum_even([0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -30
assert sum_even([]) == 0

print("All tests passed!")

print(sum_even([1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10]))
print(sum_even([0, -1, -2, -2, -3, -4, -5, -5, -6, -7, -8, -8, -9, -10]))
print(sum_even([]))

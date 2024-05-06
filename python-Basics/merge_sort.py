#!/usr/bin/env python3
"""Merge sort algorithm."""


def merge_sort(arr):
    """
    Sorts an array using merge sort algorithm.

    Args:
        arr: array to be sorted

    Returns:
        sorted array
    """
    def merge(left, right):
        """
        Merges two sorted arrays.

        Args:
            left: left array
            right: right array

        Returns:
            merged array
        """
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


"""Test Examples"""
assert merge_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert merge_sort([0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0]
assert merge_sort([]) == []

print("All tests passed!")

print()

array = [10, 102, 98, 87, 71, 65, 13, 24, 55, 2]
print("Unsorted Array: ", array)
print("Sorted Array: ", merge_sort(array))

print()

array_2 = [0, -10, -103, -98, -87, -71, -65, -13, -24, -55, -2]
print("Unsorted Array: ", array_2)
print("Sorted Array: ", merge_sort(array_2))

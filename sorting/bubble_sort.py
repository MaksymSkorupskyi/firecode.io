"""Bubble Sort
Write a function that takes in a list of ints and uses
the Bubble Sort algorithm to sort the list 'in place' in ascending order.
The method should return the same, in-place sorted list.

Note: Bubble sort is one of the most inefficient ways to sort a large list of integers.
Nevertheless, it is an interview favorite.
Bubble sort has a time complexity of O(n2). However, if the
sample size is small, bubble sort provides a simple implementation of a classic sorting algorithm.

This simple sorting algorithm iterates over a list, comparing elements in pairs
and swapping them until the larger elements "bubble up" to the end of the list,
and the smaller elements stay at the "bottom".

DISCUSSION:
Bubble sort has many of the same properties as insertion sort, but has slightly higher overhead.
In the case of nearly sorted data, bubble sort takes O(n) time,
but requires at least 2 passes through the data (whereas insertion sort requires something more like 1 pass).

PROPERTIES:
Stable
O(1) extra space
O(n2) comparisons and swaps
Adaptive: O(n) when nearly sorted
"""


def bubble_sort(a: list) -> list:
    unsorted = True
    passnum = len(a) - 1
    while unsorted:
        unsorted = False
        for i in range(passnum):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                unsorted = True
        passnum -= 1
    return a


# def bubble_sort(a):
#     while True:
#         noSwaps = True
#         for i in range(len(a) - 1):
#             if a[i] > a[i+1]:
#                 a[i], a[i+1] = a[i+1], a[i]
#                 noSwaps = False
#         if noSwaps:
#             break
#     return a

print(bubble_sort([5, 4, 3]))

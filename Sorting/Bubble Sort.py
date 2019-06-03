"""Bubble Sort
Write a function that takes in a list of ints and uses
the Bubble Sort algorithm to sort the list 'in place' in ascending order.
The method should return the same, in-place sorted list.

Note: Bubble sort is one of the most inefficient ways to sort a large list of integers.
Nevertheless, it is an interview favorite.
Bubble sort has a time complexity of O(n2). However, if the
sample size is small, bubble sort provides a simple implementation of a classic sorting algorithm.

Examples:
bubble_sort([5, 4, 3]) -> [3, 4, 5]
bubble_sort([3]) -> [3]
bubble_sort([]) -> []
[] -> [Empty] List
"""


def bubble_sort(a):
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

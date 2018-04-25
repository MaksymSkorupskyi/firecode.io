"""Repeated Elements in Array
Write a function - duplicate_items to find the redundant or repeated items in a list and return them in sorted order.
This method should return a list of redundant integers in ascending sorted order (as illustrated below).

Examples:
duplicate_items([1, 3, 4, 2, 1]) => [1]
duplicate_items([1, 3, 4, 2, 1, 2, 4]) => [1, 2, 4]
"""


# one liner:
def duplicate_items(list_numbers):
    return [i for i in set(list_numbers) if list_numbers.count(i) > 1]


# the same - explained:
def duplicate_items(list_numbers):
    duplicates = []
    for i in set(list_numbers):
        if list_numbers.count(i) > 1:
            duplicates.append(i)
    return sorted(duplicates)


# return list_number only with duplicate_items (in-place)
def duplicate_items(list_numbers):
    for i in set(list_numbers):
        list_numbers.remove(i)
    return list_numbers


# # stack solution :) O(3)
# def duplicate_items(list_numbers):
#     stack = []
#     duplicates = []
#     for i in list_numbers:
#         if i not in stack:
#             stack.append(i)
#         else:
#             duplicates.append(i)
#     return sorted(duplicates)

print(duplicate_items([1, 3, 4, 2, 1]))
print(duplicate_items([1, 3, 4, 2, 1, 2, 4]))
print(duplicate_items([1, 3, 4, 2, 1, 2, 4, 1, 1, 1]))

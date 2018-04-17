"""Find One Missing Number from 1 to 10
Given an list containing 9 numbers ranging from 1 to 10, write a function to find the missing number.
Assume you have 9 numbers between 1 to 10 and only one number is missing.

Example:
input_list: [1, 2, 4, 5, 6, 7, 8, 9, 10]
find_missing_number(input_list) => 3
"""

# cycle
def find_missing_number(list_numbers):
    for i in range(len(list_numbers)):
        if list_numbers[i + 1] - list_numbers[i] != 1:
            return list_numbers[i] + 1

# sums difference
def find_missing_number(list_numbers):
    return sum(list(range(1, len(list_numbers)+2))) - sum(list_numbers)


print(find_missing_number([1, 2, 4, 5, 6, 7, 8, 9, 10]))
print(find_missing_number([1, 2, 3, 4, 5, 6, 7, 8, 10]))
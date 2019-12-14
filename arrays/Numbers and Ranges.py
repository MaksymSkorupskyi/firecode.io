"""Numbers and Ranges
Given a sorted list and an input number as inputs, write a function to return a Range object, consisting of the indices of the first and last occurrences of the input number in the list. Check out the Use Me section to examine the structure of the Range class.

Note: The List can have duplicate numbers. The indices within the Range object should be zero based.

Examples:
Input List  : [1,2,5,5,8,8,10]
Input Number : 8
Output : [4,5]

Input List  : [1,2,5,5,8,8,10]
Input Number : 2
Output : [1,1]
"""

# def find_range(input_list,input_number):
#     return [input_list.index(input_number), input_list.index(input_number) + input_list.count(input_number) - 1]

class Range(object):
    def __init__(self):
        self.lower_bound = -1
        self.upper_bound = -1

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self):
        return "[" + str(self.lower_bound) + "," + str(self.upper_bound) + "]"


def find_range(input_list, input_number):
    return Range(input_list.index(input_number), input_list.index(input_number) + input_list.count(input_number) - 1)


print(find_range([1,2,5,5,8,8,10], 8))
print(find_range([1,2,5,5,8,8,10], 2))

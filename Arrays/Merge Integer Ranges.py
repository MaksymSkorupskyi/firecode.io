"""Merge Integer Ranges
Given a sorted list of integer ranges (see Range in Use Me), merge all overlapping ranges.
Note: Check out the Use Me section to get the structure of the Range class.

Example:
Input  : [[1,10], [5,8], [8,15]]
Output : [[1,15]]
"""


class Range(object):
    def __init__(self):
        self.lower_bound = -1
        self.upper_bound = -1

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self):
        return "[" + str(self.lower_bound) + "," + str(self.upper_bound) + "]"

def merge_ranges(input_range_list):
    if len(input_range_list) <= 1:
        return input_range_list
    res = []
    res.append(input_range_list[0])
    for i in range(1, len(input_range_list)):
        if res[i].upper_bound <= input_range_list[i].lower_bound:
            res[i].upper_bound = input_range_list[i].upper_bound
        else:
            res.append(i)
    return res


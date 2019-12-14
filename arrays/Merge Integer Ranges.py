"""Merge Integer Ranges

Given a sorted list of integer ranges (see Range in Use Me), merge all overlapping ranges.

Example:
Input  : [[1,10], [5,8], [8,15]]
Output : [[1,15]]

Input	 ->     Expected Result
Input List: [[1,5], [5,10], [11,15] ,[15,20]] -> [[1,10], [11,20]]
Input List: [[1,10], [5,8], [8,15]] -> [[1,15]]
Input List: [[1,4], [3,7], [5,10], [11,15]] -> [[1,10], [11,15]]
Input List: [[5,50], [25,100], [150,200]] -> [[5,100], [150,200]]
Input List: [[1,2], [2,5], [8,10], [15,20]] -> [[1,5], [8,10], [15,20]]
"""


class Range():
    def __init__(self):
        self.lower_bound = -1
        self.upper_bound = -1

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self):
        return "[" + str(self.lower_bound) + "," + str(self.upper_bound) + "]"

# in-place O(n), O(1):
    def merge_ranges(input_range_list):
        if len(input_range_list) <= 1:
            return input_range_list
        for i in range(len(input_range_list) - 1, 0, -1):
            if input_range_list[i - 1].upper_bound >= input_range_list[i].lower_bound:
                input_range_list[i - 1].upper_bound = input_range_list[i].upper_bound
                input_range_list.pop(i)
        return input_range_list


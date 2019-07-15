"""Insertion Sort
Like Selection Sort, this algorithm segments the list into sorted and unsorted parts.
It iterates over the unsorted segment, and inserts the element being viewed
into the correct position of the sorted list.

Explanation
We assume that the first element of the list is sorted.
We then go to the next element, let's call it x.
If x is larger than the first element we leave as is.
If x is smaller, we copy the value of the first element to the second position and then set the first element to x.

As we go to the other elements of the unsorted segment,
we continuously move larger elements in the sorted segment up the list until we encounter
an element smaller than x or reach the end of the sorted segment, and then place x in it's correct position.


Time Complexity O(n^2)
In the worst case scenario, an array would be sorted in reverse order.
The outer for loop in the Insertion Sort function always iterates n-1 times.

In the worst case scenario, the inner for loop would swap once, then swap two and so forth.
The amount of swaps would then be 1 + 2 + ... + (n - 3) + (n - 2) + (n - 1)
which gives the Insertion Sort a time complexity of O(n^2).


DISCUSSION:
Although it is one of the elementary sorting algorithms with O(n2) worst-case time,
insertion sort is the algorithm of choice either when the data is nearly sorted (because it is adaptive)
or when the problem size is small (because it has low overhead).

For these reasons, and because it is also stable, insertion sort is often used as the recursive base case
(when the problem size is small) for higher overhead divide-and-conquer sorting algorithms,
such as merge sort or quick sort.

PROPERTIES:
Stable
O(1) extra space
O(n2) comparisons and swaps
Adaptive: O(n) time when nearly sorted
Very low overhead
"""


def insertion_sort(nums: list) -> list:
    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward
        # if they are larger than the item to insert
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Insert the item
        nums[j + 1] = item_to_insert


# Verify it works
random_list_of_nums = [9, 1, 15, 28, 6]
insertion_sort(random_list_of_nums)
print(random_list_of_nums)

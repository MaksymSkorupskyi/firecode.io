"""Merge Sort
This divide and conquer algorithm splits a list in half,
and keeps splitting the list by 2 until it only has singular elements.

Adjacent elements become sorted pairs, then sorted pairs are merged and sorted with other pairs as well.
This process continues until we get a sorted list with all the elements of the unsorted input list.

Explanation
We recursively split the list in half until we have lists with size one.
We then merge each half that was split, sorting them in the process.

sorting is done by comparing the smallest elements of each half.
The first element of each list are the first to be compared.
If the first half begins with a smaller value, then we add that to the sorted list.
We then compare the second smallest value of the first half with the first smallest value of the second half.

Every time we select the smaller value at the beginning of a half,
we move the index of which item needs to be compared by one.

Note that the merge_sort() function, unlike the previous sorting algorithms,
returns a new list that is sorted, rather than sorting the existing list.

Therefore, Merge Sort requires space to create a new list of the same size as the input list.

Time Complexity O(nlog(n))
Let's first look at the merge function.
It takes two lists, and iterates n times, where n is the size of their combined input.
The merge_sort function splits its given array in 2, and recursively sorts the sub-arrays.
As the input being recursed is half of what was given,
like binary trees this makes the time it takes to process grow logarithmically to n.

Therefore the overall time complexity of the Merge Sort algorithm is O(nlog(n)).

DISCUSSION:
Merge sort is very predictable.
It makes between 0.5lg(n) and lg(n) comparisons per element, and between lg(n) and 1.5lg(n) swaps per element.
The minima are achieved for already sorted data; the maxima are achieved, on average, for random data.
If using Θ(n) extra space is of no concern, then merge sort is an excellent choice:
It is simple to implement, and it is the only stable O(n·lg(n)) sorting algorithm.
Note that when sorting linked lists, merge sort requires only Θ(lg(n)) extra space (for recursion).

Merge sort is the algorithm of choice for a variety of situations:
when stability is required,
when sorting linked lists,
and when random access is much more expensive than sequential access (for example, external sorting on tape).

There do exist linear time in-place merge algorithms for the last step of the algorithm,
but they are both expensive and complex.
The complexity is justified for applications such as external sorting when Θ(n) extra space is not available.

PROPERTIES:
Stable
Θ(n) extra space for arrays (as shown)
Θ(lg(n)) extra space for linked lists
Θ(n·lg(n)) time
Not adaptive
Does not require random access to data
"""


def merge(left_list: list,
          right_list: list) -> list:
    sorted_list = []
    left_list_index = right_list_index = 0

    # We use the list lengths often, so its handy to make variables
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # We check which value from the start of each list is smaller
            # If the item at the beginning of the left list is smaller, add it to the sorted list
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # If the item at the beginning of the right list is smaller, add it to the sorted list
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # If we've reached the end of the of the left list,
        # add the elements from the right list
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # If we've reached the end of the of the right list,
        # add the elements from the left list
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums: list) -> list:
    # If the list is a single element, return it
    if len(nums) <= 1:
        return nums

    # Use floor division to get midpoint, indices must be integers
    mid = len(nums) // 2

    # Sort and merge each half recursively
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Merge the sorted lists into a new one
    return merge(left_list, right_list)


# Verify it works
random_list_of_nums = [120, 45, 68, 250, 176]
random_list_of_nums = merge_sort(random_list_of_nums)
print(random_list_of_nums)

"""Quick Sort
This divide and conquer algorithm is the most often used sorting algorithm.
When configured correctly, it's extremely efficient and does not require the extra space Merge Sort uses.
We partition the list around a pivot element, sorting values around the pivot.

Explanation
Quick Sort begins by partitioning the list - picking one value of the list that will be in its sorted place.
This value is called a pivot.
All elements smaller than the pivot are moved to its left.
All larger elements are moved to its right.

Knowing that the pivot is in it's rightful place,
we recursively sort the values around the pivot until the entire list is sorted.

Time Complexity O(nlog(n))
The worst case scenario is when the smallest or largest element is always selected as the pivot.
This would create partitions of size n-1, causing recursive calls n-1 times.
This leads us to a worst case time complexity of O(n^2).

While this is a terrible worst case, Quick Sort is heavily used
because it's average time complexity is much quicker.
While the partition function utilizes nested while loops,
it does comparisons on all elements of the array to make its swaps.
As such, it has a time complexity of O(n).

With a good pivot, the Quick Sort function would partition the array into halves
which grows logarithmically with n.
Therefore the average time complexity of the Quick Sort algorithm is O(nlog(n)).

DISCUSSION:
When carefully implemented, quick sort is robust and has low overhead.
When a stable sort is not needed, quick sort is an excellent general-purpose sort
– although the 3-way partitioning version should always be used instead.

The 2-way partitioning code shown above is written for clarity rather than optimal performance;
it exhibits poor locality, and, critically, exhibits O(n2) time when there are few unique keys. A more efficient and robust 2-way partitioning method is given in Quicksort is Optimal by Robert Sedgewick and Jon Bentley. The robust partitioning produces balanced recursion when there are many values equal to the pivot, yielding probabilistic guarantees of O(n·lg(n)) time and O(lg(n)) space for all inputs.

With both sub-sorts performed recursively, quick sort requires O(n) extra space for the recursion stack in the worst case when recursion is not balanced. This is exceedingly unlikely to occur, but it can be avoided by sorting the smaller sub-array recursively first; the second sub-array sort is a tail recursive call, which may be done with iteration instead. With this optimization, the algorithm uses O(lg(n)) extra space in the worst case.

PROPERTIES:
Not stable
O(lg(n)) extra space (see discussion)
O(n2) time, but typically O(n·lg(n)) time
Not adaptive

"""


# There are different ways to do a Quick Sort partition, this implements the Hoare partition scheme.
# Tony Hoare also created the Quick Sort algorithm.
def partition(nums: list,
              low: int,
              high: int) -> int:
    # We select the middle element to be the pivot.
    # Some implementations select the first element or the last element.
    # Sometimes the median value becomes the pivot, or a random one.
    # There are many more strategies that can be chosen or created.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than
        # the element at j (on right right of the pivot), then swap them
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums) -> None:
    # Create a helper function that will be called recursively
    def _quick_sort(items: list,
                    low: int,
                    high: int) -> None:
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


# Verify it works
random_list_of_nums = [22, 5, 1, 18, 99]
quick_sort(random_list_of_nums)
print(random_list_of_nums)

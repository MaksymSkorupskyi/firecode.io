"""Heap Sort
This popular sorting algorithm, like the Insertion and Selection sorts,
segments the list into sorted and unsorted parts.
It converts the unsorted segment of the list to a Heap data structure,
so that we can efficiently determine the largest element.

Explanation
We begin by transforming the list into a Max Heap - a Binary Tree where the biggest element is the root node.
We then place that item to the end of the list.
We then rebuild our Max Heap which now has one less value,
placing the new largest value before the last item of the list.

We iterate this process of building the heap until all nodes are removed.

Time Complexity
Let's first look at the time complexity of the heapify function.
In the worst case the largest element is never the root element, this causes a recursive call to heapify.
While recursive calls might seem dauntingly expensive, remember that we're working with a binary tree.

Visualize a binary tree with 3 elements, it has a height of 2.
Now visualize a binary tree with 7 elements, it has a height of 3.
The tree grows logarithmically to n. The heapify function traverses that tree in O(log(n)) time.

The heap_sort function iterates over the array n times.
Therefore the overall time complexity of the Heap Sort algorithm is O(nlog(n)).

DISCUSSION:
Heap sort is simple to implement, performs an O(n·lg(n)) in-place sort, but is not stable.

The first loop, the Θ(n) “heapify” phase, puts the array into heap order.
The second loop, the O(n·lg(n)) “sortdown” phase, repeatedly extracts the maximum and restores heap order.

The heapify function is written recursively for clarity.
Thus, as shown, the code requires Θ(lg(n)) space for the recursive call stack. However, the tail recursion in sink() is easily converted to iteration, which yields the O(1) space bound.

Both phases are slightly adaptive, though not in any particularly useful manner.
In the nearly sorted case, the heapify phase destroys the original order.
In the reversed case, the heapify phase is as fast as possible since the array starts in heap order,
but then the sortdown phase is typical.
In the few unique keys case, there is some speedup but not as much as in shell sort or 3-way quicksort.

PROPERTIES:
Not stable
O(1) extra space (see discussion)
O(n·lg(n)) time
Not really adaptive

"""


def heapify(nums: list,
            heap_size: int,
            root_index: int) -> None:
    # Assume the index of the largest element is the root index
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # If the left child of the root is a valid index,
    # and the element is greater than the current largest element, then update the largest element
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # Do the same for the right child of the root
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # If the largest element is no longer the root element, swap them
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)


def heap_sort(nums: list) -> None:
    n = len(nums)

    # Create a Max Heap from the list
    # The 2nd argument of range means we stop at the element before -1 i.e.
    # the first element of the list.
    # The 3rd argument of range means we iterate backwards, reducing the count
    # of i by 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Move the root of the max heap to the end of
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


# Verify it works
random_list_of_nums = [35, 12, 43, 8, 51]
heap_sort(random_list_of_nums)
print(random_list_of_nums)

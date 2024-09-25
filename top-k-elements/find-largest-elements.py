# Find the top 3 largest elements in an array.
import pytest

class MinHeap:
    def __init__(self):
        self.top = float('-inf')
        self.left = float('-inf')
        self.right = float('-inf')

    def replace(self, n):
        if n <= self.left and n <= self.right:
            self.top = n
        elif self.left < n and self.left <= self.right:
            self.top = self.left
            self.left = n
        else:
            self.top = self.right
            self.right = n

def find_largest_elements(arr):
    n = len(arr)
    if n <= 3:
        return arr

    # min-heap -- https://www.geeksforgeeks.org/min-heap-in-python/
    #
    #    [0]       top element is less than or equal to its two children
    #   /   \
    # [1]   [2]
    #
    min_heap = MinHeap()
    for i in range(n):
        # Compare element with top heap element.
        el = arr[i]
        if el > min_heap.top:
            # If the current element is greater, pop the top element from the heap (min_heap[0]) and push the new element.
            min_heap.replace(el)


    # At the end, the heap will contain the 3 largest elements.
    return [min_heap.top, min_heap.left, min_heap.right]

@pytest.mark.parametrize("arr, expected", [
    ([], []),
    ([1, 2], [1, 2]),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 1, 1, 1, 1], [1, 1, 1]),
    ([9, 1, 1, 2, 7, 1, 1, 1, 5], [9, 7, 5]),
    ([1, 5, 11, 9, 7, 2], [11,9,7]),
])
def test_find_largest_elements(arr, expected):
    r = find_largest_elements(arr)
    assert set(r) == set(expected)

# Given an array, find the next greater element for each item.
# If there isn't one, output -1.

import pytest

def find_next_greater(arr):
    n = len(arr)
    if n == 0:
        return []
    stack = []
    result = [-1] * n

    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            result[stack.pop()] = arr[i]
        stack.append(i)

    return result

@pytest.mark.parametrize("arr, expected", [
    ([], []),
    ([0], [-1]),
    ([1,4,6,3,2,7], [4,6,7,7,7,-1]),
])
def test_find_next_greater(arr, expected):
    n = find_next_greater(arr)
    assert n == expected

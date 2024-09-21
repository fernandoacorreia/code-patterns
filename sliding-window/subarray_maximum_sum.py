import pytest


def find_subarray_maximum_sum(a, k):
    # initialize a window containing the sum of the first k elements
    # iterate through the array
    #   - subtract value of leftmost item
    #   - add new items value from the right
    #   - update the result
    n = len(a)
    window_sum = sum(a[:k])

    max_sum = window_sum
    max_start_index = 0

    for i in range(n - k):
        window_sum = window_sum - a[i] + a[i + k]
        if window_sum > max_sum:
            max_sum = window_sum
            max_start_index = i + 1
    return a[max_start_index:max_start_index + k], max_sum


@pytest.mark.parametrize("a, size, expected_array, expected_sum", [
    ([], 0, [], 0),
    ([3, 2, 7, 5, 9, 6, 2], 3, [7, 5, 9], 21),
])
def test_find_subarray_maximum_sum(a, size, expected_array, expected_sum):
    assert find_subarray_maximum_sum(a, size) == (expected_array, expected_sum)

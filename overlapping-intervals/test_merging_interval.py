import merging_interval
import pytest

@pytest.mark.parametrize("arr, expected", [
    ([], []),
    ([[1,2]], [[1,2]]),
    ([[1,2], [1,3]], [[1, 3]]),
    ([[1,2], [1,6], [2,4]], [[1,6]]),
    ([[1,2], [1,6], [2,7]], [[1,7]]),
    ([[1,3], [2,6], [8,10], [15,18]], [[1,6], [8,10], [15,18]]),
    ([[1,3], [2,6], [8,10], [9,11], [15,18]], [[1,6], [8,11], [15,18]]),
])
def test_merge_overlapping_intervals(arr, expected):
    result = merging_interval.merge_overlapping_intervals(arr)
    assert result == expected

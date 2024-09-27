from search_rotated_array import search_rotated_array
import pytest


@pytest.mark.parametrize("arr, target, expected", [
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ([4, 5, 6, 7, 0, 1, 2], 4, 0),
    ([4, 5, 6, 7, 0, 1, 2], 2, 6),
])
def test_search_rotated_array(arr, target, expected):
    result = search_rotated_array(arr, target)
    assert result == expected

@pytest.mark.parametrize("arr, target", [
    ([4, 5, 6, 7, 0, 1, 2], 3),
])
def test_search_rotated_array_invalid(arr, target):
    with pytest.raises(ValueError, match=f"{target} not found in the input array"):
        search_rotated_array(arr, target)


from summarizer import Summarizer
import pytest


def test_pre_computed():
    a = [1, 2, 3, 4, 5, 6, 7]
    summarizer = Summarizer(a)
    expected = [0, 1, 3, 6, 10, 15, 21, 28]
    assert summarizer.pre_computed == expected

def test_find_sum_invalid_start():
    summarizer = Summarizer([1, 2, 3, 4, 5, 6, 7])
    with pytest.raises(ValueError, match="start must be >= 0"):
        summarizer.find_sum(-1, 1)

def test_find_sum_invalid_end():
    summarizer = Summarizer([1, 2, 3, 4, 5, 6, 7])
    with pytest.raises(ValueError, match="end must be < 7"):
        summarizer.find_sum(0, 7)

@pytest.mark.parametrize("start, end, expected", [
    (2, 4, 12),
    (4, 4, 5),
    (0, 6, 28),
    (0, 0, 1),
    (6, 6, 7),
])
def test_find_sum(start, end, expected):
    summarizer = Summarizer([1, 2, 3, 4, 5, 6, 7])
    sum = summarizer.find_sum(start, end)
    assert sum == expected

import pytest


def is_palindrome(s):
    n = len(s)
    i = 0
    j = n - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

@pytest.mark.parametrize("s, expected", [
    ("", True),
    ("a", True),
    ("aba", True),
    ("abcba", True),
    ("abcdcba", True),
    ("abx", False),
    ("abcxa", False),
    ("abcdxba", False),
    ("abxdcba", False),
    ("tattarrattat", True),
])
def test_is_palindrome(s, expected):
    assert is_palindrome(s) == expected

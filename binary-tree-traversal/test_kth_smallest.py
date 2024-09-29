import pytest

from kth_smallest import Solution, TreeNode


@pytest.mark.parametrize("arr, k, expected", [
    ([3,1,4,None,2], 1, 1),
    ([50,30,60,20,40,None,None,1], 3, 30),
])
def test_kthSmallest(arr, k, expected):
    tree = array_to_binary_tree(arr)
    solution = Solution()
    result = solution.kthSmallest(tree, k)
    assert result == expected

def array_to_binary_tree(arr):
    if not arr:
        return None

    def build_tree(index):
        if index >= len(arr) or arr[index] is None:
            return None

        node = TreeNode(arr[index])
        node.left = build_tree(2 * index + 1)
        node.right = build_tree(2 * index + 2)
        return node

    return build_tree(0)
    return None

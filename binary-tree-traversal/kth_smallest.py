# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            self.result.append(node.val)
            inorder(node.right)

        inorder(root)

        if len(self.result) == 0:
            return ValueError("Input tree was empty.")

        return self.result[k-1]

#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def areSymetric(
            left: Optional[TreeNode], right: Optional[TreeNode]
        ) -> bool:
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return (
                left.val == right.val
                and areSymetric(left.left, right.right)
                and areSymetric(left.right, right.left)
            )

        if root is None:
            return True
        return areSymetric(root.left, root.right)


# @lc code=end

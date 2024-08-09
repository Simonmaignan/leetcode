#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        left_equals = self.isSameTree(p.left, q.left)
        right_equals = self.isSameTree(p.right, q.right)

        return left_equals and right_equals


# @lc code=end

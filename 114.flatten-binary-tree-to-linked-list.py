#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        # print(f"cur={root.val}")
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            end_left = root.left
            # print(f"cur={root.val}; start_left={end_left.val}")
            while end_left.right:
                end_left = end_left.right
            # print(f"cur={root.val}; end_left={end_left.val}")
            end_left.right = root.right
            root.right = root.left
            root.left = None


# @lc code=end

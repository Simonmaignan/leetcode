#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#
from typing import List, Optional


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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        val_list: List[int] = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return

            dfs(node.left)
            val_list.append(node.val)
            dfs(node.right)

        dfs(root)
        min_diff = float("inf")
        for i in range(1, len(val_list)):
            min_diff = min(min_diff, abs(val_list[i] - val_list[i - 1]))
        return min_diff


# @lc code=end

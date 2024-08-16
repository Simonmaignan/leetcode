#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n == 0:
            return None
        left, right = 0, n
        mid = (left + right) // 2
        left_node = self.sortedArrayToBST(nums[left:mid])
        right_node = self.sortedArrayToBST(nums[mid + 1 : right])
        return TreeNode(val=nums[mid], left=left_node, right=right_node)


# @lc code=end

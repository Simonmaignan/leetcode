#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#
from typing import Optional, Tuple
from collections import deque


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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        cur_level = 1
        max_level_sum: Tuple[int, int] = (cur_level, root.val)
        while queue:
            cur_level_sum = 0
            for _ in range(len(queue)):
                cur_node = queue.pop()
                cur_level_sum += cur_node.val
                if cur_node.left:
                    queue.appendleft(cur_node.left)
                if cur_node.right:
                    queue.appendleft(cur_node.right)
            if cur_level_sum > max_level_sum[1]:
                max_level_sum = (cur_level, cur_level_sum)
            cur_level += 1
        return max_level_sum[0]


# @lc code=end

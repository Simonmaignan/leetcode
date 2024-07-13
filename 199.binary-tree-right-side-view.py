#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
from collections import deque
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        right_side_view: List[int] = []
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                current_node = queue.popleft()
                for child in [current_node.left, current_node.right]:
                    if child:
                        queue.append(child)
                if i == (level_size - 1):
                    right_side_view.append(current_node.val)
        return right_side_view


# @lc code=end

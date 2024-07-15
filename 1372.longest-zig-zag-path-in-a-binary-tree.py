#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
# ]
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
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest_zig_zag = 0

        def maxZigZag(
            node: Optional[TreeNode], left_steps: int, right_steps: int
        ) -> None:
            if node is None:
                return
            self.longest_zig_zag = max(
                right_steps, left_steps, self.longest_zig_zag
            )
            # print(f"node={node.val}; left={left}; right={right}")
            # Going left -> left path reset
            maxZigZag(node.left, left_steps=right_steps + 1, right_steps=0)
            # Going right -> right path reset
            maxZigZag(node.right, left_steps=0, right_steps=left_steps + 1)

        maxZigZag(root, 0, 0)
        return self.longest_zig_zag


# @lc code=end

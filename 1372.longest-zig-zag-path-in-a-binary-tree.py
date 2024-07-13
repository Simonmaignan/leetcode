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
        def maxZigZag(
            node: Optional[TreeNode], left: bool, current_path: int
        ) -> int:
            if node is None:
                return 0
            # current_path += 1
            print(f"node={node.val}; left={left}; current_path={current_path}")
            new_path_right = maxZigZag(node.right, True, 0)
            new_path_left = maxZigZag(node.left, False, 0)
            print(f"node={node.val}; left={left}; current_path={current_path}")
            print(f"new_path_right={new_path_right}")
            print(f"new_path_left={new_path_left}")
            if left:
                current_path += new_path_left
                current_path = max(current_path, new_path_right)
            else:
                current_path += new_path_right
                current_path = max(current_path, new_path_left)
            print(f"current_path={current_path+1}")

            return current_path + 1

        return max(maxZigZag(root, True, 0), maxZigZag(root, False, 0))


# @lc code=end

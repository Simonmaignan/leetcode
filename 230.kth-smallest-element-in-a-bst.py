#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
from typing import Optional, List


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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        k_smallest: List[int] = []

        def find_k_smallest(root: Optional[TreeNode]) -> None:
            if root is None:
                return
            # print(f"root={root.val}")

            find_k_smallest(root.left)

            if len(k_smallest) == k:
                return
            k_smallest.append(root.val)
            # print(f"center; root={root.val}; k_smallest={k_smallest}")

            find_k_smallest(root.right)

        find_k_smallest(root)
        return k_smallest[-1]


# @lc code=end

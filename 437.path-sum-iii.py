#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
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
    def check_target_match(
        self, sums_prefix: List[int], targetSum: int
    ) -> None:
        for i in range(len(sums_prefix) - 1):
            if (sums_prefix[-1] - sums_prefix[i]) == targetSum:
                self.target_sum_nb_matches += 1

    def dfs(
        self, root: Optional[TreeNode], sums_prefix: List[int], targetSum: int
    ) -> None:
        if root is None:
            return
        # print(f"Node {root.val}")
        sums_prefix.append(sums_prefix[-1] + root.val)
        self.check_target_match(sums_prefix, targetSum)
        # print(target_sums_list)
        self.dfs(root.left, sums_prefix, targetSum)
        self.dfs(root.right, sums_prefix, targetSum)
        sums_prefix.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.target_sum_nb_matches = 0
        self.dfs(root, [0], targetSum)
        return self.target_sum_nb_matches


# @lc code=end

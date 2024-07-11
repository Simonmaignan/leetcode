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
    def add_to_list(
        self,
        target_sums_list: List[int],
        to_add: int,
        target: Optional[int] = None,
    ) -> None:
        for i in range(len(target_sums_list)):
            target_sums_list[i] += to_add
            if target is not None and target_sums_list[i] == target:
                # print(f"match")
                self.target_sum_match += 1

    def dfs(
        self,
        root: Optional[TreeNode],
        target_sums_list: List[int],
        targetSum: int,
    ) -> None:
        if root is None:
            return
        # print(f"Node {root.val}")
        target_sums_list.append(0)
        self.add_to_list(target_sums_list, root.val, target=targetSum)
        # print(target_sums_list)
        self.dfs(root.left, target_sums_list, targetSum)
        self.dfs(root.right, target_sums_list, targetSum)
        target_sums_list.pop()
        self.add_to_list(target_sums_list, -root.val)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.target_sum_match = 0
        self.dfs(root, [], targetSum)
        return self.target_sum_match


# @lc code=end

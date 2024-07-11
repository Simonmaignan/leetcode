#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
from typing import Dict, Optional
from collections import defaultdict


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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(
            root: Optional[TreeNode],
            cur_sum: int,
            sums_counter: Dict[int, int],
        ) -> int:
            if root is None:
                return 0
            target_sum_nb_matches = 0
            cur_sum += root.val
            target_sum_nb_matches += sums_counter[cur_sum - targetSum]
            sums_counter[cur_sum] += 1
            target_sum_nb_matches += dfs(root.left, cur_sum, sums_counter)
            target_sum_nb_matches += dfs(root.right, cur_sum, sums_counter)
            sums_counter[cur_sum] = max(0, sums_counter[cur_sum] - 1)
            return target_sum_nb_matches

        sums_counter: Dict[int, int] = defaultdict(int)
        sums_counter[0] = 1
        return dfs(root, 0, sums_counter)


# @lc code=end

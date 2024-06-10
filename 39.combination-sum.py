#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
from typing import List


# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations: List[List[int]] = []
        n = len(candidates)

        def dfs(start_index: int, rest: int, combination: List[int]) -> None:
            if rest < 0:
                return
            if rest == 0:
                combinations.append(combination[:])
                return

            for idx in range(start_index, n):
                combination.append(candidates[idx])
                dfs(idx, rest - candidates[idx], combination)
                combination.pop()

        dfs(0, target, [])

        return combinations


# @lc code=end

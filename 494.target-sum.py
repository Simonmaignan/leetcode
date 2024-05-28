#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
from typing import List


# @lc code=start
class Solution:
    def findTargetSumWays_(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp: List[List[int]] = [[-1] * 2001 for _ in range(n + 1)]

        def dfs(num_i: int, sum_expr: int) -> int:
            if num_i == n:
                if sum_expr == target:
                    return 1
                else:
                    return 0
            if dp[num_i][sum_expr] >= 0:
                return dp[num_i][sum_expr]

            nb_max_comb = 0
            nb_max_comb += dfs(num_i + 1, sum_expr + nums[num_i])
            nb_max_comb += dfs(num_i + 1, sum_expr - nums[num_i])

            dp[num_i][sum_expr] = nb_max_comb

            return nb_max_comb

        return dfs(0, 0)


# @lc code=end

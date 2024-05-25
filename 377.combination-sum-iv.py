#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#
from typing import List


# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo: List[int] = [-1] * (target + 1)

        def dfs(sum_num: int) -> int:
            if sum_num == target:
                return 1
            if sum_num > target:
                return 0
            if memo[sum_num] >= 0:
                return memo[sum_num]

            nb_comb = 0
            for num in nums:
                nb_comb += dfs(sum_num + num)

            memo[sum_num] = nb_comb
            return nb_comb

        return dfs(0)


# @lc code=end

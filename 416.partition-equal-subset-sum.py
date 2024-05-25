#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
from typing import List


# @lc code=start
class Solution:
    def canPartition_(self, nums: List[int]) -> bool:
        n = len(nums)
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        half_sum = sum_nums // 2
        dp: List[List[int]] = [[False] * (half_sum + 1) for _ in range(n + 1)]

        def dfs(start_index: int, left_sum: int) -> bool:
            if start_index == n or left_sum > half_sum or dp[start_index][left_sum]:
                return False
            if left_sum == half_sum:
                return True

            for i in range(start_index, n):
                if dfs(i + 1, left_sum + nums[i]):
                    return True
            dp[start_index][left_sum] = True
            return False

        return dfs(0, 0)

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        half_sum = sum_nums // 2
        dp: List[List[int]] = [[False] * (half_sum + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i, num in enumerate(nums):
            for amount in range(half_sum + 1):
                dp[i + 1][amount] = dp[i][amount]
                if amount >= num:
                    dp[i + 1][amount] = dp[i + 1][amount] or dp[i][amount - num]
                if amount == half_sum and dp[i + 1][amount]:
                    return True

        return False


# @lc code=end

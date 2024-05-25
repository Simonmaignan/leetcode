#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#
from typing import List


# @lc code=start
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp: List[List[int]] = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for dice in range(n):
            for value in range(1, target + 1):
                for dice_throw in range(1, min(k, value) + 1):
                    dp[dice + 1][value] += dp[dice][value - dice_throw]

        return dp[-1][-1] % (10**9 + 7)


# @lc code=end

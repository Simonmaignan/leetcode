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
            for value in range(target):
                for dice_throw in range(1, k + 1):
                    if value + 1 - dice_throw >= 0:
                        dp[dice + 1][value + 1] += dp[dice][value + 1 - dice_throw]

        return dp[-1][-1] % (10**9 + 7)


# @lc code=end

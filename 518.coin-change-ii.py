#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#
from typing import List


# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp: List[int] = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[-1]


# @lc code=end

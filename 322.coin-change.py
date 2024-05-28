#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
from typing import List

# @lc code=start
from math import inf


class Solution:
    def coinChange_(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp: List[List[int]] = [[inf] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0
        for i, coin in enumerate(coins):
            for value in range(amount + 1):
                dp[i + 1][value] = dp[i][value]
                if value >= coin:
                    dp[i + 1][value] = min(
                        dp[i + 1][value], dp[i + 1][value - coin] + 1
                    )

        return dp[-1][-1] if dp[-1][-1] < inf else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp: List[int] = [inf] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            # print(f"coin={coin}")
            # for value in range(amount, coin-1, -1):
            for value in range(coin, amount + 1):
                # print(f"value={value}")
                if dp[value - coin] < inf:
                    dp[value] = min(dp[value], dp[value - coin] + 1)
                # print(dp)
        # print(dp)
        return dp[-1] if dp[-1] < inf else -1


# @lc code=end

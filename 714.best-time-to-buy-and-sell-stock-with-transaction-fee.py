#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        max_profit = 0
        dp: List[int] = [0] * n
        prev_max_profit = 0
        for buy_day, buy_price in enumerate(prices):
            # print(f"buy_day={buy_day}; buy_price={buy_price}")
            if buy_day >= 1:
                prev_max_profit = max(prev_max_profit, dp[buy_day - 1])
            # print(f"prev_max_profit={prev_max_profit}")
            for sell_day in range(buy_day + 1, n):
                # print(f"sell_day={buy_day}; sell_price={prices[sell_day]}")
                dp[sell_day] = max(
                    dp[sell_day],
                    prices[sell_day] - buy_price - fee + prev_max_profit,
                )
                max_profit = max(max_profit, dp[sell_day])
                # print(dp)

        # print(dp)

        return max_profit


# @lc code=end

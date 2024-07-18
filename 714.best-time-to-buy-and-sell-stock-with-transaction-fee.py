#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#
from typing import List
from math import inf


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        # dp is my max profit for n days with or without any share bought
        dp: List[List[int]] = [[0] * 2 for _ in range(n + 1)]
        dp[0][1] = -inf
        for day, price in enumerate(prices):
            # I have bought a share meaning
            # I buy, the one from today with my max profit from yesterday
            # or I keep the one I bought before yesterday)
            dp[day + 1][1] = max(dp[day][1], dp[day][0] - price)
            # I don't have any share meaning
            # I keep my profit from yesterday
            # or I sell the share I had before yesterday)
            dp[day + 1][0] = max(dp[day][0], dp[day][1] + price - fee)
        # print(dp)

        return max(dp[-1][0], dp[-1][1])


# @lc code=end

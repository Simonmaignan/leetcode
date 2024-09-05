#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        total_profit = 0
        for i in range(1, n):
            buy_price = prices[i - 1]
            sell_price = prices[i]
            total_profit += max(0, sell_price - buy_price)
        return total_profit


# @lc code=end

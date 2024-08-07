#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_day = 0
        sell_day = 1
        while sell_day < len(prices):
            if prices[sell_day] <= prices[buy_day]:
                buy_day = sell_day
            else:
                max_profit = max(
                    max_profit, prices[sell_day] - prices[buy_day]
                )
            sell_day += 1

        return max_profit


# @lc code=end

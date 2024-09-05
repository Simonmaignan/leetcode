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
        dp_buy: List[int] = [0] * n
        dp_buy[0] = prices[0]
        dp_sell: List[int] = [0] * n
        for i in range(1, n):
            dp_buy[i] = max(dp_buy[i - 1], dp_sell[i - 1] - prices[i])
            dp_sell[i] = max(
                dp_sell[i - 1],
                dp_buy[i] + prices[i],
                dp_buy[i - 1] + prices[i],
            )
        # print(dp_buy)
        # print(dp_sell)
        return max(dp_buy[-1], dp_sell[-1])


# @lc code=end

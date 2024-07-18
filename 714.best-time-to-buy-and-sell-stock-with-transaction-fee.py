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
        share = -inf
        no_share = 0
        for price in prices:
            # I have bought a share meaning
            # I buy, the one from today with my max profit from yesterday
            # or I keep the one I bought before yesterday)
            share = max(share, no_share - price)
            # I don't have any share meaning
            # I keep my profit from yesterday
            # or I sell the share I had before yesterday)
            no_share = max(no_share, share + price - fee)

        return no_share


# @lc code=end

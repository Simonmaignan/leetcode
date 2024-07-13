#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#
from typing import List, Tuple


# @lc code=start
class StockSpanner:

    def __init__(self):
        self.stock_list: List[Tuple[int, int]] = []

    def next(self, price: int) -> int:
        span = 1
        while self.stock_list and self.stock_list[-1][0] <= price:
            span += self.stock_list.pop()[1]

        self.stock_list.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end

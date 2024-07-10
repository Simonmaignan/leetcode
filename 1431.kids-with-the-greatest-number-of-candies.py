#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#
from typing import List


# @lc code=start
class Solution:
    def kidsWithCandies(
        self, candies: List[int], extraCandies: int
    ) -> List[bool]:
        result = [False] * len(candies)
        max_candies = max(candies)
        for i, candy in enumerate(candies):
            if candy + extraCandies >= max_candies:
                result[i] = True
        return result


# @lc code=end

#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#
from typing import List


# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        dp: List[int] = [1] * (n + 1)
        dp[0] = 0
        for i in range(3, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
        return dp[n]


# @lc code=end

#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#
from typing import List


# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp_2 = cost[0]
        dp_1 = cost[1]

        for i in range(2, len(cost)):
            dp_next = min(dp_1, dp_2) + cost[i]
            dp_2 = dp_1
            dp_1 = dp_next

        return min(dp_2, dp_1)


# @lc code=end

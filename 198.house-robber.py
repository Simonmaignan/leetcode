#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
from typing import List


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_3 = 0
        rob_2 = 0
        rob_1 = 0
        for cur_rob in nums:
            new_rob = max(rob_3, rob_2) + cur_rob
            rob_3 = rob_2
            rob_2 = rob_1
            rob_1 = new_rob

        return max(rob_1, rob_2, rob_3)


# @lc code=end

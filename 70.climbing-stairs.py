#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        prev_step, cur_step = 1, 1

        for _ in range(2, n + 1):
            prev_step, cur_step = cur_step, prev_step + cur_step

        return cur_step


# @lc code=end

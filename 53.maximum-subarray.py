#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import List

# @lc code=start
from math import inf


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_prefix_sum = 0
        max_sub_array = -inf
        prefix_sum_prev = 0
        prefix_sum_cur = 0
        for num in nums:
            prefix_sum_cur = prefix_sum_prev + num
            max_sub_array = max(max_sub_array, prefix_sum_cur - min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum_cur)
            prefix_sum_prev = prefix_sum_cur

        return max_sub_array


# @lc code=end

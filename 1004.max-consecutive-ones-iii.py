#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#
from typing import List


# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_ones = 0
        for right, num in enumerate(nums):
            # If right at 0
            if not num:
                # with some 0 flip left
                if k > 0:
                    k -= 1
                # without 0 flip left
                else:
                    # Move left until next 0
                    while nums[left]:
                        left += 1
                    # Move left and right one step
                    left += 1
            max_ones = max(max_ones, right - left + 1)
        return max_ones


# @lc code=end

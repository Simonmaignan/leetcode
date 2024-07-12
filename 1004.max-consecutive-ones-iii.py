#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#
from typing import List


# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = right = 0
        max_ones = 0
        while right < n:
            # If right at 1
            if nums[right]:
                right += 1
            # If right at 0, with some 0 flip left
            elif k > 0:
                right += 1
                k -= 1
            # If right at 0, without 0 flip left
            else:
                # Move left until next 0
                while nums[left]:
                    left += 1
                # Move left and right one step
                left += 1
                right += 1
            max_ones = max(max_ones, right - left)
        return max_ones


# @lc code=end

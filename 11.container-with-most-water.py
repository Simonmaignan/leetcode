#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
from typing import List


# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = -1
        while left < right:
            max_water = max(
                max_water, (right - left) * min(height[left], height[right])
            )
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water


# @lc code=end

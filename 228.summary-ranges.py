#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#
from typing import List


# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        left = 0
        ranges: List[str] = []
        n = len(nums)
        if n == 0:
            return ranges

        for i in range(1, n):
            if nums[i] - 1 != nums[i - 1]:
                right = i - 1
                # One number range
                if left == right:
                    ranges.append(str(nums[left]))
                # Multiple number range
                else:
                    ranges.append(f"{nums[left]}->{nums[right]}")
                left = i
        # Handle last range
        right = n - 1
        if left == right:
            ranges.append(str(nums[left]))
        else:
            ranges.append(f"{nums[left]}->{nums[right]}")

        return ranges


# @lc code=end

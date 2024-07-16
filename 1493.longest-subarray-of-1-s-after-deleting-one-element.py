#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#
from typing import List


# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = deleted = longest_subarray = 0
        for right, num in enumerate(nums):
            if not num:
                deleted += 1
            while deleted > 1:
                if not nums[left]:
                    deleted -= 1
                left += 1
            longest_subarray = max(longest_subarray, right - left)

        return longest_subarray


# @lc code=end

#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#
from typing import List


# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        max_operation = 0
        while left < right:
            pair_sum = nums[left] + nums[right]
            if pair_sum == k:
                max_operation += 1
                left += 1
                right -= 1
            elif pair_sum < k:
                left += 1
            else:
                right -= 1
        return max_operation


# @lc code=end

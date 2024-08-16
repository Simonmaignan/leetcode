#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
from typing import List


# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans + 1


# @lc code=end

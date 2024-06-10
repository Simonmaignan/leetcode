#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
from typing import List


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid_idx = (left + right) // 2
            mid = nums[mid_idx]
            # print(f"left={left}, {nums[left]}")
            # print(f"mid={mid_idx}, {mid}")
            # print(f"right={right}, {nums[right]}")
            if mid == target:
                return mid_idx
            # If left side is ascending
            if nums[left] <= mid:
                if nums[left] <= target < mid:
                    right = mid_idx - 1
                else:
                    left = mid_idx + 1
            else:
                if mid < target <= nums[right]:
                    left = mid_idx + 1
                else:
                    right = mid_idx - 1
            # print(f"left={left}")
            # print(f"mid={mid_idx}")
            # print(f"right={right}")

        return -1


# @lc code=end

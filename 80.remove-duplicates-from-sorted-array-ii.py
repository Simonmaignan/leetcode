#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
from typing import List


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums[0] == nums[-1]:
            return 2

        left = 1
        right = len(nums) - 1

        occ_count = 1
        while left <= right:
            if nums[left] == nums[left - 1]:
                occ_count += 1
            else:
                occ_count = 1
            # print(f"left={left}; right={right}; occ={occ_count}")

            if occ_count > 2:
                # Slide
                # print(f"Slide {left} to {right}")
                j = left
                while j < right:
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]
                    j += 1

                occ_count -= 1
                right -= 1
                # print(nums)
            else:
                left += 1

        return left


# @lc code=end

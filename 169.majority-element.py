#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
from typing import List, Optional


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element: Optional[int] = None
        count: int = 0
        for element in nums:
            print(f"element={element}; maj={majority_element}; count={count}")
            if count == 0:
                majority_element = element
            if element == majority_element:
                count += 1
            else:
                count -= 1
            if count > len(nums) / 2:
                return majority_element

        return majority_element


# @lc code=end

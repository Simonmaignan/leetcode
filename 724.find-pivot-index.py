#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#
from typing import List


# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefixes: List[int] = [0] * (n + 1)
        suffixes: List[int] = [0] * (n + 1)
        for i, num in enumerate(nums):
            prefixes[i + 1] = prefixes[i] + num

        for i in range(n - 1, -1, -1):
            suffixes[i] = suffixes[i + 1] + nums[i]

        # print(prefixes)
        # print(suffixes)

        for i in range(n):
            # print(f"i={i}; prefix={prefixes[i]}; suffix={suffixes[i + 1]}")
            if prefixes[i] == suffixes[i + 1]:
                return i

        return -1


# @lc code=end

#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#
from typing import List


# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        j = 1
        k = 2
        while k != n - 1 and j != n - 2 and i != n - 3:
            print(f"i={i}; j={j}; k={k}")
            if nums[i] < nums[j] < nums[k]:
                return True
            if nums[i] > nums[j]:
                if nums[i + 1] > nums[i]:
                    i += 1
                else:
                    j += 1
            elif nums[j] > nums[k]:
                if nums[j + 1] > nums[j]:
                    j += 1
                else:
                    k += 1
            while j <= i:
                j += 1
            while k <= j:
                k += 1

        return False


# @lc code=end

#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from typing import List


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        products_except: List[int] = [nums[0]]
        for i in range(1, n):
            products_except.append(products_except[-1] * nums[i])

        suffix_product = 1
        for i in range(n - 1, 0, -1):
            products_except[i] = products_except[i - 1] * suffix_product
            suffix_product *= nums[i]
        products_except[0] = suffix_product
        return products_except


# @lc code=end

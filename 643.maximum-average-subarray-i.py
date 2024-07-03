#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#
from typing import List


# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = cur_sum = sum(nums[:k])
        n = len(nums)
        right = k
        for right in range(k, n):
            left = right - k
            cur_sum += nums[right]
            cur_sum -= nums[left]
            max_sum = max(cur_sum, max_sum)
        return max_sum / k


# @lc code=end

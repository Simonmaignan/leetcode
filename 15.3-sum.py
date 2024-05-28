#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
from typing import List


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        three_sum_list: List[List[int]] = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            # print(f"i; nums[{i}]={nums[i]}")
            while left < right:
                # print(f"left; nums[{left}]={nums[left]}")
                # print(f"right; nums[{right}]={nums[right]}")
                if left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                elif right < n - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                elif nums[left] + nums[right] + nums[i] == 0:
                    # print([nums[i], nums[left], nums[right]])
                    three_sum_list.append([nums[i], nums[left], nums[right]])
                    left += 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    right -= 1
        return three_sum_list


# @lc code=end

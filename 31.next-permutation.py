#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
from typing import List, Tuple


# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        def dfs(start_index: int) -> Tuple[int, int]:
            if start_index < 0:
                return -1, -1
            print(f"start_index={start_index}")
            for i in range(start_index - 1, -1, -1):
                print(f"i={i}")
                if nums[start_index] > nums[i]:
                    return start_index, i
            return dfs(start_index - 1)

        idx_1, idx_2 = dfs(n - 1)
        if (idx_1, idx_2) == (-1, -1):
            nums.sort()
        else:
            nums[idx_1], nums[idx_2] = nums[idx_2], nums[idx_1]


# @lc code=end

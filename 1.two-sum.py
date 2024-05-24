#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import Dict, List


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map: Dict[int, int] = {element: idx for idx, element in enumerate(nums)}
        # print(hash_map)
        for i, element in enumerate(nums):
            rest: int = target - element
            if rest in hash_map and hash_map[rest] != i:
                return [i, hash_map[rest]]


# @lc code=end

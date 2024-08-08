#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import Dict, List


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map: Dict[int, int] = {}
        # print(hash_map)
        for i, element in enumerate(nums):
            complement: int = target - element
            if complement in hash_map:
                return [i, hash_map[complement]]
            hash_map[element] = i


# @lc code=end

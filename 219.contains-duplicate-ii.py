#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
from collections import defaultdict
from typing import Dict, List


# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict: Dict[int, List[int]] = defaultdict(list)
        for i, num in enumerate(nums):
            for j in nums_dict[num]:
                if abs(i - j) <= k:
                    return True
            nums_dict[num].append(i)
        return False


# @lc code=end

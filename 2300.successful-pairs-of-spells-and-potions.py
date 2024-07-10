#
# @lc app=leetcode id=2300 lang=python3
#
# [2300] Successful Pairs of Spells and Potions
#
from typing import List
from bisect import bisect_left


# @lc code=start
class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        m = len(potions)
        pairs: List[bool] = []
        for spell in spells:
            min_potion = success / spell
            i = bisect_left(potions, min_potion)
            pairs.append(m - i)
        return pairs


# @lc code=end

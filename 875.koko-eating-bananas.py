#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
from typing import List


# @lc code=start
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_all_bananas(k: int) -> bool:
            # print(f"can eat all bananas with {k} speed?")
            eating_h = 0
            for pile in piles:
                # print(f"pile={pile}")
                eating_h += ceil(pile / k)
                # print(f"eating_h={eating_h}")
                if eating_h > h:
                    # print("no")
                    return False
            # print("yes")
            return True

        k_left = 1
        k_right = max(piles)
        min_k = k_right
        while k_left <= k_right:
            k_mid = (k_left + k_right) // 2
            if can_eat_all_bananas(k_mid):
                min_k = k_mid
                k_right = k_mid - 1
            else:
                k_left = k_mid + 1

        return min_k


# @lc code=end

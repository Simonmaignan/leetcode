#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#
from typing import List


# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i, flower in enumerate(flowerbed):

            if (
                not flower
                and (i == 0 or not flowerbed[i - 1])
                and (i == len(flowerbed) - 1 or not flowerbed[i + 1])
            ):
                flowerbed[i] = 1
                n -= 1
                # print(flowerbed)
                # print(n)
                if n == 0:
                    return True
        return False


# @lc code=end

#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
from typing import List


# @lc code=start
class Solution:
    def countBits_(self, n: int) -> List[int]:
        ans: List[int] = []
        for i in range(n + 1):
            nb_ones = 0
            for bit in f"{i:b}":
                if bit == "1":
                    nb_ones += 1
            ans.append(nb_ones)
        return ans

    def countBits(self, n: int) -> List[int]:
        ans: List[int] = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i & (i - 1)] + 1
        return ans


# @lc code=end

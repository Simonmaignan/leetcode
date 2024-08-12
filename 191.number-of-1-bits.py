#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#


# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        nb_set_bits = 0
        while n > 0:
            nb_set_bits += n % 2
            n = n // 2
        return nb_set_bits


# @lc code=end

#
# @lc app=leetcode id=1318 lang=python3
#
# [1318] Minimum Flips to Make a OR b Equal to c
#


# @lc code=start
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a_bin = bin(a)[2:]
        b_bin = bin(b)[2:]
        c_bin = bin(c)[2:]
        n_max = max(len(a_bin), len(b_bin), len(c_bin))
        a_bin = a_bin.zfill(n_max)
        b_bin = b_bin.zfill(n_max)
        c_bin = c_bin.zfill(n_max)
        # print(a_bin)
        # print(b_bin)
        # print(c_bin)

        min_flips = 0

        for i, a_i in enumerate(a_bin):
            if c_bin[i] == "1" and b_bin[i] == "0" and a_i == "0":
                min_flips += 1
            if c_bin[i] == "0":
                if b_bin[i] == "1":
                    min_flips += 1
                if a_i == "1":
                    min_flips += 1

        return min_flips


# @lc code=end

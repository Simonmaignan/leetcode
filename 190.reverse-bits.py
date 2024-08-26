#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#


# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        n_bits = f"{n:b}".zfill(32)
        print(n_bits)
        for i in range(len(n_bits) - 1, -1, -1):
            print(f"i={i}; bit={n_bits[i]}")
            ans += int(n_bits[i]) * 2**i
        return ans


# @lc code=end

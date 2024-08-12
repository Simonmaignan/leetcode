#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
from typing import List


# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_i = len(a) - 1
        b_i = len(b) - 1
        add_binary: List[int] = []
        carry = 0
        while a_i >= 0 or b_i >= 0:
            # print(f"a_i={a_i}; b_i={b_i}")
            a_bit = b_bit = 0
            if a_i >= 0:
                a_bit = int(a[a_i])
            if b_i >= 0:
                b_bit = int(b[b_i])
            # print(f"a_bit={a_bit}; b_bit={b_bit}; carry={carry}")
            sum_bit = a_bit + b_bit + carry
            # print(f"sum={sum_bit}")
            add_binary.append(str(sum_bit % 2))
            # print(add_binary)
            carry = sum_bit // 2
            a_i -= 1
            b_i -= 1

        if carry:
            add_binary.append("1")
        return "".join(reversed(add_binary))


# @lc code=end

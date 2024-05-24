#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#


# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        # print(f"n={n}")

        # Skip white spaces
        while i < n and s[i] == " ":
            i += 1

        # Check sign
        negative = False
        if i < n and s[i] in ["-", "+"]:
            negative = s[i] == "-"
            # print(negative)
            i += 1

        left = i
        # print(f"left={left}")
        while left < n and s[left].isnumeric():
            left += 1
        left -= 1
        # print(f"left={left}")

        power_10 = 0
        number = 0
        # print(f"i={i}")
        while left >= i:
            number += int(s[left]) * 10**power_10
            # print(f"number={number}")
            left -= 1
            power_10 += 1

        return min(number, 2**31 - 1) if not negative else max(-number, -(2**31))


# @lc code=end

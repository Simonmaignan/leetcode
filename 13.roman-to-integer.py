#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
from typing import Dict


# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_map: Dict[str, int] = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        converted_integer = 0
        for i, c in enumerate(s):
            converted_roman = roman_to_int_map[c]
            if i + 1 < len(s) and roman_to_int_map[s[i + 1]] > converted_roman:
                converted_integer -= converted_roman
            else:
                converted_integer += converted_roman
        return converted_integer


# @lc code=end

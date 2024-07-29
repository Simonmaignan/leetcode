#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
from typing import Dict, List


# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list: List[str] = s.split()
        if len(pattern) != len(s_list):
            return False
        pattern_dict: Dict[str, str] = dict()
        s_dict: Dict[str, str] = dict()
        for char, word in zip(pattern, s_list):
            # print(f"char={char}, word={word}")
            # print(f"pattern_dict={pattern_dict}, s_dict={s_dict}")
            if (char in pattern_dict and pattern_dict[char] != word) or (
                word in s_dict and s_dict[word] != char
            ):
                return False
            pattern_dict[char] = word
            s_dict[word] = char
        return True


# @lc code=end

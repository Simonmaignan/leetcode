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
            if char not in pattern_dict:
                if word in s_dict:
                    return False
                pattern_dict[char] = word
            elif pattern_dict[char] != word:
                return False
            if word not in s_dict:
                s_dict[word] = char

        return True


# @lc code=end

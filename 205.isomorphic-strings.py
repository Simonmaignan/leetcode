#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
from typing import Dict, Set


# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map: Dict[str, str] = {}
        already_mapped_char: Set[str] = set()
        for i, char in enumerate(s):
            if char in char_map:
                if char_map[char] != t[i]:
                    return False
            else:
                if t[i] in already_mapped_char:
                    return False
                char_map[char] = t[i]
                already_mapped_char.add(t[i])

        return True


# @lc code=end

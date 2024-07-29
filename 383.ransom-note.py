#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
from typing import Dict
from collections import defaultdict


# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter: Dict[str, int] = defaultdict(int)
        for letter in magazine:
            magazine_counter[letter] += 1
        for note in ransomNote:
            if magazine_counter[note] <= 0:
                return False
            magazine_counter[note] -= 1
        return True


# @lc code=end

#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#
from typing import List


# @lc code=start
class Solution:
    def removeStars(self, s: str) -> str:
        stack: List[str] = []
        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)


# @lc code=end

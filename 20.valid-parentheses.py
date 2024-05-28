#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
from typing import Dict, List


# @lc code=start
class Solution:
    parenthesis_match: Dict[str, str] = {"(": ")", "[": "]", "{": "}"}

    def isValid(self, s: str) -> bool:
        parentheses_stack: List[str] = []
        for parenthesis in s:
            if parenthesis in self.parenthesis_match:
                parentheses_stack.append(parenthesis)
            else:
                last_opened_parenthesis = (
                    parentheses_stack.pop() if parentheses_stack else ""
                )
                if parenthesis != self.parenthesis_match.get(
                    last_opened_parenthesis, ""
                ):
                    return False

        return not parentheses_stack


# @lc code=end

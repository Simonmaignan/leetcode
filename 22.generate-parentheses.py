#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
from typing import List


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis_list: List[str] = []

        def dfs(count_open: int, count_closed: int, parenthesis: List[str]) -> None:
            if count_open == n and count_closed == n:
                parenthesis_list.append("".join(parenthesis))
                return
            if count_open < n:
                parenthesis.append("(")
                dfs(count_open + 1, count_closed, parenthesis)
                parenthesis.pop()
            if count_closed < count_open:
                parenthesis.append(")")
                dfs(count_open, count_closed + 1, parenthesis)
                parenthesis.pop()

        dfs(0, 0, [])
        return parenthesis_list


# @lc code=end

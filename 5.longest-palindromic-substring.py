#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
from typing import List, Tuple


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp: List[List[bool]] = [[False] * n for _ in range(n)]
        ans: Tuple[int] = (0, 0)

        for i in range(n):
            dp[i][i] = True
            if i < (n - 1) and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = (i, i + 1)

        for diff in range(2, n):
            for left in range(n - diff):
                right = left + diff
                # print(f"left={left} - right={right}")
                # print(s[left : right + 1])
                if s[left] == s[right] and dp[left + 1][right - 1]:
                    dp[left][right] = True
                    ans = (left, right)
                    # print(ans)
        # pprint(dp)
        return s[ans[0] : ans[1] + 1]


# @lc code=end

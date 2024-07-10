#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#


# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p_s = p_t = 0
        n_s = len(s)
        n_t = len(t)
        while p_s < n_s and p_t < n_t:
            # print(f"s[{p_s}]={s[p_s]} - t[{p_t}]={t[p_t]}")
            if s[p_s] == t[p_t]:
                # print(f"s[{p_s}]={s[p_s]} - t[{p_t}]={t[p_t]}")
                p_s += 1
            p_t += 1

        return p_s == n_s


# @lc code=end

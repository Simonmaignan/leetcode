#
# @lc app=leetcode id=1653 lang=python3
#
# [1653] Minimum Deletions to Make String Balanced
#
from typing import List


# @lc code=start
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        prefix_nb_b: List[int] = [0] * n
        suffix_nb_a: List[int] = [0] * n
        for i in range(1, n):
            prefix_nb_b[i] = prefix_nb_b[i - 1] + int(s[i - 1] == "b")
            suffix_nb_a[-i - 1] = suffix_nb_a[-i] + int(s[-i] == "a")

        min_deletion = n
        for i in range(n):
            min_deletion = min(min_deletion, prefix_nb_b[i] + suffix_nb_a[i])
        print(prefix_nb_b)
        print(suffix_nb_a)

        return min_deletion


# @lc code=end

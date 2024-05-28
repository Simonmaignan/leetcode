#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#
from typing import List, Tuple


# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def count_1s_and_0s(string: str) -> Tuple[int]:
            nb_1s, nb_0s = 0, 0
            for c in string:
                if c == "0":
                    nb_0s += 1
                else:
                    nb_1s += 1

            return nb_0s, nb_1s

        ns = len(strs)
        strs_01: List[Tuple[int]] = [count_1s_and_0s(string) for string in strs]

        dp: List[List[List[int]]] = [
            [[-1] * (n + 1) for _ in range(m + 1)] for _ in range(ns + 1)
        ]

        def dfs(start_idx: int, nb_0s: int, nb_1s: int) -> int:
            if start_idx == ns:
                return 0
            if dp[start_idx][nb_0s][nb_1s] >= 0:
                return dp[start_idx][nb_0s][nb_1s]

            largest_subset_size = dfs(start_idx + 1, nb_0s, nb_1s)
            if (
                nb_0s + strs_01[start_idx][0] <= m
                and nb_1s + strs_01[start_idx][1] <= n
            ):
                largest_subset_size = max(
                    largest_subset_size,
                    dfs(
                        start_idx + 1,
                        nb_0s + strs_01[start_idx][0],
                        nb_1s + strs_01[start_idx][1],
                    )
                    + 1,
                )

            dp[start_idx][nb_0s][nb_1s] = largest_subset_size
            return largest_subset_size

        return dfs(0, 0, 0)


# @lc code=end

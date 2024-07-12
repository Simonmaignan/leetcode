#
# @lc app=leetcode id=2542 lang=python3
#
# [2542] Maximum Subsequence Score
#
from typing import List


# @lc code=start
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)

        def dfs(
            cur_i: int, k_left: int, sum1: int, min2: int, max_score: int
        ) -> int:
            # print(
            #     f"cur_i={cur_i}; k_left={k_left}; sum1={sum1}; min2={min2}; max_score={max_score}"
            # )
            if (cur_i + k_left) > n:
                return max_score
            if k_left == 0:
                return max(max_score, sum1 * min2)

            # Use cur_i
            max_score = dfs(
                cur_i + 1,
                k_left - 1,
                sum1 + nums1[cur_i],
                min(min2, nums2[cur_i]),
                max_score,
            )
            # Do not use cur_i
            max_score = dfs(cur_i + 1, k_left, sum1, min2, max_score)

            return max_score

        return dfs(0, k, 0, 10**5, 0)


# @lc code=end

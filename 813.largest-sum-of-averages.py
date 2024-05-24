#
# @lc app=leetcode id=813 lang=python3
#
# [813] Largest Sum of Averages
#
from typing import List


# @lc code=start
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix_nums: List[int] = [0] * (n + 1)
        for i, num in enumerate(nums):
            prefix_nums[i + 1] = prefix_nums[i] + num
        # print(f"prefix_nums={prefix_nums}")

        dp: List[List[int]] = [[0] * k for _ in range(n + 1)]

        def dfs(start_i: int, nb_subarray: int) -> int:
            # print(f"start_i={start_i}; nb_subarray={nb_subarray}")
            if start_i >= n:
                return 0
            if nb_subarray == k - 1:
                # print(f"rest={prefix_nums[-1] - prefix_nums[start_i]} by {n - start_i}")
                return (prefix_nums[-1] - prefix_nums[start_i]) / (n - start_i)
            if dp[start_i][nb_subarray] != 0:
                return dp[start_i][nb_subarray]

            max_sum_avg = 0
            for j in range(start_i + 1, n + 1):
                tmp = dfs(j, nb_subarray + 1)
                # print(
                #     f"start_i={start_i}; j={j}; dfs={tmp}; prefix {prefix_nums[j] - prefix_nums[start_i]} by {j - start_i}"
                # )

                max_sum_avg = max(
                    max_sum_avg,
                    tmp + (prefix_nums[j] - prefix_nums[start_i]) / (j - start_i),
                )
            # print(
            #     f"start_i={start_i}; nb_subarray={nb_subarray}; max_sum_avg={max_sum_avg}"
            # )
            dp[start_i][nb_subarray] = max_sum_avg
            return max_sum_avg

        return dfs(0, 0)


# @lc code=end

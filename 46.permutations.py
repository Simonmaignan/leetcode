#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from typing import List


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations: List[List[int]] = []
        n = len(nums)
        visited: List[bool] = [False] * n

        def dfs(start_index: int, permutation: List[int]) -> None:
            if start_index == n:
                permutations.append(permutation[:])
                return
            for idx, num in enumerate(nums):
                if visited[idx]:
                    continue
                permutation.append(num)
                visited[idx] = True
                dfs(start_index + 1, permutation)
                visited[idx] = False
                permutation.pop()

        dfs(0, [])
        return permutations


# @lc code=end

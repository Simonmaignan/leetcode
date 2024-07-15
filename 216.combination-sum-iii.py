#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
from typing import List


# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(
            start_num: int,
            cur_sum: int,
            cur_comb: List[int],
            combinations: List[List[int]],
        ) -> None:
            m = len(cur_comb)
            if m > k or m == k and cur_sum != n:
                return
            # print(f"start_i={start_num};cur_sum={cur_sum};cur_comb={cur_comb}")
            if cur_sum > n:
                return
            if cur_sum == n:
                if m == k:
                    combinations.append(cur_comb[:])
                    # print(f"combinations={combinations}")
                return

            for num in range(start_num, 10):
                if (cur_sum + num) > n or (
                    (cur_sum + num) == n and m < (k - 1)
                ):
                    break
                cur_comb.append(num)
                dfs(num + 1, cur_sum + num, cur_comb, combinations)
                cur_comb.pop()

        ans: List[List[int]] = []
        dfs(1, 0, [], ans)
        return ans


# @lc code=end

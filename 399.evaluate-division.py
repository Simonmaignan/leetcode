#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
from typing import Dict, List, Tuple, Set
from collections import defaultdict


# @lc code=start
class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        variables_relations: Dict[str, List[Tuple[str, float]]] = defaultdict(
            list
        )
        for i, (a, b) in enumerate(equations):
            value = values[i]
            variables_relations[a].append((b, value))
            variables_relations[b].append((a, 1 / value))
        # print(variables_relations)

        def resolve_division(num: str, denom: str, visited: Set[str]) -> float:
            # print(f"resolve {num}/{denom}")
            if num == denom:
                return 1.0
            for related_var, multiplicand in variables_relations[num]:
                if related_var not in visited:
                    visited.add(related_var)
                    division = resolve_division(related_var, denom, visited)
                    if division >= 0.0:
                        return multiplicand * division

            return -1.0

        ans: List[int] = []
        for c, d in queries:
            # print(f"query {c}/{d}")
            if c not in variables_relations or d not in variables_relations:
                ans.append(-1.0)
            else:
                ans.append(resolve_division(c, d, set([c])))
        return ans


# @lc code=end

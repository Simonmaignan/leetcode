#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#
from typing import List, Set
from collections import Counter


# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        occurrences: Set[int] = set()
        for occurrence in counter.values():
            if occurrence in occurrences:
                return False
            occurrences.add(occurrence)
        return True


# @lc code=end

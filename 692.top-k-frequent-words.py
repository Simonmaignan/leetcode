#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#
from typing import List, Tuple
from collections import Counter

# @lc code=start
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_counter = Counter(words)
        heap: List[Tuple[int, str]] = []
        for word, count in words_counter.items():
            heapq.heappush(heap, (-count, word))

        return [heapq.heappop(heap)[1] for _ in range(k)]


# @lc code=end

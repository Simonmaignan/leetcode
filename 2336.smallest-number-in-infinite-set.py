#
# @lc app=leetcode id=2336 lang=python3
#
# [2336] Smallest Number in Infinite Set
#
from typing import List, Set

# @lc code=start
import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.heap: List[int] = [1]
        self.popped_numbers: Set[int] = set()

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.heap)
        self.popped_numbers.add(smallest)
        if not self.heap:
            self.heap.append(smallest + 1)
        return smallest

    def addBack(self, num: int) -> None:
        if num in self.popped_numbers:
            heapq.heappush(self.heap, num)
            self.popped_numbers.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end

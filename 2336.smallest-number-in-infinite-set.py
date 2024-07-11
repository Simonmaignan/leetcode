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
        self.set: Set[int] = set([1])

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.heap)
        self.set.remove(smallest)
        if not self.heap:
            self.heap.append(smallest + 1)
            self.set.add(smallest + 1)
        return smallest

    def addBack(self, num: int) -> None:
        largest = heapq.nlargest(1, self.heap)[0]
        if num < largest and num not in self.set:
            heapq.heappush(self.heap, num)
            self.set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end

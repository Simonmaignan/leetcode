#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#
from typing import List


# @lc code=start
class RecentCounter:

    def __init__(self):
        self.call_queue: List[int] = []

    def ping(self, t: int) -> int:
        self.call_queue.append(t)
        nb_calls = 0
        call_i = len(self.call_queue) - 1
        while call_i >= 0 and self.call_queue[call_i] >= t - 3000:
            nb_calls += 1
            call_i -= 1
        return nb_calls


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

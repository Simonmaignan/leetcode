#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#


# @lc code=start
from collections import deque


class RecentCounter:

    def __init__(self):
        self.call_queue = deque()

    def ping(self, t: int) -> int:
        # print(f"ping {t}")
        self.call_queue.append(t)
        while self.call_queue[0] < t - 3000:
            self.call_queue.popleft()
            # print(f"pop {self.call_queue.popleft()}")
        return len(self.call_queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

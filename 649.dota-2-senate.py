#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#
from collections import deque


# @lc code=start
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        d_queue = deque()
        r_queue = deque()

        for i, senator in enumerate(senate):
            # print(f"senator={senator}")
            if senator == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)
        # print(f"Radiant senators = {r_queue}")
        # print(f"Dire senators = {d_queue}")
        while r_queue and d_queue:
            # print(f"Radiant senators = {r_queue}")
            # print(f"Dire senators = {d_queue}")
            if r_queue[0] < d_queue[0]:
                # print(f"Next Radiant senator={next_senator}")
                r_queue.append(r_queue[0] + n)
            else:
                # print(f"Next Dire senator={next_senator}")
                d_queue.append(d_queue[0] + n)
            d_queue.popleft()
            r_queue.popleft()
        return "Radiant" if r_queue else "Dire"


# @lc code=end

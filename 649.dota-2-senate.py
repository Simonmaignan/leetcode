#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#
from collections import deque


# @lc code=start
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_bans = d_bans = 0
        d_queue = deque()
        r_queue = deque()

        for i, senator in enumerate(senate):
            # print(f"senator={senator}")
            if senator == "R":
                if r_bans == 0:
                    d_bans += 1
                    r_queue.append(i)
                else:
                    r_bans -= 1
            else:
                if d_bans == 0:
                    r_bans += 1
                    d_queue.append(i)
                else:
                    d_bans -= 1
        # print(f"Radiant senators = {r_queue}")
        # print(f"Dire senators = {d_queue}")
        while r_queue and d_queue:
            # print("New round")
            next_d_queue = deque()
            next_r_queue = deque()
            while r_queue or d_queue:
                # print(f"Radiant senators = {r_queue}")
                # print(f"Dire senators = {d_queue}")
                if (
                    r_queue
                    and not d_queue
                    or (r_queue and r_queue[0] < d_queue[0])
                ):
                    next_senator = r_queue.popleft()
                    # print(f"Next Radiant senator={next_senator}")
                    if r_bans == 0:
                        d_bans += 1
                        next_r_queue.append(next_senator)
                    else:
                        r_bans -= 1
                else:
                    next_senator = d_queue.popleft()
                    # print(f"Next Dire senator={next_senator}")
                    if d_bans == 0:
                        r_bans += 1
                        next_d_queue.append(next_senator)
                    else:
                        d_bans -= 1
            r_queue = next_r_queue
            d_queue = next_d_queue
        return "Radiant" if r_queue else "Dire"


# @lc code=end

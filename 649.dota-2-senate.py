#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#


# @lc code=start
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_votes = d_votes = 0
        r_bans = d_bans = 0

        for senator in senate:
            print(f"senator={senator}")
            if senator == "R":
                if r_bans == 0:
                    d_bans += 1
                    r_votes += 1
                else:
                    r_bans -= 1
            else:
                if d_bans == 0:
                    r_bans += 1
                    d_votes += 1
                else:
                    d_bans -= 1
            print(f"Radiants={r_votes} - {r_bans}")
            print(f"Dire={d_votes} - {d_bans}")
        r_votes -= r_bans
        d_votes -= d_bans
        return "Radiant" if r_votes > d_votes else "Dire"


# @lc code=end

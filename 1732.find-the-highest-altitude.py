#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#
from typing import List


# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        highest_altitude = 0
        for altitude_gain in gain:
            current_altitude += altitude_gain
            highest_altitude = max(highest_altitude, current_altitude)

        return highest_altitude


# @lc code=end

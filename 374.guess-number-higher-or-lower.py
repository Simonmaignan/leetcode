#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#
def guess(num: int) -> int:
    pass


# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n
        while True:
            pick = (left + right) // 2
            if guess(pick) == 0:
                return pick
            if guess(pick) < 0:
                right = pick - 1
            else:
                left = pick + 1


# @lc code=end

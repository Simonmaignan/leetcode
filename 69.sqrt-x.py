#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#


# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        ans: int = -1
        while left < right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                ans = mid
                left = mid
            else:
                right = mid - 1
        return ans


# @lc code=end

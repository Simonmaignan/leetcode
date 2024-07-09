#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#


# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)

        def divides_both_str(divider: str) -> bool:
            n = len(divider)
            left = 0
            right = n
            while right <= n1:
                if str1[left:right] != divider:
                    return False
                left = right
                right = left + n

            if left != n1:
                return False

            left = 0
            right = n
            while right <= n2:
                if str2[left:right] != divider:
                    return False
                left = right
                right = left + n

            if left != n2:
                return False

            return True

        gcd = ""
        left = 0
        while left < n1 and left < n2:
            if str1[left] != str2[left]:
                return gcd
            if divides_both_str(str1[: left + 1]):
                gcd = str1[: left + 1]
            left += 1
        return gcd


# @lc code=end

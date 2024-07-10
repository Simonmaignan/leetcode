#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#


# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ("a", "e", "i", "o", "u")
        s_list = list(s)
        # print(s_list)
        left = 0
        right = len(s) - 1
        while left < right:
            # print(f"left={left}")
            if (
                s_list[left].lower() in vowels
                and s_list[right].lower() in vowels
            ):
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
                print(
                    f"switch s[{left}]={s_list[left]} and s[{right}]={s_list[right]}"
                )
            elif s_list[left].lower() not in vowels:
                left += 1
            elif s_list[right].lower() not in vowels:
                right -= 1
        return "".join(s_list)


# @lc code=end

#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#


# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        cur_nb_vowels = 0
        for right in range(k):
            if s[right] in vowels:
                cur_nb_vowels += 1

        max_nb_vowels = cur_nb_vowels
        for right in range(k, len(s)):
            left = right - k
            if s[right] in vowels:
                cur_nb_vowels += 1
            if s[left] in vowels:
                cur_nb_vowels -= 1
            max_nb_vowels = max(max_nb_vowels, cur_nb_vowels)

        return max_nb_vowels


# @lc code=end

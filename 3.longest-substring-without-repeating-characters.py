#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest_substring = 0
        substring_set = set()
        for right, c_r in enumerate(s):
            while c_r in substring_set:
                substring_set.remove(s[left])
                left += 1
            substring_set.add(c_r)
            longest_substring = max(longest_substring, right - left + 1)
        return longest_substring


# @lc code=end

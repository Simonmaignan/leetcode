#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#
from typing import List


# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        left = right = write = 0
        while right < n:
            while right < n and chars[right] == chars[left]:
                right += 1
            nb_consecutive_char = right - left
            # Write letter
            chars[write] = chars[left]
            write += 1
            if nb_consecutive_char > 1:
                # Write digits
                nb_consecutive_char_str = str(nb_consecutive_char)
                for digit_char in nb_consecutive_char_str:
                    chars[write] = digit_char
                    write += 1

            left = right

        return write


# @lc code=end

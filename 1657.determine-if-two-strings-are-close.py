#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#
from collections import Counter


# @lc code=start
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n1 = len(word1)
        n2 = len(word2)

        if n1 != n2:
            return False

        count1 = Counter(word1)
        print(count1)
        count2 = Counter(word2)
        print(count2)

        if count1 == count2:
            return True

        nb_occ1 = sorted(count1.values())
        unique_char1 = count1.keys()
        print(nb_occ1)
        print(unique_char1)
        nb_occ2 = sorted(count2.values())
        unique_char2 = count2.keys()
        print(nb_occ2)
        print(unique_char2)

        if nb_occ1 == nb_occ2 and unique_char1 == unique_char2:
            return True

        return False


# @lc code=end

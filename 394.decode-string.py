#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#


# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        self.start_index = 0

        def recurse() -> str:
            # print(f"start index={self.start_index}")
            current_char = s[self.start_index]

            if current_char.isalpha():
                self.start_index += 1
                return current_char

            if current_char.isdigit():
                end_of_digit = self.start_index + 1
                while s[end_of_digit].isdigit():
                    end_of_digit += 1

                demultiplier = int(s[self.start_index : end_of_digit])
                self.start_index = end_of_digit
                # Skip [
                self.start_index += 1
                encoded_string = ""
                while s[self.start_index] != "]":
                    encoded_string += recurse()
                self.start_index += 1
                return demultiplier * encoded_string

        decoded_string = ""
        while self.start_index < n:
            decoded_string += recurse()
        return decoded_string


# @lc code=end

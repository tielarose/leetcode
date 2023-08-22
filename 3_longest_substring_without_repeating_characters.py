# Given a string s, find the length of the longest
# substring
#  without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


# first approach: use a dictionary to record how many times a character appears in the current window's substring; if the added character is a duplicate, contract the window until there are no duplicates anymore
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = left = 0

        letters_count = defaultdict(int)

        for right in range(len(s)):
            right_char = s[right]

            letters_count[right_char] += 1

            while letters_count[right_char] > 1:
                left_char = s[left]
                letters_count[left_char] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans


# optimized approach: instead of storing the count of each character, store it's last seen index. When a duplicate is encountered, contract the window to the left of where that character was last seen
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = left = 0

        ind_of_chars = defaultdict(int)

        for right in range(len(s)):
            right_char = s[right]

            # check if the character has been seen before in the current window
            if (right_char in ind_of_chars) and (ind_of_chars[right_char] >= left):
                left = ind_of_chars[right_char] + 1
                ind_of_chars[right_char] = right
            else:
                ind_of_chars[right_char] = right

            ans = max(ans, right - left + 1)

        return ans

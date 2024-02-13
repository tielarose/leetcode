# Given a string s and an integer k, return the length of the longest
# substring
#  of s that contains at most k distinct characters.


# Example 1:

# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.
# Example 2:

# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.


# Constraints:

# 1 <= s.length <= 5 * 104
# 0 <= k <= 50

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = ans = 0

        for right in range(len(s)):
            count[s[right]] += 1

            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            ans = max(ans, right - left + 1)

        return ans

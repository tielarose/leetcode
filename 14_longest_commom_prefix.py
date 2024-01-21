# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = []

        strs = sorted(strs)
        first_word = strs[0]
        last_word = strs[-1]

        for i in range(min(len(first_word), len(last_word))):
            if first_word[i] != last_word[i]:
                return "".join(common_prefix)
            common_prefix.append(first_word[i])

        return "".join(common_prefix)

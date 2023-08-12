# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.


# Example 1:


# Input: text = "nlaebolko"
# Output: 1
# Example 2:


# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0


# Constraints:

# 1 <= text.length <= 104
# text consists of lower case English letters only.

from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters_count = defaultdict(int)

        for letter in text:
            letters_count[letter] += 1

        return min(
            letters_count["b"],
            letters_count["a"],
            letters_count["n"],
            letters_count["l"] // 2,
            letters_count["o"] // 2,
        )

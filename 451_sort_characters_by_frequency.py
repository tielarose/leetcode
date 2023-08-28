# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.


# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.


# Constraints:

# 1 <= s.length <= 5 * 105
# s consists of uppercase and lowercase English letters and digits.

# first attempt
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        letter_count = Counter(s)

        letter_count_tuples = [(letter_count[x], x) for x in letter_count]

        letter_count_tuples.sort(reverse=True)

        final_string = ""

        for count, letter in letter_count_tuples:
            final_string += letter * count

        return final_string


# refactored to avoid creating a new string every time I iterate over a tuple
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        letter_count = Counter(s)

        letter_count_tuples = [(letter_count[x], x) for x in letter_count]

        letter_count_tuples.sort(reverse=True)

        sorted_string_chars = []

        for count, letter in letter_count_tuples:
            sorted_string_chars.append(letter * count)

        return "".join(sorted_string_chars)


# using most_common()
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        letter_counts = Counter(s)

        sorted_string_chars = []

        for letter, count in letter_counts.most_common():
            sorted_string_chars.append(letter * count)

        return "".join(sorted_string_chars)


# O(n) solution using a bucket sort
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        letter_counts = Counter(s)
        max_freq = max(letter_counts.values())

        # bucket sort by frequency
        buckets = [[] for x in range(max_freq + 1)]
        for char, freq in letter_counts.items():
            buckets[freq].append(char)

        # build the string
        string_builder = []
        for i in range(len(buckets) - 1, 0, -1):
            chars = buckets[i]
            for char in chars:
                string_builder.append(char * i)

        return "".join(string_builder)

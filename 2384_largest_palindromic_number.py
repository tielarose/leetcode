# You are given a string num consisting of digits only.

# Return the largest palindromic integer (in the form of a string) that can be formed using digits taken from num. It should not contain leading zeroes.

# Notes:

# You do not need to use all the digits of num, but you must use at least one digit.
# The digits can be reordered.


# Example 1:

# Input: num = "444947137"
# Output: "7449447"
# Explanation:
# Use the digits "4449477" from "444947137" to form the palindromic integer "7449447".
# It can be shown that "7449447" is the largest palindromic integer that can be formed.
# Example 2:

# Input: num = "00009"
# Output: "9"
# Explanation:
# It can be shown that "9" is the largest palindromic integer that can be formed.
# Note that the integer returned should not contain leading zeroes.


# Constraints:

# 1 <= num.length <= 105
# num consists of digits.

from collections import Counter


class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = Counter(num)
        outer = []
        middle = ""

        for digit_str in sorted(count.keys(), reverse=True):
            # if the count is odd, replace the middle if this is larger
            if count[digit_str] % 2 == 1:
                middle = max(middle, digit_str)
            # add half the digits to the outer part of the palindrome
            outer_num = count[digit_str] // 2
            if outer_num > 0:
                outer.append(digit_str * outer_num)

        if outer and int(outer[0][0]) == 0:
            outer = outer[1:]
        first = "".join(outer[:])
        last = "".join(outer[::-1])

        ans = (first + middle + last) or "0"

        return ans

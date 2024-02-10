# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.


# Example 1:

# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s_list = [*s]

        left = 0
        right = len(s) - 1

        while left < right:
            if not s_list[left].isalpha():
                left += 1
                continue
            if not s_list[right].isalpha():
                right -= 1
                continue

            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        return "".join(s_list)

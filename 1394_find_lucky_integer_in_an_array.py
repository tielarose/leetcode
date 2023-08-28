# Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

# Return the largest lucky integer in the array. If there is no lucky integer return -1.


# Example 1:

# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:

# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
# Example 3:

# Input: arr = [2,2,2,3,3]
# Output: -1
# Explanation: There are no lucky numbers in the array.


# Constraints:

# 1 <= arr.length <= 500
# 1 <= arr[i] <= 500


# without Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        integer_count = {}

        for num in arr:
            integer_count[num] = integer_count.get(num, 0) + 1

        lucky_nums = [integer_count[x] for x in integer_count if x == integer_count[x]]

        if lucky_nums:
            return max(lucky_nums)
        else:
            return -1


# with Counter
from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        integer_counts = Counter(arr)
        largest_lucky_num = -1

        for num, count in integer_counts.items():
            if num == count:
                largest_lucky_num = max(largest_lucky_num, num)

        return largest_lucky_num

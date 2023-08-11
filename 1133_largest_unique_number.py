# Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.

# Example 1:

# Input: nums = [5,7,3,9,4,9,8,3,1]
# Output: 8
# Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.

# Example 2:

# Input: nums = [9,9,8,8]
# Output: -1
# Explanation: There is no number that occurs only once.

# Constraints:

# 1 <= nums.length <= 2000
# 0 <= nums[i] <= 1000

# my solution
from collections import defaultdict


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums_count = defaultdict(int)

        for num in nums:
            nums_count[num] += 1

        unique_nums = [x for x in nums_count if nums_count[x] == 1]

        if unique_nums:
            return max(unique_nums)
        else:
            return -1


# editorial solution; instead of creating a list of unique numbers, iterate over the dictionary, and for each unique number, see if it's larger than the current "result"
# this ends up being slightly slower and using slightly more memory than my solution
from collections import defaultdict


class Solution:
    def largestUniqueNumber2(self, nums: List[int]) -> int:
        nums_count = defaultdict(int)

        for num in nums:
            nums_count[num] += 1

        result = -1

        for key, value in nums_count.items():
            if value == 1:
                result = max(result, key)

        return result

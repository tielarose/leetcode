# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

# Return the sum of all the unique elements of nums.


# Example 1:

# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: 0
# Explanation: There are no unique elements, and the sum is 0.
# Example 3:

# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.


# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


# without using Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        elements_count = {}

        for num in nums:
            elements_count[num] = elements_count.get(num, 0) + 1

        return sum([x for x in elements_count if elements_count[x] == 1])


# using Counter
from collections import Counter


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum([x for x in Counter(nums) if Counter(nums)[x] == 1])

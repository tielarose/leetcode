# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.


# Example 1:

# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# Example 2:

# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15


# Constraints:

# 1 <= nums.length <= 3 * 104
# nums[i] is either 0 or 1.
# 0 <= goal <= nums.length

from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = [0]

        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        seen = defaultdict(int)

        num_of_subarrays = 0
        for sum in prefix_sum:
            num_of_subarrays += seen[sum]
            seen[sum + goal] += 1

        return num_of_subarrays

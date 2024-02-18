# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.


# Example 1:

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # key: count_diff, val: first index that count was seen
        counts_seen = {0: -1}
        max_len = count_diff = 0

        for i, num in enumerate(nums):
            count_diff += 1 if num == 1 else -1
            # if count was seen before, we have an equal num of 0s and 1s between those two indices
            if count_diff in counts_seen:
                max_len = max(max_len, i - counts_seen[count_diff])
            # if we haven't seen count before, add it to the counts_seen dict with the index
            else:
                counts_seen[count_diff] = i

        return max_len

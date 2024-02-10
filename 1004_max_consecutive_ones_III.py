# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.


# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = num_0s = 0

        for right in range(len(nums)):
            # every iteration moves the right pointer right
            # keep track of number of 0s in num_0s
            if nums[right] == 0:
                num_0s += 1

            # only when we exceed k 0s do we move the left pointer
            # at this point, the window should never get smaller
            # (we want the largest window)
            # so each time we move right up, we move left exactly once, too
            # until we get below k 0s, at which point we can possibly expand
            # the window again
            if num_0s > k:
                if nums[left] == 0:
                    num_0s -= 1
                left += 1

        # return the current window size, which will always be the largest
        # it can be
        return right - left + 1

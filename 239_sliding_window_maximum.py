# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.


# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()

        for i, num in enumerate(nums):
            # if the new num violates the decreasing order of q,
            # remove elements until decreasing order is restored
            while q and nums[q[-1]] < num:
                q.pop()

            # add index of curr element to the queue
            q.append(i)

            # check that the max element isn't out of bounds
            if q[0] == i - k:
                q.popleft()

            # add the max to ans (if the window is bigger than k)
            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans

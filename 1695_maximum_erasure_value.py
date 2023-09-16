# You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

# Return the maximum score you can get by erasing exactly one subarray.

# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).


# Example 1:

# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].
# Example 2:

# Input: nums = [5,2,1,2,5,2,1,2,5]
# Output: 8
# Explanation: The optimal subarray here is [5,2,1] or [1,2,5].


# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104

# solution using a dictionary to record the last seen index of a given element
from collections import defaultdict


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # create a dictionary to record the most recently seen index of any given number
        ind_of_nums = defaultdict(int)

        # initialize a current subarray total, a max score, left and right pointers
        subarray_total = max_score = left = right = 0

        # loop over each element in the nums array
        while right < len(nums):
            curr_ele = nums[right]
            subarray_total += curr_ele

            if curr_ele in ind_of_nums:
                while ind_of_nums[curr_ele] >= left and right > 0:
                    subarray_total -= nums[left]
                    left += 1

            ind_of_nums[curr_ele] = right
            max_score = max(max_score, subarray_total)

            right += 1

        return max_score


# solution using a set instead
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen_nums = set()

        subarray_total = max_score = left = right = 0

        while right < len(nums):
            curr_ele = nums[right]

            while curr_ele in seen_nums:
                subarray_total -= nums[left]
                seen_nums.remove(nums[left])
                left += 1

            subarray_total += curr_ele
            seen_nums.add(curr_ele)

            max_score = max(max_score, subarray_total)

            right += 1

        return max_score

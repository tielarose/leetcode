# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4


# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary_search(arr, lo, hi, targ):
            print(f"lo is {lo}, hi is {hi}, target is {target}")
            if hi >= lo:
                mid = (hi + lo) // 2

                if nums[mid] == targ:
                    return mid

                elif nums[mid] > targ:
                    return binary_search(arr, lo, mid - 1, targ)

                else:
                    return binary_search(arr, mid + 1, hi, targ)

            return lo

        return binary_search(nums, 0, len(nums) - 1, target)

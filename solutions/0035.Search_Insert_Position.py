"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid_index = (left + right) // 2
            mid_num = nums[mid_index]
            if mid_num >= target:
                return mid_index
            elif mid_num > target:
                right = mid_index - 1
            else:
                left = mid_index + 1
        return right + 1

    def searchInsertNotGood(self, nums: List[int], target: int) -> int:
        for idx, num in enumerate(nums):
            if num >= target:
                return idx
        return idx + 1

"""
https://leetcode.com/problems/two-sum/

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""


def two_sum(nums, target):
    cache = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in cache:
            return [cache[complement], idx]
        cache[num] = idx

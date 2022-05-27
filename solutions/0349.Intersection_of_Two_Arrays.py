"""
https://leetcode.com/problems/intersection-of-two-arrays/

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""


class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums2).intersection(set(nums1)))

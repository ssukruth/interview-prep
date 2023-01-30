"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sums = {0:1} # empty prefix
        curr_sum = 0
        res = 0

        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            if diff in prefix_sums:
                res += prefix_sums[diff]
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1

        return res

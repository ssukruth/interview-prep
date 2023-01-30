"""
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
"""

def length_of_longest_substring(arr, k):
    start, end = 0, 0
    max_len = 0
    counter = {}

    while end < len(arr):
        if arr[end] not in counter:
            counter[arr[end]] = 0
        counter[arr[end]] += 1
        while (end - start + 1 - counter.get(1, 0)) >  k:
            counter[arr[start]] -= 1
            start += 1
        max_len = max(max_len, end - start + 1)
        end += 1
    return max_len

"""
- start with empty window
- until window size is greater than k + num of 0s in window:
    - shrink the window
- check and set max len
- slide the window
"""

"""
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""

def max_sub_array_of_size_k(k, arr):
  start, end = 0, 0
  window_sum = 0
  max_sum = 0

  while end < len(arr):
    window_sum += arr[end]
    if end >= k - 1: # once the end moves past k -1, start sliding the window by one item in each iteration
      max_sum = max(max_sum, window_sum)
      window_sum -= arr[start]
      start += 1
    end += 1
  return max_sum

"""
- start with empty window
- once window size == k:
        - check & set max sum
        - slide the window
"""

"""
Given an array of positive integers and a number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [5, 2].

Example 2:

Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [8].

Example 3:

Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to ‘8’ are [3, 4, 1] or [1, 1, 6].
"""

def smallest_subarray_sum(s, arr):
  start, end, curr_sum = 0, 0, 0
  min_size = float("inf")

  while end < len(arr):
    curr_sum += arr[end]
    while curr_sum >= s: # Keep sliding as long as window sum is greater than s. i.e. use while and not if over here
      min_size = min(min_size, end - start + 1)
      curr_sum -= arr[start]
      start += 1
    end += 1
  if min_size == float("inf"):
    return 0
  return min_size

"""
- start with empty window
- until the window sum > target sum:
        - check and set win window size
- slide the window
"""

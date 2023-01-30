"""
Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.

Example 1:

Input: [2, 5, 3, 10], target=30
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.
Example 2:

Input: [8, 2, 6, 5], target=50
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]
Explanation: There are seven contiguous subarrays whose product is less than the target.

"""
from collections import deque

def find_subarrays(arr, target):
  product = 1
  left = 0
  result = []
  for right in range(len(arr)):
    product *= arr[right]
    while product >= target and left <= right:
      product /= arr[left]
      left += 1
    tmp_list = deque()
    for i in range(right, left - 1, -1):
      tmp_list.appendleft(arr[i])
      result.append(list(tmp_list))

  return result


"""
- use two pointers: left & right
- while right < N:
    - multiply product with arr[right]
    - while product is less than target & left <= right: divide product by arr[left] & increment left
    - append arr[left..right] to the result
"""

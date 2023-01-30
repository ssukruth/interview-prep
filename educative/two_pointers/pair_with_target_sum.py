"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
"""
def pair_with_targetsum(arr, target_sum):
  begin = 0
  end = len(arr) - 1

  while begin < end:
    if arr[begin] + arr[end] == target_sum:
      return [begin, end]
    elif arr[begin] + arr[end] < target_sum:
      begin += 1
    else:
      end -= 1
  return [-1, -1]

"""
- two pointers: begin at 0, end at N
- while begin < end (not <= since we need the target sum from two unique elements)
    - if arr[begin] + arr[end] is sum, return begin & end
    - if it's less than sum, then increment begin as we need the lowest of the numbers to get bigger
    - if it's more than sum, then decrement begin as we need the highest of the numbers to get smaller
"""

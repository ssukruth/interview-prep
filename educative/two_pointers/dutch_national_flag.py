"""
Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

Example 1:

Input: [1, 0, 2, 1, 0]
Output: [0, 0, 1, 1, 2]
Example 2:

Input: [2, 2, 0, 1, 2, 0]
Output: [0, 0, 1, 2, 2, 2,]
"""

def dutch_flag_sort(arr):
  low, high = 0, len(arr) -1
  i = 0
  while i <= high:
    if arr[i] == 0:
      arr[low], arr[i] = arr[i], arr[low]
      i += 1
      low += 1
    elif arr[i] == 1:
      i += 1
    else:
      arr[high], arr[i] = arr[i], arr[high]
      high -= 1
  return arr


"""
- Maintain two pointers low & high
- Use i as iterator
- while i <= high:
    - if arr[i] is 0, it needs to go to left: swap with arr[low]. increment low & i as this means we'd have already processed ith element
    - if arr[i] is 1, nothing to do, go to next element by incrementing i
    - if arr[i] is 2, it needs to go to right: swap with arr[high]. decrement high. do not increment i as the new element in ith pos needs to be processed.
"""

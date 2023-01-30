"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
"""

def search_pair(arr, target_sum, left, triplets):
  right = len(arr) - 1
  while left <= right:
    if arr[left] + arr[right] == target_sum:
      triplets.append([-1*target_sum, arr[left], arr[right]])
      left += 1
      right -= 1
    elif arr[left] + arr[right] < target_sum:
      left += 1
    else:
      right -= 1

def search_triplets(arr):
  arr.sort()
  triplets = []
  for i,_ in enumerate(arr):
    if i > 0 and arr[i] == arr[i-1]:
      continue
    search_pair(arr, -1*arr[i], i+1, triplets)

  return triplets

"""
- Triplets sum uses 2sum with two pointers.
- First sort the array, this makes it easier to ignore dups and also helps with two sum.
- for each element in the arr:
    - if it's same as prev element, skip processing it to avoid dups
    - else: run two_sum to find a pair of elements whos sum is the complement of the current element

- within two sum, when the sum is found, shrink the window so that we can check if there are other combinations
"""

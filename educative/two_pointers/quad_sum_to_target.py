"""
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

Example 1:

Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.
Example 2:

Input: [2, 0, -1, 1, -2, 2], target=2
Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
Explanation: Both the quadruplets add up to the target.

"""

def search_pair(arr, target, first, second, quadruplets):
  left = second + 1
  right = len(arr) - 1

  while left < right:
    if arr[left] + arr[right] == target:
      quadruplets.append([arr[first], arr[second], arr[left], arr[right]])
      return
    elif arr[left] + arr[right] < target:
      left += 1
    else:
      right -= 1

def search_triplets(arr, target, first, quadruplets):
  for i in range(first+1, len(arr)):
    if i > 0 and arr[i] == arr[i-1]:
      continue
    search_pair(arr, target - arr[i], first, i, quadruplets)

def search_quadruplets(arr, target):
  quadruplets = []
  arr.sort()
  for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i -1]:
      continue
    search_triplets(arr, target - arr[i], i, quadruplets)
  return quadruplets

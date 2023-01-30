"""
Given an array of numbers sorted in ascending order, find the element in the array that has the minimum difference with the given ‘key’.

Example 1:

Input: [4, 6, 10], key = 7
Output: 6
Explanation: The difference between the key '7' and '6' is minimum than any other number in the array
Example 2:

Input: [4, 6, 10], key = 4
Output: 4
Example 3:

Input: [1, 3, 8, 10, 15], key = 12
Output: 10
Example 4:

Input: [4, 6, 10], key = 17
Output: 10
"""


def search_min_diff_element(arr, key):
  if key < arr[0]:
    return arr[0]
  if key > arr[-1]:
    return arr[-1]

  start = 0
  end = len(arr) - 1

  while start <= end:
    mid = (start+end) //2
    if arr[mid] == key:
      return arr[mid]
    elif arr[mid] < key:
      start = mid + 1
    else:
      end = mid - 1

  if abs(arr[start] - key) < abs(arr[end] - key):
    return arr[start]
  return arr[end]

def main():
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))


main()


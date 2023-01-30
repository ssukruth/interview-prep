"""
Regular subsets code is like BFS:


def find_subsets(nums):
  subsets = []
  subsets.append([]) # append to queue
  for num in nums:
    n = len(subsets) # get number of elements in the level
    for i in range(n):  # for each element in prev level do something
      new_item = subsets[i][:]
      new_item.append(num)
      subsets.append(new_item)
  return subsets
"""

"""
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:

Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]
Example 2:

Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]

"""
def find_subsets(nums):
  # sort the numbers to handle duplicates
  list.sort(nums)
  subsets = []
  subsets.append([])
  startIndex, endIndex = 0, 0
  for i in range(len(nums)):
    startIndex = 0
    # if current and the previous elements are same, create new subsets only from the subsets
    # added in the previous step
    if i > 0 and nums[i] == nums[i - 1]:
      startIndex = endIndex
    endIndex = len(subsets)
    for j in range(startIndex, endIndex):
      # create a new subset from the existing subset and add the current element to it
      set1 = list(subsets[j])
      set1.append(nums[i])
      subsets.append(set1)
  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()

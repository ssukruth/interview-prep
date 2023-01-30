"""
Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].
Example 2:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].
Example 3:

Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
"""
def insert(intervals, new_interval):
  merged = []

  i = 0
  while i < len(intervals) and intervals[i][1] < new_interval[0]:
    merged.append(intervals[i])
    i += 1

  start, end = new_interval
  while i < len(intervals) and end > intervals[i][0]:
    start = min(start, intervals[i][0])
    end = max(end, intervals[i][1])
    i += 1

  merged.append([start, end])
  while i < len(intervals):
    merged.append(intervals[i])
    i += 1

  return merged


def main():
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()

"""
- while start of new interval is > end of interval in interval list: do nothing
- while end of new interval is < start of interval in interval list: merge
- add remaining intervals to the list
"""

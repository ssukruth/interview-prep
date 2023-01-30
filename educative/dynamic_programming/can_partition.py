"""
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}
Example 2:

Input: {1, 1, 3, 4, 7}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}
Example 3:

Input: {2, 3, 4, 6}
Output: False
Explanation: The given set cannot be partitioned into two subsets with equal sum.


This is same as 0/1 knapsack. Treat subset sum as capcaity and numbers as items and their values as weights
Use boolean values in 2D Table
Base case: T[b][1] = True if num[0] == b
"""

def can_partition(num):
  S = sum(num)
  if S % 2 != 0:
    return False

  S = S // 2
  N = len(num)
  T = [[True]*(N+1) for _ in range(S+1)]

  for s in range(S+1):
    T[s][1] = num[0] == s

  for s in range(1, S+1):
    for i in range(1, N+1):
      if T[s][i-1]: # Can make sum without curr number
        T[s][i] = True
      else: # Check if you can make the sum with current number
        if s > num[i-1]:
          T[s][i] = T[s - num[i-1]][i-1]

  for s in range(S+1):
    print(T[s])
  return T[S][N]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()

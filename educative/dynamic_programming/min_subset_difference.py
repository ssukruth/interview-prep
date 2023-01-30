"""
Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.

Example 1:#
Input: {1, 2, 3, 9}
Output: 3
Explanation: We can partition the given set into two subsets where minimum absolute difference
between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.
Example 2:#
Input: {1, 2, 7, 1, 5}
Output: 0
Explanation: We can partition the given set into two subsets where minimum absolute difference
between the sum of number is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.
Example 3:#
Input: {1, 3, 100, 4}
Output: 92
Explanation: We can partition the given set into two subsets where minimum absolute difference
between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.
"""

def can_partition(num):
  S = sum(num)
  S = S//2
  N = len(num)

  T = [[False]*(N+1) for _ in range(S+1)]

  for s in range(1, S+1):
    T[s][1] = num[0] == s

  for s in range(1, S+1):
    for i in range(1, N+1):
      if T[s][i-1]:
        T[s][i] = True
      else:
        if s > num[i-1]:
          T[s][i] = T[s - num[i-1]][i-1]

  if T[S][N]:
    return 0


  subset1 = 0
  for s in range(S, -1, -1):
    if T[s][N]:
      subset1 = s
      break

  subset2 = sum(num) - subset1
  return abs(subset2 - subset1)


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 9])))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
  print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()

"""
Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number "S".
Example 1:
Input: {1, 1, 2, 3}, S=4
Output: 3
The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
Note that we have two similar sets {1, 3}, because we have two '1' in our input.
Example 2:
Input: {1, 2, 7, 1, 5}, S=9
Output: 3
The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}
"""
def count_subsets(num, sum):
  S = sum
  N = len(num)
  T = [[0] * (N+1) for _ in range(S+1)]

  # If there's at least one item then 0 sum can be achieved by empty sum
  for i in range(1, N+1):
    T[0][i] = 1

  # If there's only one item check if sum > 0 and num[0] == sum
  for s in range(1, S+1):
    T[s][1] = 1 if num[0] == s else 0

  for s in range(1, S+1):
    for i in range(1, N+1):
      T[s][i] += T[s][i-1] # add count without num
      if s >= num[i-1]:
        T[s][i] += T[s - num[i-1]][i-1] # add count with num

  return T[S][N]


def main():
  print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
  print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()



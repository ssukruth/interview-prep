"""
The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order. For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}
"""


def LIS(A):
    n = len(A)
    T = [0]*n
    T[0] = 1
    for i in range(1, n):
      T[i] = 1
      for j in range(i):
        if A[i] > A[j]:
          T[i] = max(T[i], 1 + T[j])
    return T[-1]


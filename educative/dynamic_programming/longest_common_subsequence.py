"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.



Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
"""

def LCS(X, Y):
  x = len(X)
  y = len(Y)
  T = [[0]*(y+1) for _ in range(x+1)]
  for i in range(1, x+1):
    for j in range(1, y+1):
      if X[i-1] == Y[j-1]:
        T[i][j] = 1 + T[i-1][j-1]
      else:
        T[i][j] = max(T[i-1][j], T[i][j-1])
  return T[x][y]


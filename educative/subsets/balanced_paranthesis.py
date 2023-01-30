"""
Problem Statement#
For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.

Example 1:

Input: N=2
Output: (()), ()()
Example 2:

Input: N=3
Output: ((())), (()()), (())(), ()(()), ()()()
"""

# This is pretty standard DFS implementation

from collections import deque

def generate_valid_parentheses(num):
  result = []
  permutations = deque()
  permutations.append("")

  while permutations:
      p = permutations.popleft()
      l = p.count("(")
      r = p.count(")")
      if l == num and r == num:
        result.append(p)
      if l < num:
        permutations.append(p + ("("))
      if r < l:
        permutations.append(p + (")"))
  return result

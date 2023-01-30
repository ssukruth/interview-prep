"""
Given a string and a pattern, find all anagrams of the pattern in the given string.

Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string, we get N!
N!
 permutations (or anagrams) of a string having N
N
 characters. For example, here are the six anagrams of the string “abc”:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
Example 2:

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
"""

def find_string_anagrams(str1, pattern):
  from collections import Counter
  result_indexes = []
  start, end = 0, 0
  pc = Counter(pattern)
  sc = Counter()

  while end < len(str1):
    if str1[end] not in sc:
      sc[str1[end]] = 0
    sc[str1[end]] += 1

    if str1[end] not in pc:
      sc = Counter()
      start = end + 1

    while (end - start + 1) > len(pattern):
      sc[str1[start]] -= 1
      if sc[str1[start]] == 0:
        del sc[str1[start]]
      start += 1

    if sc == pc:
      result_indexes.append(start)
    end += 1
  return result_indexes

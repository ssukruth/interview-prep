"""
Given a string and a pattern, find the smallest substring in the given string which has all the character occurrences of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"
Example 2:

Input: String="aabdec", Pattern="abac"
Output: "aabdec"
Explanation: The smallest substring having all character occurrences of the pattern is "aabdec"
Example 3:

Input: String="abdbca", Pattern="abc"
Output: "bca"
Explanation: The smallest substring having all characters of the pattern is "bca".
Example 4:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.
"""
def find_substring(str1, pattern):
  from collections import Counter
  pc = Counter(pattern) # Frequency map of pattern
  start, end = 0, 0
  min_len = len(str1) + 1
  matched = 0
  substr_start = 0

  while end < len(str1):
    if str1[end] in pc: # if char in pattern, decrement count.
      pc[str1[end]] -= 1
      if pc[str1[end]] >= 0: # as long as counter for char >= 0 post decrement, we've matched one char
        matched += 1

    # Shrink the window if matched chars amount to len(pattern)
    while matched == len(pattern):
      # Check and set min len
      if end - start + 1 < min_len:
        min_len = end - start + 1
        substr_start = start

      # shrink the window by moving the start index
      if str1[start] in pc:
        # if the char is fully matched i.e counter is 0, then decrement the matched count
        if pc[str1[start]] == 0:
          matched -= 1
        pc[str1[start]] += 1
      start += 1
    end += 1

  if min_len > len(str1):
    return ""
  return str1[substr_start: substr_start+ min_len]

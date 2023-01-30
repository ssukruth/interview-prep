"""
Given a string, find the length of the longest substring, which has all distinct characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring with distinct characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring with distinct characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings with distinct characters are "abc" & "cde".
"""

def non_repeat_substring(str1):
    chars_counters = {}
    start, end = 0, 0
    max_len = 0

    while end < len(str1):
        if str1[end] not in chars_counters:
            chars_counters[str1[end]] = 0
        chars_counters[str1[end]] += 1
        while chars_counters[str1[end]] > 1:
            chars_counters[str1[start]] -= 1
            if chars_counters[str1[start]] == 0:
                del chars_counters[str1[start]]
            start += 1
        max_len = max(max_len, end - start + 1)
        end += 1
    return max_len

"""
- start with empty window
- until the window has more than one occurrence of end char:
    - shrink the window
- check and set max len
- slide the window
"""

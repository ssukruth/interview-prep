"""
Problem Statement#
Given a string with lowercase letters only, if you are allowed to replace no more than k letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have the longest repeating substring "bbbbb".
Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have the longest repeating substring "bbbb".
Example 3:

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
"""

def length_of_longest_substring(str1, k):
    start, end = 0, 0
    max_str, max_repeating, max_len = 0, 0, 0
    counter = {}

    while end < len(str1):
        if str1[end] not in counter:
            counter[str1[end]] = 0
        counter[str1[end]] += 1
        # Keep track of the max num times a character repeats
        # Check if the len curr substring minus the max repeating char is > k, if so shrink the window
        max_repeating = max(max_repeating, counter[str1[end]])
        if (end - start + 1 - max_repeating) > k:
            counter[str1[start]] -= 1
            start += 1
        max_len = max(max_len, end - start + 1)
        end += 1
    return max_len

print(length_of_longest_substring("aabccbb", 2))


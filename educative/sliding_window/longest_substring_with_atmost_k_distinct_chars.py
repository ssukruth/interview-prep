"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
Example 4:

Input: String="cbbebi", K=10
Output: 6
Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".
"""

def longest_substring_with_k_distinct(str1, k):
    bucket = {}
    start, end = 0, 0
    max_str = 0

    while end < len(str1):
        if str1[end] not in bucket:
            bucket[str1[end]] = 0
        bucket[str1[end]] += 1
        while len(bucket) > k:
            bucket[str1[start]] -= 1
            if bucket[str1[start]] == 0:
                bucket.pop(str1[start])
            start += 1
        max_str = max(max_str, end - start + 1)
        end += 1
    return max_str

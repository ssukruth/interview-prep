"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".


Constraints:

1 <= s.length <= 20
1 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        result = {}

        def dfs(i, j):
            if (i, j) in result:
                return result[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            # check if curr char index of p is the same as "." or curr char index of s
            matched = i < len(s) and p[j] in [s[i], "."]

            # handle * first
            # if next char is *
            # res(i, j) = dfs(i, j+2) i.e nothing matches OR dfs(i+1, j) i.e. something matches
            if j < len(p) - 1 and p[j+1] == "*":
                result[(i, j)] = dfs(i, j+2) or (matched and dfs(i+1, j))
                return result[(i, j)]

            # else if there is a match
            # res(i, j) = dfs(i+1, j+1)
            if matched:
                result[(i, j)] = dfs(i+1, j+1)
                return result[(i, j)]

            result[(i, j)] = False
            return result[(i, j)]

        return dfs(0, 0)

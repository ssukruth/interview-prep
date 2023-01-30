"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            elif char == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
            elif char == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0

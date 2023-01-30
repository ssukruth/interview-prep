class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def expand_and_check(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        longest = ''
        longer = ''
        maxlen = float("-inf")
        for i in range(len(s)):
            odd = expand_and_check(s, i, i)
            even = expand_and_check(s, i, i+1)

            if len(odd) < len(even):
                longer = even
            else:
                longer = odd
            if len(longer) > maxlen:
                longest = longer
                maxlen = len(longer)

        return longest

"""
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.



Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.

"""

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        # N = number of words
        # L = max len of each word

        # Adding words into map O(NL)
        word_map = {word: i for i, word in enumerate(words)}

        # Creating graph O(N)
        graph = {i: [] for i in range(len(words))}

        # Creating memoization table  O(N)
        distances = [0] *len(words)

        # For each string we check if we can create another string by splitting the string into two halves and omitting a char
        # O(NL^2) => O(N) for the loop. O(L) for inner loop and O(L) for slicing & concating the string.
        for v, word in enumerate(words):
            for i in range(len(word)):
                s = word[0:i] + word[i+1:]
                if s in word_map:
                    u = word_map[s]
                    graph[u].append(v)


        # Graph can have atmost NL edges since the graph is created by the two nested for loops above.
        # Finding the max length chain in a graph is O(E) i.e O(NL)
        def longest_edge_chain(u):
            if distances[u] > 0:
                return distances[u]
            for v in graph[u]:
                distances[u] = max(distances[u], longest_edge_chain(v) + 1)
            return distances[u]

        res = 0
        for i in range(len(words)):
            res = max(res, longest_edge_chain(i))

        return res + 1

        # Total time complexity O(N*L^2) + O(NL) ~ O(N*L^2)

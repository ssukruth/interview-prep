"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.


Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        from collections import defaultdict, deque
        dictionary = {word: i for i, word in enumerate(wordList)}

        if endWord not in dictionary:
            return 0

        graph = defaultdict(list)
        lc = "abcdefghijklmnopqrstuvwxyz"

        for word in wordList:
            for i in range(len(word)):
                left = word[:i]
                right = word[i+1:]
                for ch in lc:
                    if ch != word[i]:
                        new_word = left + ch + right
                        if new_word in dictionary:
                            graph[word].append(new_word)
                        elif new_word == beginWord:
                            graph[beginWord].append(word)

        if not graph[beginWord]:
            return 0


        q = deque()
        q.append(beginWord)
        count = 1
        seen = set()
        seen.add(beginWord)
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count

                for new_word in graph[word]:
                    if new_word not in seen:
                        q.append(new_word)
                        seen.add(new_word)
            count += 1

        return 0

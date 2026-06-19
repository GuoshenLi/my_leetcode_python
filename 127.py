from collections import deque
from typing import List
# 典型的广度优先搜索 基于图 插入一个要删除set中的元素 否则会死循环
# leetcode 433 一样的题目
# bfs同时出发
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet: return 0

        queue = deque()
        queue.append([beginWord, 1])
        if beginWord in wordSet:
            wordSet.remove(beginWord)

        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length

            for i in range(len(word)):
                for j in range(26):
                    new_word = word[:i] + chr(ord('a') + j) + word[i + 1:]
                    if new_word in wordSet:
                        wordSet.remove(new_word)
                        queue.append([new_word, length + 1])

        return 0

print(Solution().ladderLength(
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]))

from collections import deque
from typing import List
# 典型的广度优先搜索 基于图 插入一个要删除set中的元素 否则会死循环
# leetcode 433 一样的题目
# bfs同时出发
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        len_word = len(beginWord)
        queue = deque()
        queue.append([beginWord, [beginWord], 1])
        if beginWord in wordList:
            wordList.remove(beginWord)

        res = []

        while queue:
            word, path, step = queue.popleft()
            if word == endWord:
                res.append(path)


            for i in range(len_word):
                for j in range(26):
                    newword = word[:i] + chr(ord('a') + j) + word[i + 1:]
                    if newword in wordList:
                        wordList.remove(newword)
                        queue.append([newword, path + [newword], step + 1])

        return res


print(Solution().ladderLength(
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]))

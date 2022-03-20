from collections import defaultdict
from typing import List
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList: return []
        wordList = set(wordList)
        current = {}
        # key: 到达这个单词 value: 全部路径
        current[beginWord] = [[beginWord]]

        while current:
            nxt = defaultdict(list)

            for word in current:
                if word == endWord: return current[word]

                for i in range(len(word)):
                    for j in range(26):
                        new_word = word[:i] + chr(ord('a') + j) + word[i + 1:]

                        if new_word in wordList:
                            nxt[new_word] += [path + [new_word] for path in current[word]]

            wordList -= set(nxt.keys())
            current = nxt

        return []




# 或者直接用队列
# （按层） bfs它寻找的就是最短的路径
from collections import deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList: return []
        wordList = set(wordList)

        # key: 到达这个单词 value: 到达val的某一条路径
        queue = deque()
        queue.append([beginWord, [beginWord]])
        res = []

        while queue:
            visited = set()
            len_this_level = len(queue)
            # 队列当中保存着这一层中所有的最短路径
            for i in range(len_this_level):
                word, path = queue.popleft()
                if word == endWord: res.append(path)

                for i in range(len(word)):
                    for j in range(26):
                        new_word = word[:i] + chr(ord('a') + j) + word[i + 1:]

                        if new_word in wordList:
                            queue.append([new_word, path + [new_word]])
                            visited.add(new_word)

            wordList -= visited

        return res


print(Solution().findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
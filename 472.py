from typing import List
# 暴力回溯也能过
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        n = len(words)
        word_set = set()

        for word in words:
            if not word:
                continue
            word_set.add(word)

        def dfs(word, start, count):
            if start == len(word) and count >= 2: return True

            for end in range(start, len(word)):
                slice_ = word[start: end + 1]
                if slice_ in word_set:
                    if dfs(word, end + 1, count + 1):
                        return True

            return False


        res = []
        for word in words:
            if not word:
                continue
            if dfs(word, 0, 0):
                res.append(word)

        return res




class Trie_Node:
    def __init__(self):
        self.next = [None] * 26
        self.is_word = False


class Trie_Tree:
    def __init__(self):
        self.root = Trie_Node()

    def insert(self, word):
        n = len(word)
        node = self.root
        for i in range(n):
            alpha = word[i]
            if not node.next[ord(alpha) - ord('a')]:
                node.next[ord(alpha) - ord('a')] = Trie_Node()
            node = node.next[ord(alpha) - ord('a')]

        node.is_word = True

    def search(self, word, start, count):
        node = self.root
        n = len(word)
        if start == n and count >= 2: return True
        for i in range(start, n):
            alpha = word[i]
            if not node.next[ord(alpha) - ord('a')]:
                break
            node = node.next[ord(alpha) - ord('a')]
            if node.is_word:
                if self.search(word, i + 1, count + 1):
                    return True

        return False



class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []
        tree = Trie_Tree()
        # 最朴素的操作 先插入所有
        for word in words:
            if len(word) == 0: continue
            tree.insert(word)

        # 再一个一个判断，加入一个count参数 要大于等于两个才可以
        # 不要用那么多trick
        for word in words:
            if len(word) == 0: continue

            if tree.search(word, 0, 0):
                res.append(word)

        return res




print(Solution().findAllConcatenatedWordsInADict(words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
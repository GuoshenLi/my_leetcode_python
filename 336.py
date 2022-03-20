from typing import List
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        n = len(words)
        res = []
        for i in range(n):
            for j in range(n):
                if i != j and self.is_palindrome(''.join([words[i], words[j]])):
                    res.append([i, j])

        return res

    def is_palindrome(self, word):

        left = 0
        right = len(word) - 1

        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True



# 字典树
class Trie_Node:
    def __init__(self):
        self.next = [None for i in range(26)]
        self.index = -1


class Trie_Tree:
    def __init__(self):
        self.root = Trie_Node()

    def insert(self, word, index):
        n = len(word)
        cur_node = self.root

        for i in range(n - 1, -1, -1):
            alpha = word[i]
            if not cur_node.next[ord(alpha) - ord('a')]:
                cur_node.next[ord(alpha) - ord('a')] = Trie_Node()
            cur_node = cur_node.next[ord(alpha) - ord('a')]

        cur_node.index = index

    def search(self, word):
        n = len(word)
        cur_node = self.root

        for i in range(n):
            alpha = word[i]
            if not cur_node.next[ord(alpha) - ord('a')]:
                return -1
            cur_node = cur_node.next[ord(alpha) - ord('a')]

        return cur_node.index


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        self.tree = Trie_Tree()

        for i in range(len(words)):
            self.tree.insert(words[i], i)

        res = list()
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                if self.is_palindrome(word, j, m - 1):
                    leftId = self.tree.search(word[:j])
                    if leftId != -1 and leftId != i:
                        res.append([i, leftId])

                if j and self.is_palindrome(word, 0, j - 1):

                    # 有可能 abcd 与dcba这种情况，遍历到abcd的时候已经把[1, 0]和[0, 1]全都加入集合了
                    # 因此再遍历dcba的时候 会把两个重新加入一遍，造成重复，最简单的话就直接用哈希去重。
                    # 或者 j or j!=m 上一个判断。

                    rightId = self.tree.search(word[j:])
                    if rightId != -1 and rightId != i:
                        res.append([rightId, i])

        return res

    def is_palindrome(self, word, left, right):

        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True


print(Solution().palindromePairs(words = ["abcd","dcba","lls","s","sssll"]))
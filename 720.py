class Solution(object):
    def longestWord(self, words):
        ans = ""
        wordset = set(words)
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if all(word[:k] in wordset for k in range(1, len(word))):
                    ans = word

        return ans


# 字典树
class Trie_Node:
    def __init__(self):
        self.next = [None for i in range(26)]
        self.is_word = False
        self.word = None


class Trie_Tree:
    def __init__(self):
        self.root = Trie_Node()
        self.max_depth = 0
        self.res = ''

    def insert(self, word):
        n = len(word)
        cur_node = self.root
        for i in range(n):
            alpha = word[i]
            if not cur_node.next[ord(alpha) - ord('a')]:
                cur_node.next[ord(alpha) - ord('a')] = Trie_Node()
            cur_node = cur_node.next[ord(alpha) - ord('a')]

        cur_node.is_word = True
        cur_node.word = word

    def max_len_word(self, depth, node):
        if depth > 0 and not node.is_word:
            return None

        if depth > self.max_depth:
            self.max_depth = depth
            self.res = node.word

        for i in range(26):
            if node.next[i]:
                self.max_len_word(depth + 1, node.next[i])


class Solution:
    def longestWord(self, words: List[str]) -> str:
        tree = Trie_Tree()
        for word in words:
            tree.insert(word)
        tree.max_len_word(0, tree.root)
        return tree.res




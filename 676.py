from collections import defaultdict
# 暴力解法 记录字符串长度 以长度为key, value为对应的字符串

class MagicDictionary(object):
    def __init__(self):
        self.bucket = defaultdict(list)

    def buildDict(self, words):
        for word in words:
            self.bucket[len(word)].append(word)

    def search(self, word):
        if len(word) not in self.bucket:
            return False

        for each in self.bucket[len(word)]:
            count = 0
            for i, j in zip(each, word):
                if i != j:
                    count += 1
            if count == 1:
                return True
        return False





# 字典树递归
class Trie_Node:
    def __init__(self):
        self.next = [None for i in range(26)]
        self.is_word = False


class Trie_Tree:
    def __init__(self):
        self.root = Trie_Node()

    def insert(self, word):
        n = len(word)
        cur_node = self.root
        for i in range(n):
            alpha = word[i]
            if not cur_node.next[ord(alpha) - ord('a')]:
                cur_node.next[ord(alpha) - ord('a')] = Trie_Node()
            cur_node = cur_node.next[ord(alpha) - ord('a')]

        cur_node.is_word = True

    def search(self, word, num, index, node):
        if num < 0: return False
        if index == len(word): return (num == 0) and node.is_word

        for i in range(26):
            if node.next[i]:  # 有这个字
                if chr(i + ord('a')) == word[index]:
                    if self.search(word, num, index + 1, node.next[i]):
                        return True

                else:
                    if self.search(word, num - 1, index + 1, node.next[i]):
                        return True

        return False


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = Trie_Tree()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.tree.insert(word)

    def search(self, searchWord: str) -> bool:
        return self.tree.search(searchWord, 1, 0, self.tree.root)

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)

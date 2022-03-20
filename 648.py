from typing import List
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # 暴力解法
        # 判断词根在不在
        rootset = set(dictionary)

        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split(' ')))




# 字典树
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

    def query(self, word):
        n = len(word)
        cur_node = self.root
        for i in range(n):
            alpha = word[i]

            if cur_node.is_word == True: return word[:i]
            if not cur_node.next[ord(alpha) - ord('a')]:
                return word
            cur_node = cur_node.next[ord(alpha) - ord('a')]

        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        tree = Trie_Tree()
        for word in dictionary:
            tree.insert(word)

        sentence = sentence.split()
        res = []
        for word in sentence:
            res.append(tree.query(word))

        return ' '.join(res)


print(Solution().replaceWords(dictionary = ["cat","bat","rat"],
                        sentence = "the cattle was rattled by the battery"))


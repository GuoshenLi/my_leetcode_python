# 不用字典树 按长度来
import collections
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(set)  # 键为单词长度，值为相同长度的单词列表

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        self.dic[len(word)].add(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        n = len(word)
        if n not in self.dic:
            return False

        for compare_word in self.dic[n]:
            for i in range(n):
                if word[i] != '.' and word[i] != compare_word[i]:
                    break
            else:
                return True
        return False






# 字典树写法
class WordDictionary:
    class Node:
        def __init__(self):
            self.is_word = False
            self.next = [None for _ in range(26)]

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = WordDictionary.Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        size = len(word)
        cur_node = self.root
        for i in range(size):
            alpha = word[i]
            if cur_node.next[ord(alpha) - ord('a')] is None:
                cur_node.next[ord(alpha) - ord('a')] = WordDictionary.Node()
            cur_node = cur_node.next[ord(alpha) - ord('a')]

        if not cur_node.is_word:
            cur_node.is_word = True



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.__match(word, self.root, 0)



    def __match(self, word, node, start):
        if start == len(word):
            return node.is_word
        alpha = word[start]
        # 关键在这里，如果当前字母是 "." ，每一个分支都要走一遍
        if alpha == '.':
            # print(node.next)
            for i in range(26):
                if node.next[i] and self.__match(word, node.next[i], start + 1):
                    return True
            return False
        else:
            if not node.next[ord(alpha)-ord('a')]:
                return False
            return self.__match(word, node.next[ord(alpha) - ord('a')], start + 1)


WordDictionary().addWord('abcde')





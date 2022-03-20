# 字典树 也容易记
class Trie_node:
    def __init__(self):
        self.is_word = False
        self.next = [None for i in range(26)]


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie_node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        n = len(word)
        cur_node = self.root

        for i in range(n):
            alpha = word[i]
            if not cur_node.next[ord(alpha) - ord('a')]:
                cur_node.next[ord(alpha) - ord('a')] = Trie_node()
            cur_node = cur_node.next[ord(alpha) - ord('a')]

        if not cur_node.is_word:
            cur_node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        cur_node = self.root
        n = len(word)
        for i in range(n):
            alpha = word[i]
            if not cur_node.next[ord(alpha) - ord('a')]:
                return False
            else:
                cur_node = cur_node.next[ord(alpha) - ord('a')]

        return cur_node.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        cur_node = self.root
        n = len(prefix)
        for i in range(n):
            alpha = prefix[i]
            if not cur_node.next[ord(alpha) - ord('a')]:
                return False
            else:
                cur_node = cur_node.next[ord(alpha) - ord('a')]

        return True





# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("hello")
param_2 = obj.search("hell")
print(param_2)
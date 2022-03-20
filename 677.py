from collections import defaultdict
# 暴力法
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map_ = defaultdict(int)



    def insert(self, key: str, val: int) -> None:
        self.map_[key] = val

    def sum(self, prefix: str) -> int:
        length = len(prefix)
        return sum(v for k, v in self.map_.items() if k[:length] == prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

# 字典树
class Trie_Node:
    def __init__(self):
        self.next = [None for i in range(26)]
        self.is_word = False
        self.val = None


class Trie_Tree:
    def __init__(self):
        self.root = Trie_Node()

    def insert(self, word, val):
        n = len(word)
        cur_node = self.root
        for i in range(n):
            alpha = word[i]
            if not cur_node.next[ord(alpha) - ord('a')]:
                cur_node.next[ord(alpha) - ord('a')] = Trie_Node()
            cur_node = cur_node.next[ord(alpha) - ord('a')]

        cur_node.is_word = True
        cur_node.val = val

    def calculate_sum(self, prefix):
        n = len(prefix)
        cur_node = self.root
        for i in range(n):
            alpha = prefix[i]
            if not cur_node.next[ord(alpha) - ord('a')]:
                return 0
            cur_node = cur_node.next[ord(alpha) - ord('a')]

        return self.search(cur_node)

    def search(self, node):
        if not node: return 0
        sum_ = 0
        if node.is_word:
            sum_ += node.val

        for i in range(26):
            sum_ += self.search(node.next[i])

        return sum_


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.tree = Trie_Tree()

    def insert(self, key: str, val: int) -> None:
        self.tree.insert(key, val)

    def sum(self, prefix: str) -> int:
        return self.tree.calculate_sum(prefix)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
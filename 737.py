class UnionFind:
    def __init__(self, length):
        self.length = length
        self.parent = [-1] * self.length

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root: return False
        self.parent[x_root] = y_root

    def find(self, x):
        while self.parent[x] != -1:
            x = self.parent[x]
        return x


class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False

        uf = UnionFind(len(similarPairs) * 2)
        word2index = {}

        for idx, (word1, word2) in enumerate(similarPairs):
            if word1 not in word2index:
                word2index[word1] = idx * 2
            if word2 not in word2index:
                word2index[word2] = idx * 2 + 1
            uf.union(word2index[word1], word2index[word2])

        for word1, word2 in zip(sentence1, sentence2):
            if word1 == word2: continue
            if word1 in word2index and word2 in word2index:
                # test case 有特殊情况
                root_word1 = uf.find(word2index[word1])
                root_word2 = uf.find(word2index[word2])

                if root_word1 != root_word2:
                    return False
            else:
                return False
        return True




# dfs
from collections import defaultdict
class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False

        graph = defaultdict(list)

        for u, v in similarPairs:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(start, end, visited):
            if start == end: return True
            visited.add(start)
            for neighbor in graph[start]:
                if neighbor not in visited and dfs(neighbor, end, visited): return True
            visited.remove(start)
            return False

        for word1, word2 in zip(sentence1, sentence2):
            if word1 == word2: continue
            if word1 in graph and word2 in graph:
                if not dfs(word1, word2, set()):
                    return False
            else:
                return False
        return True
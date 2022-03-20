# 套用79题目 39/40超时
from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        res = []
        for word in words:
            if self.exist(board, word):
                res.append(word)

        return res

    def exist(self, board: List[List[str]], word: str) -> bool:

        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        m = len(board)
        n = len(board[0])
        length = len(word)
        vidited = [[False] * n for i in range(m)]

        def dfs(i, j, index):
            if index == length - 1:
                return board[i][j] == word[index]
            elif board[i][j] != word[index]:
                return False
            # 等于
            vidited[i][j] = True
            for x_, y_ in direction:
                new_x = x_ + i
                new_y = y_ + j

                if 0 <= new_x < m and 0 <= new_y < n and (vidited[new_x][new_y] == False) and dfs(new_x, new_y,
                                                                                                  index + 1):
                    return True

            vidited[i][j] = False
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False


class Trie_Node:
    def __init__(self):
        self.is_end = False
        self.next = [None for i in range(26)]
        self.word = None


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

        if not cur_node.is_end:
            cur_node.is_end = True
            cur_node.word = word

class Trie_Node:
    def __init__(self):
        self.is_end = False
        self.next = [None for i in range(26)]
        self.word = None


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

        if not cur_node.is_end:
            cur_node.is_end = True
            cur_node.word = word





#########   字典树
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 进行一次回溯即可，字典树只可以进行一次回溯

        trie_tree = Trie_Tree()
        for word in words:
            trie_tree.insert(word)

        self.m = len(board)
        self.n = len(board[0])
        self.res = []
        self.direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * self.n for i in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                self.dfs(board, visited, i, j, trie_tree.root)

        return self.res

    def dfs(self, board, visited, row, col, node):
        if visited[row][col] == True:
            return None

        char = board[row][col]

        if not node.next[ord(char) - ord('a')]:
            return None

        node = node.next[ord(char) - ord('a')]

        if node.is_end == True:
            self.res.append(node.word)
            node.is_end = False

        visited[row][col] = True
        for x, y in self.direction:
            new_row = row + x
            new_col = col + y
            if 0 <= new_row < self.m and 0 <= new_col < self.n:
                self.dfs(board, visited, new_row, new_col, node)

        visited[row][col] = False


print(Solution().findWords(board = [["o","a","a","n"],
                              ["e","t","a","e"],
                              ["i","h","k","r"],
                              ["i","f","l","v"]],

                     words = ["oath","pea","eat","rain"]))



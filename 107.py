# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# BFS 宽度优先搜索，容易想到。
from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        legth_this_level = len(queue)
        paths = []
        while queue:
            path = []
            for _ in range(legth_this_level):
                node = queue.popleft()
                path.append(node.val)
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            legth_this_level = len(queue)
            paths.append(path)

        return paths[::-1]


# DFS 宽度优先搜索，不容易想到，要写一个函数，记住（这个节点，这个节点对应的level，以及总path）
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        path = []
        self.recur_level(root, 0, path)
        return path[::-1]

    def recur_level(self, node, level, path):
        if not node:
            return None
        if len(path) == level:
            path.append([])
        path[level].append(node.val)
        self.recur_level(node.left, level + 1, path)
        self.recur_level(node.right, level + 1, path)



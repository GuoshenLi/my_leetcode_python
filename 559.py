"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# 宽度优先搜索
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0

        queue = deque()
        queue.append(root)
        depth = 0

        while queue:
            n = len(queue)
            depth += 1
            for i in range(n):
                node = queue.popleft()
                if node.children:
                    for child in node.children:
                        queue.append(child)

        return depth


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# 深度优先搜索
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        return max(self.maxDepth(child) for child in root.children) + 1



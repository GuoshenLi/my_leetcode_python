# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        curLevel = [root]
        paths = []
        while curLevel:
            tmpLevel = []
            path = []
            for node in curLevel:
                path.append(node.val)
                if node.left:
                    tmpLevel.append(node.left)
                if node.right:
                    tmpLevel.append(node.right)
            paths.append(path)
            curLevel = tmpLevel

        return paths


###### BFS ######
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        levels = []

        while queue:
            length_this_level = len(queue)
            level = []
            for _ in range(length_this_level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)
            levels.append(level)
        return levels
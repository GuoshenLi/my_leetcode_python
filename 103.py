# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        paths = []

        node_que = deque()
        node_que.append(root)
        length_level = len(node_que)
        FLAG = False
        while node_que:
            path = []
            for _ in range(length_level):
                node = node_que.popleft()
                path.append(node.val)

                if node.left:
                    node_que.append(node.left)

                if node.right:
                    node_que.append(node.right)
            length_level = len(node_que)
            if FLAG:
                path = path[::-1]
            paths.append(path)
            FLAG = not FLAG
        return paths




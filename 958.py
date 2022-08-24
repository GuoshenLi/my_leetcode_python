# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        res = []
        queue = deque()
        queue.append([root, 0])

        while queue:
            length = len(queue)
            for _ in range(length):
                node, index = queue.popleft()
                res.append(index)
                if node.left:
                    queue.append([node.left, 2 * index + 1])
                if node.right:
                    queue.append([node.right, 2 * index + 2])

        return res[-1] == len(res) - 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:

        queue = deque()
        queue.append(root)
        res = 0
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                if i == 0:
                    res = node.val

        return res

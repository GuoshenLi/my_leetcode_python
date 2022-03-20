# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = deque()
        queue.append(root)
        depth = 0
        while queue:
            n = len(queue)
            depth += 1
            for i in range(n):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return depth


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0
        depth = 1
        current_level = [root]

        while True:
            tmp_level = []
            for node in current_level:
                if node.left:
                    tmp_level.append(node.left)
                if node.right:
                    tmp_level.append(node.right)
            if len(tmp_level) == 0:
                break
            else:
                depth += 1
                current_level = tmp_level

        return depth



class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0
        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1

        return max(left, right)

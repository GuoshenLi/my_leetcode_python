# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 变样的 2 sum
from collections import deque
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:

        if not root: return False
        s = set()

        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()

            value = node.val

            if k - value in s: return True
            s.add(value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False




# 2021.11.2 现在都习惯写递归了哈哈啊哈哈
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:

        table = set()

        def dfs(node):
            if not node: return False
            if k - node.val in table: return True
            table.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
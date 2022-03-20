# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root


        queue = deque()
        queue.append(root)
        depth -= 1
        while depth > 1:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            depth -= 1

        n = len(queue)
        for i in range(n):
            node = queue.popleft()
            left = node.left
            right = node.right

            node.left = TreeNode(val)
            node.right = TreeNode(val)

            node.left.left = left
            node.right.right = right


        return root


# 2021.11.2 递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:

        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root


        def dfs(node, cur_depth):
            if not node: return None
            if cur_depth == depth - 1:

                left = node.left
                right = node.right
                node.left = TreeNode(val)
                node.right = TreeNode(val)
                node.left.left = left
                node.right.right = right

            else:
                dfs(node.left, cur_depth + 1)
                dfs(node.right, cur_depth + 1)

        dfs(root, 1)

        return root




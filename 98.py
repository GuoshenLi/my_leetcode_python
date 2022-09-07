# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        node_que = deque()
        max_que = deque()
        min_que = deque()

        node_que.append(root)
        max_que.append(float('+inf'))
        min_que.append(float('-inf'))

        while node_que:
            node = node_que.popleft()
            max_ = max_que.popleft()
            min_ = min_que.popleft()

            if node.val >= max_ or node.val <= min_:
                return False

            if node.left:
                node_que.append(node.left)
                max_que.append(node.val)
                min_que.append(min_)

            if node.right:
                node_que.append(node.right)
                max_que.append(max_)
                min_que.append(node.val)

        return True


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.recur_BST(root, float(-inf), float(+inf))

    def recur_BST(self, node, min, max):
        if not node:
            return True
        if node.val >= max or node.val <= min:
            return False

        return self.recur_BST(node.left, min, node.val) and self.recur_BST(node.right, node.val, max)
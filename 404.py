# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        sum = 0
        isLeafNode = lambda node: True if not node.left and not node.right else False

        node_que = deque()
        node_que.append(root)
        while node_que:
            node = node_que.popleft()

            if node.left:
                if isLeafNode(node.left):
                    sum += node.left.val

                else:
                    node_que.append(node.left)

            if node.right:
                node_que.append(node.right)

        return sum


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        sum = 0
        isLeafNode = lambda node: True if not node.left and not node.right else False
        if root.left:
            if isLeafNode(root.left):
                sum = root.left.val

        return sum + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)




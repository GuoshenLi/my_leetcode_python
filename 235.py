# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node_que = deque()
        node_que.append(root)

        while node_que:
            node = node_que.popleft()
            if (p.val - node.val) * (q.val - node.val) <= 0:
                return node

            elif (p.val - node.val) > 0:
                node_que.append(node.right)

            elif (p.val - node.val) < 0:
                node_que.append(node.left)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)



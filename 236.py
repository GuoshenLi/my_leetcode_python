# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

# bfs，储存从跟节点到p和q的路径，两条路径最后一个不相等的节点即为所求。
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node_que = deque()
        path_que = deque()
        p_path = []
        q_path = []

        node_que.append(root)
        path_que.append([root])
        while node_que:
            node = node_que.popleft()
            node_path = path_que.popleft()

            if node == p:
                p_path = node_path
            if node == q:
                q_path = node_path

            if p_path and q_path:
                break

            if node.left:
                node_que.append(node.left)
                path_que.append(node_path + [node.left])

            if node.right:
                node_que.append(node.right)
                path_que.append(node_path + [node.right])
        print(len(q_path))
        print(len(p_path))

        same = -1

        for i in range(min(len(q_path), len(p_path))):

            if q_path[i] == p_path[i]:
                same += 1
        return q_path[same]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 要烂熟于心！代码特别：先返回p或q，再返回公公祖先。
# 若两个节点公共祖先为其中一个节点，则其走到其中一个节点就可以了。
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left and not right:
            return None
        if left and right:
            return root
        return left or right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        node_que = deque()
        path_que = deque()

        node_que.append(root)
        path_que.append(str(root.val))
        final_path = []
        while node_que:
            node = node_que.popleft()
            path_node = path_que.popleft()

            if not node.left and not node.right:
                final_path.append(path_node)

            if node.left:
                node_que.append(node.left)
                path_que.append(path_node + '->' + str(node.left.val))
            if node.right:
                node_que.append(node.right)
                path_que.append(path_node + '->' + str(node.right.val))


        return final_path


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        self.final_path = []
        self.recur_path(root, '')
        return self.final_path

    def recur_path(self, node, path):
        if not node:
            return None
        if not node.left and not node.right:
            return self.final_path.append(path + str(node.val))

        self.recur_path(node.left, path + str(node.val) + '->')
        self.recur_path(node.right, path + str(node.val) + '->')

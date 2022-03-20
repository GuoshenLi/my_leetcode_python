######   BFS ######
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        if not root:
            return []

        node_que = deque()
        path_que = deque()
        sum_que = deque()

        node_que.append(root)
        path_que.append([root.val])
        sum_que.append(root.val)
        paths = []
        while node_que:
            node = node_que.popleft()
            path = path_que.popleft()
            sum_path = sum_que.popleft()

            if not node.left and not node.right:
                if sum_path == sum_:
                    paths.append(path)

            if node.left:
                node_que.append(node.left)
                path_que.append(path + [node.left.val])
                sum_que.append(sum_path + node.left.val)

            if node.right:
                node_que.append(node.right)
                path_que.append(path + [node.right.val])
                sum_que.append(sum_path + node.right.val)

        return paths

# dfs #
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        if not root:
            return []

        self.final_path = []
        self.recur_sum(root, sum_, [])
        return self.final_path

    def recur_sum(self, node, sum_, path):
        if not node:
            return None

        if not node.left and not node.right:
            if node.val == sum_:
                self.final_path.append(path + [node.val])

        self.recur_sum(node.left, sum_ - node.val, path + [node.val])
        self.recur_sum(node.right, sum_ - node.val, path + [node.val])
















# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# double recursion
from collections import deque


class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        return self.pathSumFrom(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def pathSumFrom(self, node, sum):
        if not node:
            return 0

        path_num = 0
        if node.val == sum:
            path_num = 1

        return self.pathSumFrom(node.left, sum - node.val) + self.pathSumFrom(node.right, sum - node.val) + path_num

# BFS 思想巧妙，每一个节点存放这个节点反过来到跟节点所对应路径的节点值之和
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        node_que = deque()
        path_sum_que = deque()

        node_que.append(root)
        path_sum_que.append([root.val])
        num_all = 0
        while node_que:
            node = node_que.popleft()
            path_sum = path_sum_que.popleft()
            num_all += path_sum.count(sum)
            path_sum += [0]

            if node.left:
                node_que.append(node.left)
                path_sum_que.append([i + node.left.val for i in path_sum])

            if node.right:
                node_que.append(node.right)
                path_sum_que.append([i + node.right.val for i in path_sum])

        return num_all






# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

# 典型的层序遍历
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = deque()
        res = []
        queue.append(root)

        while queue:
            tmp = []
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                tmp.append(node.val)

            res.append(sum(tmp) / length)

        return res







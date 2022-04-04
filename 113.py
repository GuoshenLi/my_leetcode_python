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

# dfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if not root: return []
        res = []

        def dfs(node, targetSum, tmp):
            if not node: return None
            if not node.left and not node.right:
                if node.val == targetSum:
                    res.append(tmp + [node.val])
                return None

            dfs(node.left, targetSum - node.val, tmp + [node.val])
            dfs(node.right, targetSum - node.val, tmp + [node.val])


        dfs(root, targetSum, [])
        return res
















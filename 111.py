
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = deque()
        queue.append(root)

        depth = 0

        while queue:
            n = len(queue)
            depth += 1
            for i in range(n):
                node = queue.popleft()
                if not node.left and not node.right:
                    return depth

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)




# 递归 # 注意特殊情况
# 若对于一个特定的节点，若此节点左右子树都有，则取min
# 若此节点左右子树至少有一个为空，则取max
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1









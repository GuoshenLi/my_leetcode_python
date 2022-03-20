# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 记忆化递归
class Solution:
    def rob(self, root: TreeNode) -> int:
        memo = {}
        def dfs(root):
            if not root: return 0
            if root in memo: return memo[root]
            # 对于这个跟节点来说
            # 只有两种情况就是抢和不抢

            rob_include_root = root.val
            if root.left:
                rob_include_root += dfs(root.left.left) + dfs(root.left.right)

            if root.right:
                rob_include_root += dfs(root.right.left) + dfs(root.right.right)

            rob_not_include_root = dfs(root.left) + dfs(root.right)
            memo[root] = max(rob_include_root, rob_not_include_root)
            return memo[root]


        return dfs(root)


# 树状dp后序遍历 和 最近公公祖先 二叉树转换成链表一样 都是后序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def rob(self, root: TreeNode) -> int:


        def dfs(root):
            if not root: return None

            dfs(root.left)
            dfs(root.right)

            rob[root] = root.val + not_rob[root.left] + not_rob[root.right]
            not_rob[root] = max(rob[root.left], not_rob[root.left]) + max(rob[root.right], not_rob[root.right])


        rob = defaultdict(int)
        not_rob = defaultdict(int)
        dfs(root)

        return max(rob[root], not_rob[root])
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = float('-inf')
        def dfs(node):

            if not node: return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            self.res = max(self.res, left + right + node.val)
            return max(left, right) + node.val

        dfs(root)

        return self.res




# 暴力双递归 记住lru_cache()
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def maxPathSum(self, root: TreeNode) -> int:
        if not root: return float('-inf')


        return max(root.val + max(self.dfs(root.left), 0) + max(self.dfs(root.right), 0), self.maxPathSum(root.left), self.maxPathSum(root.right))

    @lru_cache()
    def dfs(self, node):
        if not node: return float('-inf')
        # 这个max 做截断很巧妙
        # 如果一边是负数就直接变成0 模拟不加
        left = max(self.dfs(node.left), 0)
        right = max(self.dfs(node.right), 0)

        return node.val + max(left, right)


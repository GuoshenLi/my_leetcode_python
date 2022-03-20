# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# 以root为根节点 最长能够延伸出来一条多长的路径
# 然后递归调用
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node: return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.res = max(self.res, left + right)

        return max(left, right) + 1



# 也可以双递归   但是很慢 因为做了很多重复工作 如果用记忆化会快一丢丢
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.table = {}

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0

        return max(self.max_depth(root.left) + self.max_depth(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))



    def max_depth(self, node):
        if not node: return 0
        if node in self.table: return self.table[node]
        self.table[node] = 1 + max(self.max_depth(node.left), self.max_depth(node.right))

        return self.table[node]



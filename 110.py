# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs 自上而下
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        if abs(self.height(root.left) - self.height(root.right)) >= 2:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)



    def height(self, node):
        if not node:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1



# dfs 自下而上
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.recur_balance(root) != -1

    def recur_balance(self, node):
        if not node:
            return 0

        left = self.recur_balance(node.left)
        if left == - 1:
            return - 1

        right = self.recur_balance(node.right)
        if right == - 1:
            return - 1

        return max(left, right) + 1 if abs(left - right) < 2 else -1
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
# O(n ** 2)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        return abs(self.get_height(root.left) - self.get_height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)




    def get_height(self, root):
        if not root: return 0

        return 1 + max(self.get_height(root.left), self.get_height(root.right))




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




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = True

        def dfs(root):
            if not root:
                return 0

            left_height = dfs(root.left)
            right_height = dfs(root.right)

            if abs(left_height - right_height) > 1:
                self.flag = self.flag & False

            return 1 + max(left_height, right_height)

        dfs(root)

        return self.flag
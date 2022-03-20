class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        return self.dfs(root, 0)

    def dfs(self, node, sum_pre):
        if not node:
            return 0

        total = 10 * sum_pre + node.val
        if not node.left and not node.right:
            return total
        return self.dfs(node.left, total) + self.dfs(node.right, total)




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0


        def dfs(node, val):
            if not node: return None
            if not node.right and not node.left:
                self.res += 10 * val + node.val
                return None


            dfs(node.left, 10 * val + node.val)
            dfs(node.right, 10 * val + node.val)

        dfs(root, 0)

        return self.res



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, temp_val):
            if not node: return 0
            if not node.left and not node.right: return (10 * temp_val + node.val)

            return dfs(node.left, 10 * temp_val + node.val) + dfs(node.right, 10 * temp_val + node.val)

        return dfs(root, 0)


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.table = set()
        self.traversal(root)
        if len(self.table) == 1:
            return -1
        else:
            self.table.remove(min(self.table))
            return min(self.table)

    def traversal(self, root):
        if root:
            self.traversal(root.left)
            self.table.add(root.val)
            self.traversal(root.right)





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:

        self.first_small = float('+inf')
        self.second_small = float('+inf')
        def dfs(node):

            if node:
                if node.val < self.first_small:
                    self.second_small = self.first_small
                    self.first_small = node.val
                elif self.first_small < node.val < self.second_small:
                    self.second_small = node.val

                dfs(node.left)
                dfs(node.right)


        dfs(root)


        return -1 if self.second_small == float('+inf') else self.second_small



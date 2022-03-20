# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import defaultdict


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.mode = []
        self.preval = 0
        self.curtimes = 0
        self.maxtimes = 0

        self.inorder(root)

        return self.mode

    def inorder(self, node):
        if node:
            self.inorder(node.left)

            if self.preval == node.val:
                self.curtimes += 1
            else:
                self.preval = node.val
                self.curtimes = 1

            if self.curtimes == self.maxtimes:
                self.mode.append(node.val)
            elif self.curtimes > self.maxtimes:
                self.mode = [node.val]
                self.maxtimes = self.curtimes

            self.inorder(node.right)


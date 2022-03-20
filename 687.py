# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:

        def maxLen(node):
            if node == None:
                return 0
            left = maxLen(node.left)
            right = maxLen(node.right)
            if node.left:
                left = left + 1 if node.left.val == node.val else 0
            if node.right:
                right = right + 1 if node.right.val == node.val else 0

            self.res = max(self.res, left + right)
            return max(left, right)

        maxLen(root)
        return self.res




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return 0


        return max(self.count_same(root.left, root.val) + self.count_same(root.right, root.val), self.longestUnivaluePath(root.left), self.longestUnivaluePath(root.right))


    def count_same(self, node, val):
        if not node: return 0
        if node.val != val: return 0
        return 1 + max(self.count_same(node.left, val), self.count_same(node.right, val))



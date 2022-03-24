from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 双递归 肯定能过
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:

        if not root: return 0

        res = 0

        if self.is_same(root):
            res = 1

        return res + self.countUnivalSubtrees(root.left) + self.countUnivalSubtrees(root.right)


    def is_same(self, root):
        if not root: return True
        same_flag = True

        if root.left:
            same_flag = root.val == root.left.val and same_flag
        if root.right:
            same_flag = root.val == root.right.val and same_flag

        return same_flag == self.is_same(root.left) == self.is_same(root.right) == True




root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(3)
node5 = TreeNode(2)

root.left = node2
root.right = node3
node2.left = node4
node3.left = node5

print(Solution().countUnivalSubtrees(root))




class Solution:
    def countUnivalSubtrees(self, root):
        if not root: return 0
        self.count = 0

        def dfs(root):
            if not root.left and not root.right:
                self.count += 1
                return True

            same_flag = True

            if root.left:
                same_flag = dfs(root.left) and same_flag and root.left.val == root.val

            if root.right:
                same_flag = dfs(root.right) and same_flag and root.right.val == root.val

            if same_flag:
                self.count += 1
            return same_flag


        dfs(root)

        return self.count



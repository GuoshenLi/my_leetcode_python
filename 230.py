class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.res = []
        def inorder(root):
            if root:
                inorder(root.left)
                self.res.append(root.val)
                inorder(root.right)

        inorder(root)
        return self.res[k - 1]

# 变种的中序遍历 迭代
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = [root]
        count = 0

        while stack:
            stuff = stack.pop()
            if isinstance(stuff, TreeNode):
                stack.append(stuff.right)
                stack.append(stuff.val)
                stack.append(stuff.left)

            elif isinstance(stuff, int):
                count += 1
                if count == k:
                    return stuff




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.index = 0
        self.res = None
        def dfs(root):
            if root:
                if dfs(root.left): return True
                self.index += 1
                if self.index == k:
                    self.res = root.val
                    return True
                if dfs(root.right): return True

        dfs(root)
        return self.res
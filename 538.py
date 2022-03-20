class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.total = 0

        def dfs(root: TreeNode):
            if root:
                dfs(root.right)
                self.total += root.val
                root.val = self.total
                dfs(root.left)

        dfs(root)
        return root


class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root or not root.left: return root

        rootLeft = root.left
        rootRight = root.right
        resRoot = self.upsideDownBinaryTree(rootLeft)
        rootLeft.left = rootRight
        rootLeft.right = root
        root.left = None
        root.right = None
        return resRoot

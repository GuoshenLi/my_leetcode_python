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



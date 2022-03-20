# 二叉搜索树 增 删 查 可以不用parent的。
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)

        else: # root.val == key:
              # 最终真真正起作用的就这两条
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else: # 左右都有子树
                cur = root.right
                while cur.left:
                    cur = cur.left
                root.val = cur.val
                root.right = self.deleteNode(root.right, cur.val)

        return root






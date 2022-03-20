# 非常巧妙的双递归

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 当前节点的坡度 + 左子树的坡度 + 有子树的坡度
        return abs(self.sum_(root.left) - self.sum_(root.right)) + self.findTilt(root.left) + self.findTilt(root.right)



    # 计算这个节点为跟节点对应的子树的所有值之和
    def sum_(self, root):
        if not root:
            return 0

        return root.val + self.sum_(root.left) + self.sum_(root.right)




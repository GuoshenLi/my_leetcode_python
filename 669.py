# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root: return None
        # 因为二叉搜索树，当前节点的值比low小，则选择右边的子树。
        # 因为二叉搜索树，左边的子树会更小。因此不用考虑。
        if root.val < low: return self.trimBST(root.right, low, high)
        elif root.val > high: return self.trimBST(root.left, low, high)

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root


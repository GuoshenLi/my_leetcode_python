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

# 2022/7/5 我已经不再是从前那个少年
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        if not root: return 0
        self.res = 0

        def dfs(root):
            if not root: return 0

            left_sum = dfs(root.left)
            right_sum = dfs(root.right)

            self.res += abs(left_sum - right_sum)
            return left_sum + right_sum + root.val

        dfs(root)
        return self.res


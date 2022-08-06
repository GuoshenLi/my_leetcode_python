# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 注意转换思路
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        table = set()

        def calculate_sum(root):
            if not root: return 0
            res = root.val + calculate_sum(root.left) + calculate_sum(root.right)
            table.add(res)
            return res

        res = 0
        sum_all = calculate_sum(root)
        for item in table:
            res = max(res, item * (sum_all - item))

        return res % (10 ** 9 + 7)
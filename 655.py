# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        m = self.get_depth(root)
        n = 2 ** m - 1

        res = [[""] * n for i in range(m)]

        self.construct(res, 0, 0, n - 1, root)

        return res

    def construct(self, res, level, left, right, root):
        if not root: return None
        mid = (left + right) // 2
        res[level][mid] = str(root.val)
        self.construct(res, level + 1, left, mid - 1, root.left)
        self.construct(res, level + 1, mid + 1, right, root.right)


    def get_depth(self, root):
        if not root: return 0

        return max(self.get_depth(root.left), self.get_depth(root.right)) + 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.res = []
        self.table = {}

        def dfs(node):
            if not node: return '#'
            serial = str(node.val) + ' ' + dfs(node.left) + ' ' + dfs(node.right)

            if serial in self.table:
                self.table[serial] += 1
                if self.table[serial] == 2:
                    self.res.append(node)
            else:
                self.table[serial] = 1

            return serial
        dfs(root)
        return self.res
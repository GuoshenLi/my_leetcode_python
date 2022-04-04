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





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        self.table = defaultdict(list)

        # key: 先序遍历 val: tree_node
        def dfs(root):
            if not root: return '#'

            string = str(root.val) + ' ' + dfs(root.left) + ' ' + dfs(root.right)
            self.table[string].append(root)

            return string

        dfs(root)
        return list(v[0] for k, v in self.table.items() if len(v) > 1)


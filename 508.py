# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.table = {}
        self.dfs(root)

        max_time = max(item[1] for item in self.table.items())
        res = []
        for k, v in self.table.items():
            if v == max_time:
                res.append(k)
        return res

    def dfs(self, node):
        if not node: return 0

        val = node.val + self.dfs(node.left) + self.dfs(node.right)

        if val not in self.table:
            self.table[val] = 1
        else:
            self.table[val] += 1

        return val


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        table = defaultdict(int)

        def dfs(root):
            if not root: return 0

            left_sum = dfs(root.left)
            right_sum = dfs(root.right)

            res = left_sum + right_sum + root.val
            table[res] += 1
            return res

        dfs(root)
        res = []
        max_freq = max(table.values())
        for k, v in table.items():
            if v == max_freq:
                res.append(k)
        return res
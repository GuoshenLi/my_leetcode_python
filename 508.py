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



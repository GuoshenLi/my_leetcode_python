# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        parents = defaultdict(int)
        res = []

        def find_parents(root):
            if not root: return None
            if root.left:
                parents[root.left.val] = root
            if root.right:
                parents[root.right.val] = root
            find_parents(root.left)
            find_parents(root.right)

        def dfs(cur_node, previous_node, depth):
            if not cur_node: return None

            if depth == k:
                res.append(cur_node.val)

            if cur_node.left != previous_node:
                dfs(cur_node.left, cur_node, depth + 1)

            if cur_node.right != previous_node:
                dfs(cur_node.right, cur_node, depth + 1)

            if parents[cur_node.val] != previous_node:
                dfs(parents[cur_node.val], cur_node, depth + 1)


        find_parents(root)
        dfs(target, None, 0)
        return res



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        def dfs(node):
            if not node:
                return
            if node.left:
                dct[node.left.val].append(node.val)
                dct[node.val].append(node.left.val)
            if node.right:
                dct[node.right.val].append(node.val)
                dct[node.val].append(node.right.val)
            dfs(node.left)
            dfs(node.right)
            return None



        dct = defaultdict(list)
        dfs(root)
        this_level = deque()
        this_level.append(target.val)
        visited = set()
        visited.add(target.val)

        while k:
            next_level = deque()
            while this_level:
                node = this_level.popleft()
                for neighbor in dct[node]:
                    if neighbor not in visited:
                        next_level.append(neighbor)
                        visited.add(neighbor)

            this_level = next_level
            k -= 1

        return list(this_level)



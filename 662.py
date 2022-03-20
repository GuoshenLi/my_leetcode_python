# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque


class Solution:
    def widthOfBinaryTree(self, root):
        queue = deque()
        queue.append((root, 0))
        ans = 0
        while queue:
            n = len(queue)

            for i in range(n):
                node, pos = queue.popleft()
                if i == 0:
                    left = pos
                if i == n - 1:
                    right = pos
                if node.left:
                    queue.append((node.left, pos * 2 + 1))
                if node.right:
                    queue.append((node.right, pos * 2 + 2))

            ans = max(right - left + 1, ans)

        return ans
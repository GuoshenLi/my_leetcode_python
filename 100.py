# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        que_1 = deque()
        que_2 = deque()
        que_1.append(p)
        que_2.append(q)

        while que_1 or que_2:
            leftnode = que_1.popleft()
            rightnode = que_2.popleft()

            if not leftnode and not rightnode:
                continue

            if not leftnode or not rightnode:
                return False

            if leftnode.val != rightnode.val:
                return False
            else:
                que_1.append(leftnode.left)
                que_1.append(leftnode.right)
                que_2.append(rightnode.left)
                que_2.append(rightnode.right)


        return True
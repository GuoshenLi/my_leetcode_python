# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

####### 判断两棵树（给定两个指针）是否满足一定的条件，可以使用先序遍历（dfs， bfs（队列））。
# 先判断左右节点的值是否一样，若一样再判断左右节点的左右孩子是否满足一定条件 101与100是一样套路的题目
# 要注意边界条件，1：两个节点均为空 2：两个节点有一个为空 3：两个节点不为空（看节点值是否相等（分两种））共四种情况
####### 背代码 #####

#### dfs （先序遍历）####
from collections import deque
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.recur_sym(root.left, root.right)

    def recur_sym(self, leftnode, rightnode):
        if not leftnode and not rightnode:
            return True

        if not leftnode or not rightnode:
            return False

        if leftnode.val != rightnode.val:
            return False
        else:
            return self.recur_sym(leftnode.left, rightnode.right) and self.recur_sym(leftnode.right, rightnode.left)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        que_1 = deque()
        que_2 = deque()

        que_1.append(root.left)
        que_2.append(root.right)

        while que_1 and que_2:
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

                que_2.append(rightnode.right)
                que_2.append(rightnode.left)


        return True





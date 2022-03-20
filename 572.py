# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 双递归


# 要判断一个树 t 是不是树 s 的子树，那么可以判断 t 是否和树 s 的任意子树相等。那么就转化成 100. Same Tree。
# 即，这个题的做法就是在 s 的每个子节点上，判断该子节点是否和 t 相等。
#
# 判断两个树是否相等的三个条件是与的关系，即：
#
# 当前两个树的根节点值相等；
# 并且，s 的左子树和 t 的左子树相等；
# 并且，s 的右子树和 t 的右子树相等。
# 而判断 t 是否为 s 的子树的三个条件是或的关系，即：
#
# 当前两棵树相等；
# 或者，t 是 s 的左子树；
# 或者，t 是 s 的右子树。
# 判断 是否是相等的树 与 是否是子树 的代码简直是对称美啊~


# 双递归第三题，只用在树的题目：
# 都是一样的。is_same函数是一个递归调用子函数
# isSub_Tree函数，调用is_same函数判断当前节点是不是相等，再调用自身isSub_Tree函数判断左右节点是不是子树
# 先另外函数再两个自身函数！！ 最重要这一点！！
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        if not s or not t:
            return False
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)




    # 判断树相不相同
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False

        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)

